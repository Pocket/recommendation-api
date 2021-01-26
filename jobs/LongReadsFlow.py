import json
import logging
import os
import sys

from metaflow import FlowSpec, step, Parameter, IncludeFile, conda, conda_base, schedule, Flow, namespace
from utils import setup_logger


@schedule(hourly=True)
@conda_base(libraries={"elasticsearch": "7.1.0", "elasticsearch-dsl": "7.1.0",
                       "requests-aws4auth": "1.0.1", "scikit-learn": "0.23.2",
                       "scipy": "1.5.3", "gql": "2.0.0"})
class LongReadsCandidatesFlow(FlowSpec):

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

    min_saves = Parameter("min_saves",
                          help="minimum required saves for recommendation filtering, default is 45",
                          type=int,
                          default=45)

    min_words = Parameter("min_words",
                          help="minimum required word count for recommendation filtering, default is 4500 \
                                based on a reading time of 20 mins and 225 words/min reading speed.",
                          type=int,
                          default=4500)

    time_scale = Parameter("time_scale",
                           help="The time scale for the decay in elastic search, default is 6 days",
                           type=str,
                           default="18d")

    save_origin = Parameter("save_origin",
                            help="The origin for the save decay in elastic search, default is 600",
                            type=int,
                            default=600)

    save_scale = Parameter("save_scale",
                           help="The 0.5 scale for save decay for elastic search, default is 300",
                           type=int,
                           default=300)

    approval_threshold = Parameter("approval_threshold",
                                   help="The minimum percentile for approval probability, default is 20",
                                   type=int,
                                   default=30)

    filter_curated = Parameter("filter_curated",
                               help="Flag to filter of curated items from results.",
                               type=bool,
                               default=False)

    approval_modeling = Parameter("approval_modeling",
                                  help="Flag to rank items using curated approval model.",
                                  type=bool,
                                  default=True)

    domain_allowlist_file = IncludeFile("domain_allowlist_file",
                                        is_text=True,
                                        help="Pocket domain allowlist",
                                        default="./resources/domain_allowlist_20200630.json")

    """
    A flow where Metaflow generates long reads candidates.
    """
    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.
        """
        import boto3
        from elasticsearch import Elasticsearch, RequestsHttpConnection
        from requests_aws4auth import AWS4Auth

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info("LongReadsCandidatesFlow is starting.")

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

        self.next(self.get_generic_approval_ranker)

    @step
    def get_generic_approval_ranker(self):
        """
        step to load models trained in ExploreTopicTrainingFlow
        """

        """
        Here we need to change the namespace to the production one of the corresponding model we are looking to pull
        Once https://github.com/Netflix/metaflow/issues/384 is merged and the topic model training has the right tags 
        added we will be able to change this to just "production" and pull it from AWS Secrets Manager
        """
        namespace("production:exploretopictrainingflow-0-eins")

        training_run = Flow("ExploreTopicTrainingFlow").latest_successful_run
        self.model_run_id = training_run.id
        # get vectorizer, one hot mappings for google categories and domains
        self.featurizer = training_run.data.featurizer

        # get per-topic approval models
        self.approval_model = training_run.data.generic_classifier

        self.next(self.get_results)

    @step
    def get_results(self):
        """
        A step for metaflow to issue a single topic query and get the results
        from elastic search and apply model-based ranking
        """

        from elasticsearch_dsl import Search
        from elasticsearch.exceptions import NotFoundError, RequestError, AuthorizationException
        from query import algorithmic_by_counts, postprocess_search_results
        from ranking import apply_rankers

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logger.info("Metaflow says its time to get longreads results")
        logger.info(f"min_saves: {self.input}, scale: {self.time_scale} \
                    filter_curated: {self.filter_curated}, approval_ranking: {self.approval_modeling}")
        longreads_query, score_functions = algorithmic_by_counts(min_saves=self.min_saves,
                                                                 scale=self.time_scale,
                                                                 min_words=self.min_words,
                                                                 save_origin=self.save_origin,
                                                                 save_scale=self.save_scale)

        domain_allowlist = json.loads(self.domain_allowlist_file)
        logger.info(f"Metaflow says its time to get some elasticsearch results for long reads")
        logger.info(f"min_saves: {self.min_saves} scale: {self.time_scale} min_words: {self.min_words}")

        try:
            s = Search(using=self.es, index=self.es_path).query("function_score",
                                                                query=longreads_query,
                                                                min_score=0.01,
                                                                functions=score_functions)

            # get extra results in case some are duplicates or filtered downstream
            total = min(900, self.limit*9)
            s = s[:total]
            self.search_results = postprocess_search_results(s.execute().to_dict(),
                                                             domain_allowlist,
                                                             self.limit*6)

        except (NotFoundError, RequestError, AuthorizationException) as err:
            logger.error("ElasticSearch " + str(err))
            sys.exit(1)

        logger.info(f"Metaflow says its time to get apply ranking models to elasticsearch results for long reads")
        results = apply_rankers(self.search_results,
                                topic_predictor=None,
                                approval_model=self.approval_model,
                                count=self.limit,
                                featurizer=self.featurizer,
                                approval_percentile=self.approval_threshold)

        self.final_results = [{"feed_name": "longreads",
                               "items": results}]
        logger.info(f"Returned {len(results)} for long reads")
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        pass

if __name__ == '__main__':
    setup_logger()
    LongReadsCandidatesFlow()
