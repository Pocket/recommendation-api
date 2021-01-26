import json
import logging

from metaflow import FlowSpec, step, Parameter, IncludeFile, conda, conda_base, schedule, Flow, namespace
from utils import setup_logger


@schedule(hourly=True)
@conda_base(libraries={"elasticsearch": "7.1.0", "elasticsearch-dsl": "7.1.0",
                       "requests-aws4auth": "1.0.1", "scikit-learn": "0.23.2",
                       "scipy": "1.5.3", "gql": "2.0.0"})
class TrendingCandidatesFlow(FlowSpec):

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

    time_scale = Parameter("time_scale",
                           help="The time scale for the decay in elastic search, default is 6 days",
                           type=str,
                           default="12d")

    save_origin = Parameter("save_origin",
                            help="The origin for the save decay in elastic search, default is 600",
                            type=int,
                            default=600)

    save_scale = Parameter("save_scale",
                           help="The 0.5 scale for save decay for elastic search, default is 300",
                           type=int,
                           default=300)

    approval_threshold = Parameter("approval_threshold",
                                   help="The minimum percentile for approval probability, default is 30",
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
    A flow where Metaflow generates trending candidates.
    """
    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.
        """
        from utils import elasticsearch_connect

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info("TrendingCandidatesFlow is starting.")
        self.es = elasticsearch_connect(self.es_endpoint)

        self.next(self.get_generic_approval_ranker)

    @step
    def get_generic_approval_ranker(self):
        """
        step to load models trained in ExploreTopicTrainingFlow
        """

        from utils import load_generic_approval_ranker
        self.model_run_id, self.featurizer, self.approval_model = load_generic_approval_ranker()

        self.next(self.get_results)

    @step
    def get_results(self):
        """
        A step for metaflow to issue a single topic query and get the results
        from elastic search and apply model-based ranking
        """
        from utils import query_elasticsearch
        from query import algorithmic_by_counts

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logger.info("Metaflow says its time to get trending results")
        logger.info(f"min_saves: {self.input}, scale: {self.time_scale} \
                    filter_curated: {self.filter_curated}, approval_ranking: {self.approval_modeling}")
        trending_query, score_functions = algorithmic_by_counts(min_saves=self.min_saves,
                                                                scale=self.time_scale,
                                                                save_origin=self.save_origin,
                                                                save_scale=self.save_scale)

        domain_allowlist = json.loads(self.domain_allowlist_file)
        logger.info(f"Metaflow says its time to get some elasticsearch results for trending")
        logger.info(f"min_saves: {self.min_saves} scale: {self.time_scale} min_words: {self.min_words}")

        search_results = query_elasticsearch(trending_query, score_functions, domain_allowlist,
                                             self.es, self.es_path, None, self.approval_model,
                                             self.featurizer, self.approval_threshold, self.limit)

        self.final_results = [{"feed_name": "trending",
                               "items": search_results}]
        logger.info(f"Returned {len(search_results)} for trending")
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
    TrendingCandidatesFlow()
