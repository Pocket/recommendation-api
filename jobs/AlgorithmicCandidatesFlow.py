import json
import logging
import boto3
import os
from metaflow import FlowSpec, step, Parameter, IncludeFile, conda, conda_base, schedule, Flow, namespace

from utils import setup_logger
from query import FEED_ID_EN_US


@schedule(hourly=True)
@conda_base(libraries={"elasticsearch": "7.1.0", "elasticsearch-dsl": "7.1.0",
                       "requests-aws4auth": "1.0.1", "scikit-learn": "0.23.2",
                       "scipy":"1.5.3", "gql":"2.0.0"})
class AlgorithmicCandidatesFlow(FlowSpec):

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
                      default=45)

    feed_id = Parameter("feed_id",
                        help="The curated feed_id, default is en-US.",
                        type=int,
                        default=FEED_ID_EN_US)

    domain_allowlist_file = IncludeFile("domain_allowlist_file",
                                        is_text=True,
                                        help="Pocket domain allowlist",
                                        default="./resources/domain_allowlist_20200630.json")

    """
    A flow where Metaflow generates algorithmic candidates.
    """
    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.
        """
        from elasticsearch import Elasticsearch, RequestsHttpConnection
        from requests_aws4auth import AWS4Auth
        from jobs.utils import get_topic_map

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logger.info("AlgorithmicCandidatesFlow is starting.")
        self.topic_map = get_topic_map()
        self.domain_allowlist = json.loads(self.domain_allowlist_file)
        self.topics = [k for k, x in self.topic_map.items() if x["pageType"] == "topic_page"]
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

        self.next(self.get_ranking_models)

    @step
    def get_ranking_models(self):
        """
        step to load models trained in ExploreTopicTrainingFlow
        """

        """
        Here we need to change the namespace to the production one of the corresponding model we are looking to pull
        Once https://github.com/Netflix/metaflow/issues/384 is merged and the topic model training has the right tags 
        added we will be able to change this to just "production" and pull it from AWS Secrets Manager
        """
        # TODO: can we change the below to match the new service name - Recommendation API?
        namespace("production:exploretopictrainingflow-0-eins")

        training_run = Flow("ExploreTopicTrainingFlow").latest_successful_run
        self.model_run_id = training_run.id
        # get vectorizer, one hot mappings for google categories and domains
        self.featurizer = training_run.data.featurizer

        # get generic approval model
        self.generic_ranking_model = training_run.data.generic_classifier

        # get per-topic approval models
        self.topic_approval_models = training_run.data.approval_classifiers

        # get per-topic categorization models
        self.topic_predictors = training_run.data.topic_predictors

        self.next(self.get_results, foreach='topics')

    @step
    def get_results(self):
        """
        A step for metaflow to issue a single topic query and get the results
        from elastic search and apply model-based ranking
        """

        from elasticsearch_dsl import Search
        from elasticsearch.exceptions import NotFoundError, RequestError, AuthorizationException
        from jobs.query import algorithmic_by_topic, postprocess_search_results
        from jobs.ranking import apply_rankers

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logger.info(f"Metaflow says its time to get the query for: {self.input}")
        topic_query, score_fuctions = algorithmic_by_topic(self.input, self.topic_map)
        self.topic_id = self.input

        logger.info(f"Metaflow says its time to get some elasticsearch results for: {self.input}")
        try:
            s = Search(using=self.es, index=self.es_path).query("function_score",
                                                                query=topic_query,
                                                                min_score=0.01,
                                                                functions=score_fuctions)

            # get 3x results in case some are duplicates or filtered downstream
            total = min(9000, self.limit*9)
            s = s[:total]
            self.search_results = postprocess_search_results(s.execute().to_dict(),
                                                             self.domain_allowlist,
                                                             self.limit*6)

        except (NotFoundError, RequestError, AuthorizationException) as err:
            logger.error("ElasticSearch " + str(err))

        logger.info(f"Metaflow says its time to get apply ranking models to elasticsearch results for: {self.input}")
        # model files are dicts keyed on curator labels
        curator_label = self.topic_map[self.topic_id]["curatorLabel"]
        self.ranked_results = apply_rankers(self.search_results,
                                            self.topic_predictors[curator_label],
                                            self.topic_approval_models[curator_label],
                                            self.limit,
                                            self.featurizer)

        self.next(self.join)

    @step
    def join(self, inputs):
        """
        a step in which single topic results are combined together in a single output dict
        """
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        logger.info("Metaflow says its time to join the results")
        self.final_results = [{"topic_id": job.topic_map[job.topic_id].get("id"), "items": job.ranked_results} for job in inputs]
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        for t in self.final_results:
            logger.info(f"Returned {len(t['items'])} for {t['topic_id']}")
        logger.info("AlgorithmicCandidatesFlow is done.")


if __name__ == '__main__':
    setup_logger()
    AlgorithmicCandidatesFlow()
