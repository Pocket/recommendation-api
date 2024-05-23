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
from app.rankers.algorithms import thompson_sampling, spread_publishers, boost_syndicated

# Maximum tileId that Firefox can support. Firefox uses Javascript to store this value. The max value of a Javascript
# number can be found using `Number.MAX_SAFE_INTEGER`. which is 2^53 - 1 because it uses a 64-bit IEEE 754 float.
MAX_TILE_ID = 1 << 53 - 1
# Generate tile_ids well out of the range of the MySQL-based system, which has a max tile_id of 99,999 as of 2023-03-13.
# This is done to make it easy for engineers/analysts to see which system generated the identifier.
MIN_TILE_ID = 100 * 100000
# How far recs from the same publisher should be spread apart.
PUBLISHER_SPREAD_DISTANCE = 6
# In a weighted average, how much to weigh the metrics from the requested region.
# CA has about 9x fewer impressions than the total for NEW_TAB_EN_US. The weight
# of 0.95 was chosen to boost CA enough to let them significantly impact the
# final ranking, while still giving some influence to international engagement.
# For the purpose of experimentation a constant weight probably suffices. If the
# experiment is success, we could derive this weight from actual impressions.
REGION_METRICS_WEIGHT = 0.95


class NewTabSlateProvider(SlateProvider):

    def __init__(
            self,
            corpus_api_client: CorpusApiClient,
            corpus_engagement_provider: CorpusEngagementProvider,
            recommendation_surface_id: RecommendationSurfaceId):
        """
        The only difference between this constructor and the parent one is that it explicitly requires a CorpusApiClient
        :param corpus_api_client: Client that gets corpus from Curated Corpus API.
        """
        super().__init__(
            corpus_fetchable=corpus_api_client,
            corpus_engagement_provider=corpus_engagement_provider,
            recommendation_surface_id=recommendation_surface_id)

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
                tile_id=integer_hash(self._get_tile_id_key(item), start=MIN_TILE_ID, stop=MAX_TILE_ID + 1),
                scheduled_surface_item_id=self.corpus_api_client.get_scheduled_surface_item_id(item.id),
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
        :return: Ranks items by recency, publisher spread, and engagement, as defined in the New Tab slate spec:
        https://getpocket.atlassian.net/wiki/spaces/PE/pages/2927100008/Fx+NewTab+Slate+spec+for+New+Markets
        """
        metrics = await self.corpus_engagement_provider.get(
            self.recommendation_surface_id, self.configuration_id, items)

        if kwargs.get('enable_ranking_by_region') and kwargs.get('region'):
            region_metrics = await self.corpus_engagement_provider.get(
                self.recommendation_surface_id, self.configuration_id, items, kwargs['region'])

            for item_id in metrics:
                if item_id in region_metrics:
                    # Compute weighted average of global and region metrics for 1 day opens and impressions.
                    metrics[item_id].trailing_1_day_opens = (
                        (1 - REGION_METRICS_WEIGHT) * metrics[item_id].trailing_1_day_opens +
                        REGION_METRICS_WEIGHT * region_metrics[item_id].trailing_1_day_opens
                    )
                    metrics[item_id].trailing_1_day_impressions = (
                        (1 - REGION_METRICS_WEIGHT) * metrics[item_id].trailing_1_day_impressions +
                        REGION_METRICS_WEIGHT * region_metrics[item_id].trailing_1_day_impressions
                    )

        # 3. Tertiary sort order is Thompson sampling.
        items = thompson_sampling(
            recs=items,
            metrics=metrics,
            trailing_period=1,  # Currently, Prefect only loads the 1-day trailing window for Firefox New Tab.
            default_alpha_prior=188,  # beta * P99 German NewTab CTR for 2023-03-28 to 2023-04-05 (1.5%)
            default_beta_prior=12500)  # 0.5% of median German NewTab item impressions for 2023-03-28 to 2023-04-05.

        # 2. Secondary sort order is recency.
        items.sort(key=lambda item: str(self.corpus_api_client.get_scheduled_date(item.id)), reverse=True)

        # 1. Primary sort order is publisher diversity. Sort is stable, so it will preserve recency order, except
        #    for duplicate publishers.
        items = spread_publishers(items, spread_distance=PUBLISHER_SPREAD_DISTANCE)

        # Final step is to boost a syndicated article (if one exists).
        items = boost_syndicated(items, metrics)

        return items
