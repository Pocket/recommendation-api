import logging
import boto3
import os
from metaflow import FlowSpec, step, Parameter, IncludeFile, conda_base, schedule

from jobs.query import organic_by_topic, collection_by_feed, merge_collection_results, transform_curated_results
from jobs.utils import setup_logger, get_topic_map

@schedule(hourly=True)
@conda_base(libraries={'elasticsearch': '7.1.0', 'elasticsearch-dsl': '7.1.0',
                       'requests-aws4auth': '1.0.1', "numpy":"1.19.1"})
class CollectionCandidatesFlow(FlowSpec):

    es_endpoint = Parameter("es_endpoint",
                            help="elasticsearch endpoint",
                            type=str,
                            default="search-item-recs-wslncyus6txlpavliekv7bvrty.us-east-1.es.amazonaws.com")

    es_path = Parameter("es_path",
                        help="elasticsearch index",
                        type=str,
                        default="item-rec-data_v3")

    limit = Parameter("limit",
                      help="The number of items to recommend in the topic.",
                      type=int,
                      default=15)

    """
    A flow where Metaflow retrieves curated items for dedicated collections (i.e. COVID) from elastic search.
    """
    @step
    def start(self):
        """
        This step sets up elasticsearch connection
        """

        from elasticsearch import Elasticsearch, RequestsHttpConnection
        from requests_aws4auth import AWS4Auth

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logger.info("CollectionCandidatesFlow is starting.")
        self.topic_map = get_topic_map()
        self.topics = [k for k, x in self.topic_map.items() if x["pageType"] == "editorial_collection" and x["isDisplayed"]]
        logger.info(f"flow will process {len(self.topics)} topics.")

        session = boto3.Session()
        credentials = session.get_credentials()
        region = os.environ.get('AWS_REGION', 'us-east-1')
        awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, "es",
                           session_token=credentials.token)
        self.es = Elasticsearch(
            hosts=[{'host': self.es_endpoint, 'port': 443}],
            http_auth=awsauth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )

        self.next(self.get_results, foreach='topics')

    @step
    def get_results(self):
        """
        A step for metaflow to issue a single topic query and get the results
        """

        from elasticsearch_dsl import Search
        from elasticsearch.exceptions import NotFoundError, RequestError, AuthorizationException

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logger.info(f"Metaflow says its time to get the topic label-based query for: {self.input}")
        topic_query = organic_by_topic(self.input, self.topic_map, feed=1)
        self.topic_key = self.input

        results1, results2 = {}, {}
        try:
            s = Search(using=self.es, index=self.es_path).query(
                       topic_query).sort("-approved_feeds.approved_feed_time_live")

            # get full set of results in both queries
            # in case some are duplicates or filtered downstream
            s = s[:self.limit]
            results1 = s.execute().to_dict()

            print(f"by curator label returns {len(results1['hits']['hits'])} items")

        except (NotFoundError, RequestError, AuthorizationException) as err:
            logger.error("ElasticSearch " + str(err))

        colln_feed_id = self.topic_map[self.input].get("customFeedId")
        if colln_feed_id:
            logger.info(f"Metaflow says its time to get the custom feed-based query for: {self.input}")
            topic_query = collection_by_feed(colln_feed_id)
            try:
                s = Search(using=self.es, index=self.es_path).query(
                           topic_query).sort("-approved_feeds.approved_feed_time_live")

                # get full set of results in both queries
                # in case some are duplicates or filtered downstream
                s = s[:self.limit]
                results2 = s.execute().to_dict()

                print(f"by feed_id returns {len(results2['hits']['hits'])} hits")

            except (NotFoundError, RequestError, AuthorizationException) as err:
                logger.error("ElasticSearch " + str(err))

            self.results = merge_collection_results(results1, 1, results2, feed_id2=colln_feed_id)
        else:
            self.results = transform_curated_results(results1, feed_id=1)

        self.next(self.join)

    @step
    def join(self, inputs):
        """
        a step in which single topic results are combined together in a single output dict
        """
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        logger.info("Metaflow says its time to join the results")
        self.final_results = [{"topic_id": input.topic_key, "items": input.results} for input in inputs]
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        print("CuratedCandidatesFlow is done.")


if __name__ == '__main__':
    setup_logger()
    CollectionCandidatesFlow()
