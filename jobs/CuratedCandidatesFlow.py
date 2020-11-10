import json
import logging
import time
import boto3
import os
from metaflow import FlowSpec, step, Parameter, IncludeFile, conda_base, schedule
from query import organic_by_topic, transform_curated_results
from utils import setup_logger


@schedule(hourly=True)
@conda_base(libraries={'elasticsearch': '7.1.0', 'elasticsearch-dsl': '7.1.0',
                       'requests-aws4auth': '1.0.1', "numpy": "1.19.1"})
class CuratedCandidatesFlow(FlowSpec):

    es_endpoint = Parameter("es_endpoint",
                            help="elasticsearch endpoint",
                            default="search-item-recs-wslncyus6txlpavliekv7bvrty.us-east-1.es.amazonaws.com")

    es_path = Parameter("es_path",
                        help="elasticsearch index",
                        default="item-rec-data_v3")

    limit = Parameter("limit",
                      help="The number of items to recommend in the topic.",
                      default=15)

    feed_id = Parameter("feed_id",
                        help="The curated feed_id, default is en-US.",
                        default=1)

    topic_map_file = IncludeFile("topic_map_file",
                                 is_text=True,
                                 help="Pocket topic info file",
                                 default="./app/resources/topics_weights.json")

    """
    A flow where Metaflow retrieves curated items from elastic search.
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

        logger.info("CuratedCandidatesFlow is starting.")
        self.topic_map = json.loads(self.topic_map_file)
        self.topics = [k for k, x in self.topic_map.items() if x["page_type"] == "topic_page" and x["is_displayed"]]
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

        logger.info(f"Metaflow says its time to get the query for: {self.input}")
        topic_query = organic_by_topic(self.input, self.topic_map, feed=self.feed_id)
        self.topic_id = self.input

        print("Metaflow says its time to get some elasticsearch results for: ", self.input)
        start_time = time.time()
        version = 3
        try:
            s = Search(using=self.es, index=self.es_path).query(
                       topic_query).sort("-approved_feeds.approved_feed_time_live")

            # get 3x results in case some are duplicates or filtered downstream
            s = s[:(self.limit * 3)]
            self.results = transform_curated_results(s.execute().to_dict(), feed_id=self.feed_id)

        except (NotFoundError, RequestError, AuthorizationException) as err:
            logger.error("ElasticSearch " + str(err))

        elapsed_time = round((time.time() - start_time) * 1000, 2)
        logger.info(f"organic by topic: version={version}, elapsed time={elapsed_time}")

        self.next(self.join)

    @step
    def join(self, inputs):
        """
        a step in which single topic results are combined together in a single output dict
        """
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        logger.info("Metaflow says its time to join the results")
        self.final_results = [{"topic_id": input.topic_id, "items": input.results} for input in inputs]
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
    CuratedCandidatesFlow()
