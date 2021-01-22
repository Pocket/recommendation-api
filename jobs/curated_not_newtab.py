import os
from metaflow import FlowSpec, Parameter, step, conda_base
import logging

FEED_ID_EN_US = 1

@conda_base(libraries={"elasticsearch": "7.1.0", "elasticsearch-dsl": "7.1.0",
                       "requests-aws4auth": "1.0.1", "numpy": "1.19.1"})
class CuratedNotNewTab(FlowSpec):

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
                      default=30)

    feed_id = Parameter("feed_id",
                        help="Limit to this feed_id",
                        type=int,
                        default=FEED_ID_EN_US)

    @step
    def start(self):
        from elasticsearch import Elasticsearch, RequestsHttpConnection
        from elasticsearch_dsl import Search
        from requests_aws4auth import AWS4Auth
        import boto3
        from query import curated_older_than, order_curated_by_approval_time

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

        s = Search(using=self.es, index=self.es_path).query(curated_older_than(self.feed_id)).sort("-approved_feeds.approved_feed_time_live")
        s = s[:(self.limit * 3)]
        self.results = order_curated_by_approval_time(s.execute().to_dict(), self.feed_id)
        logging.info("Got %d results", len(self.results))
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == '__main__':
    CuratedNotNewTab()
