from typing import List

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.rankers.algorithms import thompson_sampling


class RecommendedReadsSlateProvider(SlateProvider):

    def __init__(
            self,
            corpus_feature_group_client: CorpusFeatureGroupClient,
            corpus_engagement_provider: CorpusEngagementProvider,
            recommendation_surface_id: RecommendationSurfaceId,
    ):
        super().__init__(corpus_feature_group_client)
        self.corpus_engagement_provider = corpus_engagement_provider
        self.recommendation_surface_id = recommendation_surface_id

    @property
    def candidate_set_id(self) -> str:
        return '5f0dae93-a5a8-439a-a2e2-5d418c04bc98'

    @property
    def headline(self) -> str:
        return 'Recommended Reads'

    @property
    def subheadline(self) -> str:
        return 'Curated by Pocket'

    async def rank_corpus_items(
            self,
            items: List[CorpusItemModel],
            *args,
            **kwargs,
    ) -> List[CorpusItemModel]:
        """
        :param items: Candidate corpus items
        :return: Ranks items based on Thompson sampling if enable_thompson_sampling is True.
        """
        if kwargs.get('enable_thompson_sampling'):
            metrics = await self.corpus_engagement_provider.get(
                self.recommendation_surface_id, self.configuration_id, items)

            items = thompson_sampling(
                recs=items,
                metrics=metrics,
                trailing_period=7,  # With few new items/day and relatively many impressions, a low period is sufficient
                default_alpha_prior=12,   # beta * P95 item CTR for this slate (0.7%)
                default_beta_prior=1700)  # 5% of average daily item impressions for this slate

        return items
