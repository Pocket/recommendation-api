from typing import Optional, List

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.link import LinkModel
from app.rankers.algorithms import thompson_sampling


class CollectionSlateProvider(SlateProvider):

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
        return '92af3dae-25c9-46c3-bf05-18082aacc7e1'

    @property
    def headline(self) -> str:
        return 'Popular Collections'

    @property
    def subheadline(self) -> str:
        return 'Curated guides to the best reads on the web'

    @property
    def more_link(self) -> Optional[LinkModel]:
        return LinkModel(text='Explore more Collections', url='https://getpocket.com/collections')

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
                trailing_period=14,  # With a low impression volume, a longer period should help find the best stories
                default_alpha_prior=18,   # beta * P95 item CTR for this slate (1.5%)
                default_beta_prior=1200)  # 20% of average daily item impressions for this slate

        return items
