import uuid

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.corpus.corpus_fetchable import CorpusFetchable
from app.data_providers.metrics_client import MetricsFetchable
from app.data_providers.slate_provider import SlateProvider
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel


class SetupMomentDispatch:
    """
    This is a shortcut dispatch halper for launching Setup Moment more quickly. We will want to migrate
    setup moment to RankingDispatch as soon as we want to include rankers or experimentation.
    """

    SETUP_MOMENT_CORPUS_CANDIDATE_SET_ID = 'deea0f06-9dc9-44a5-b864-fea4a4d0beb7'
    DISPLAY_NAME = 'display name'
    SUB_HEADLINE = 'sub headline'
    CORPUS_IDS = ['foo']

    def __init__(self, corpus_client: CorpusFeatureGroupClient):
        self.corpus_client = corpus_client

    async def get_ranked_corpus_slate(self) -> CorpusSlateModel:
        items = await self.corpus_client.get_corpus_items(self.CORPUS_IDS)
        recommendations = [CorpusRecommendationModel(id=uuid.uuid4().hex, corpus_item=item) for item in items]

        return CorpusSlateModel(
            id=self.SETUP_MOMENT_CORPUS_CANDIDATE_SET_ID,
            headline=self.DISPLAY_NAME,
            subheadline=self.SUB_HEADLINE,
            recommendations=recommendations,
        )


class RankingDispatch:
    """
    This class is responsible for accepting:

     a dependency to get items to rank (api_client),
     a strategy for ranking them (slate_provider),
     and the data to execute ranking (metrics_client),

     and then using those three things to shape the list of items to the order and size we serve to a client.

     If there are NO rankers, it sends the original list of items, with no reshaping, to the client.
    """
    def __init__(
            self,
            corpus_client: CorpusFetchable,
            slate_provider: SlateProvider,
            metrics_client: MetricsFetchable
    ):
        self.corpus_client = corpus_client
        self.slate_provider = slate_provider
        self.metrics_client = metrics_client

    async def get_ranked_corpus_slate(self, slate_id) -> CorpusSlateModel:
        """
        From a slate identifier find the appropriate experiment. Then fetch the candidate set and sort the corpus items.
        :param slate_id: defined in `slate_configs.json`
        :return: CorpusSlateModel
        """
        corpus_slate_schema = self.slate_provider.getSlate(slate_id)
        experiment = self.slate_provider.get_random_experiment(slate_id)

        # Fetch Corporeal Candidates
        items = await self.corpus_client.get_corpus_items(experiment.corpus_ids())
        items = await self.metrics_client.rank_items(items, experiment.rankers)

        recommendations = [CorpusRecommendationModel(id=uuid.uuid4().hex, corpus_item=item) for item in items]

        return CorpusSlateModel(
            id=slate_id,
            headline=corpus_slate_schema.displayName,
            subheadline=corpus_slate_schema.description,
            recommendations=recommendations,
        )
