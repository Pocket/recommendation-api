import logging
from typing import List
from uuid import uuid5, UUID

from app.data_providers.corpus.corpus_api_client import CorpusApiClient
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.data_providers.util import integer_hash
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel
from app.rankers.algorithms import thompson_sampling

# Maximum tileId that Firefox can support. Firefox uses Javascript to store this value. The max value of a Javascript
# number can be found using `Number.MAX_SAFE_INTEGER`. which is 2^53 - 1 because it uses a 64-bit IEEE 754 float.
MAX_TILE_ID = 1 << 53 - 1
# Generate tile_ids well out of the range of the MySQL-based system, which has a max tile_id of 99,999 as of 2023-03-13.
# This is done to make it easy for engineers/analysts to see which system generated the identifier.
MIN_TILE_ID = 100 * 100000


class NewTabSlateProvider(SlateProvider):

    def __init__(
            self,
            corpus_api_client: CorpusApiClient,
            corpus_engagement_provider: CorpusEngagementProvider,
            recommendation_surface_id: RecommendationSurfaceId,
            locale: LocaleModel):
        """
        The only difference between this constructor and the parent one is that it explicitly requires a CorpusApiClient
        :param corpus_api_client: Client that gets corpus from Curated Corpus API.
        """
        super().__init__(
            corpus_fetchable=corpus_api_client,
            corpus_engagement_provider=corpus_engagement_provider,
            recommendation_surface_id=recommendation_surface_id,
            locale=locale)

        self.corpus_api_client = corpus_api_client

    @property
    def candidate_set_id(self) -> str:
        # The recommendation_surface_id (e.g. NEW_TAB_EN_US) uniquely identifies the candidates for the New Tab slate.
        return self.recommendation_surface_id.value

    @property
    def candidate_set_uuid(self) -> UUID:
        """
        :return: A UUID uniquely identifying the candidate_set_id, as is expected by the base class.
        """
        # The UUID on the left is an arbitrary one.
        return uuid5(UUID('8066f150-6e8d-4f1b-a432-d7260e1aad78'), self.candidate_set_id)

    @property
    def headline(self) -> str:
        return 'Recommended by Pocket'  # Strings on New Tab are provided and localized by the Firefox client.

    async def get_recommendations(
            self,
            ranked_items: List[CorpusItemModel],
            *args,
            **kwargs,
    ) -> List[CorpusRecommendationModel]:
        """
        :return: CorpusRecommendationModel with a tileId that's used in Firefox telemetry to identify items. tileId
                 uniquely identifies the scheduled surface, scheduled time, and CorpusItem.id of a recommendation.
        """
        return [
            CorpusRecommendationModel(
                corpus_item=item,
                tile_id=integer_hash(self._get_tile_id_key(item), start=MIN_TILE_ID, stop=MAX_TILE_ID + 1)
            ) for item in ranked_items
        ]

    def _get_tile_id_key(self, item: CorpusItemModel) -> str:
        """
        :return: A string that identifiers the scheduled surface, scheduled date, and CorpusItem.
        """
        scheduled_date = self.corpus_api_client.get_scheduled_date(item.id)
        if scheduled_date is None:
            logging.error(f'scheduled_date is None for {item.id}. We will gracefully degrade performance by continuing'
                          f' to return recommendations with a different `tile_id` value.')

        return f'{self.recommendation_surface_id}/{item.id}/{scheduled_date}'

    async def rank_corpus_items(self, items: List[CorpusItemModel], *args, **kwargs) -> List[CorpusItemModel]:
        """
        :param items: Candidate corpus items
        :return: Ranks items based on Thompson sampling.
        """
        metrics = await self.corpus_engagement_provider.get(
            self.recommendation_surface_id, self.configuration_id, items)

        items = thompson_sampling(
            recs=items,
            metrics=metrics,
            trailing_period=1,  # Currently, Prefect only loads the 1-day trailing window for Firefox New Tab.
            default_alpha_prior=188,  # beta * P99 German NewTab CTR for 2023-03-28 to 2023-04-05 (1.5%)
            default_beta_prior=12500)  # 0.5% of median German NewTab item impressions for 2023-03-28 to 2023-04-05.

        # Sort newest to oldest. Sort is stable, so it will preserve the Thompson sampling within a scheduled date.
        items.sort(key=lambda item: str(self.corpus_api_client.get_scheduled_date(item.id)), reverse=True)

        return items
