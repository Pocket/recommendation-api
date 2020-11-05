import json
import logging
import time
import boto3
import os
from metaflow import FlowSpec, step, Parameter, IncludeFile, conda_base

from jobs.query import organic_by_topic, collection_by_feed, merge_collection_results, transform_results
from jobs.utils import setup_logger

#  @schedule(hourly=True)
@conda_base(libraries={'elasticsearch': '7.1.0', 'elasticsearch-dsl': '7.1.0',
                       'requests-aws4auth': '1.0.1', "numpy":"1.19.1"})
class CollectionCandidatesFlow(FlowSpec):
    ENV = {"prod": {"s3_bucket": "s3://pocket-data-models",
                    "s3_item": "curated_test.json",
                    "es_path": "item-rec-data_v3",
                    "es_endpoint": "search-item-recs-wslncyus6txlpavliekv7bvrty.us-east-1.es.amazonaws.com"}
          }

    env = Parameter("env",
                    help="The deployment environment",
                    required=True)

    limit = Parameter("limit",
                      help="The number of items to recommend in the topic.",
                      default=15)

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
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.
        """

        from elasticsearch import Elasticsearch, RequestsHttpConnection
        from requests_aws4auth import AWS4Auth

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logger.info("CuratedCandidatesFlow is starting.")
        self.es_endpoint = self.ENV[self.env]['es_endpoint']
        self.es_path = self.ENV[self.env]['es_path']
        self.topic_map = json.loads(self.topic_map_file)
        self.topics = [k for k, x in self.topic_map.items() if x["page_type"] == "editorial_collection" and x["is_displayed"]]
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
        A step for metaflow to get the topic query and issue per topic
        """

        from elasticsearch_dsl import Search
        from elasticsearch.exceptions import NotFoundError, RequestError, AuthorizationException

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logger.info(f"Metaflow says its time to get the query for: {self.input}")
        topic_query = organic_by_topic(self.input, self.topic_map)
        self.topic_key = self.input

        print("Metaflow says its time to get some elasticsearch results for: ", self.input)
        start_time = time.time()
        version = 3
        results1, results2 = {}, {}
        try:
            s = Search(using=self.es, index=self.es_path).query(
                       topic_query).sort("-approved_feeds.approved_feed_time_live")

            # get 3x results in case some are duplicates or filtered downstream
            s = s[:self.limit]
            results1 = s.execute().to_dict()

        except (NotFoundError, RequestError, AuthorizationException) as err:
            logger.error("ElasticSearch " + str(err))

        feed_id = self.topic_map[self.input].get("custom_feed_id")
        if feed_id:
            topic_query = collection_by_feed(feed_id)
            try:
                s = Search(using=self.es, index=self.es_path).query(
                           topic_query).sort("-approved_feeds.approved_feed_time_live")

                # get 3x results in case some are duplicates or filtered downstream
                s = s[:self.limit]
                results2 = s.execute().to_dict()

            except (NotFoundError, RequestError, AuthorizationException) as err:
                logger.error("ElasticSearch " + str(err))

            self.results = merge_collection_results(results1, results2)
        else:
            self.results = transform_results(results1, curated=True)

        elapsed_time = round((time.time() - start_time) * 1000, 2)
        logger.info(f"organic_by_topic: version={version}, elapsed time={elapsed_time}")

        self.next(self.join)

    @step
    def join(self, inputs):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        logger.info("Metaflow says its time to join the results")
        self.final_results = {input.topic_key: input.results for input in inputs}
        for t, r in self.final_results.items():
            c = r["curated_recommendations"]
            logger.info(f"{t} returned {len(c)} curated results.")

        self.output = json.dumps(self.final_results)
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
