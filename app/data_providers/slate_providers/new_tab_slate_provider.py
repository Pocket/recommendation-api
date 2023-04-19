import itertools
from datetime import timedelta, datetime
from typing import List, Dict
from uuid import uuid5, UUID

import pytz

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.data_providers.translation import TranslationProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel
from app.data_providers.util import integer_hash
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.rankers.algorithms import thompson_sampling

# Maximum tileId that Firefox can support. Firefox uses Javascript to store this value. The max value of a Javascript
# number can be found using `Number.MAX_SAFE_INTEGER`. which is 2^53 - 1 because it uses a 64-bit IEEE 754 float.
MAX_TILE_ID = 1 << 53 - 1
# Generate tile_ids well out of the range of the MySQL-based system, which has a max tile_id of 99,999 as of 2023-03-13.
# This is done to make it easy for engineers/analysts to see which system generated the identifier.
MIN_TILE_ID = 100 * 100000


class NewTabSlateProvider(SlateProvider):
    _corpus_item_scheduled_date: Dict[str, str] = {}  # Maps CorpusItem.id to scheduledDate

    def __init__(
            self,
            pocket_graph_client_session: PocketGraphClientSession,
            corpus_feature_group_client: CorpusFeatureGroupClient,
            corpus_engagement_provider: CorpusEngagementProvider,
            recommendation_surface_id: RecommendationSurfaceId,
            locale: LocaleModel,
            translation_provider: TranslationProvider):

        super().__init__(
            corpus_feature_group_client=corpus_feature_group_client,
            corpus_engagement_provider=corpus_engagement_provider,
            recommendation_surface_id=recommendation_surface_id,
            locale=locale,
            translation_provider=translation_provider)

        self.pocket_graph_client_session = pocket_graph_client_session

    @property
    def candidate_set_id(self) -> str:
        """
        :return: UUID candidate set identifier, which identifies the corpus items that serve as the input for this slate
        """
        # This class gets candidates from GraphQL, which identifies candidates using a human-readable string identifier
        # `recommendation_surface_id` (e.g. 'NEW_TAB_EN_US'). This identifier is turned into a UUID, because that's what
        # SlateProvider expects. The UUID below is arbitrary. 'NEW_TAB_EN_US' uniquely describes the candidate item set.
        return str(uuid5(UUID('b6396f0d-ea1b-40ba-9192-83accda9c106'), self.recommendation_surface_id.value))

    async def get_candidate_corpus_items(self) -> List[CorpusItemModel]:
        """
        :return: The CorpusItems from the candidate set, without any rankers or filters applied.
        """
        """
        Get all Unleash assignments for the given user/session.
        :param user:
        :return:
        """
        query = """
            query ScheduledSurface($scheduledSurfaceId: ID!, $date_today: Date!, $date_yesterday: Date!) {
              scheduledSurface(id: $scheduledSurfaceId) {
                items_today:     items(date: $date_today)     { corpusItem { id topic } scheduledDate }
                items_yesterday: items(date: $date_yesterday) { corpusItem { id topic } scheduledDate }
              }
            }
        """

        # The date is supposed to progress at midnight EST.
        today = datetime.now(tz=pytz.timezone('America/New_York'))
        yesterday = today - timedelta(days=1)

        body = {
            'query': query,
            'variables': {
              'scheduledSurfaceId': self.recommendation_surface_id.value,
              'date_today': today.strftime('%Y-%m-%d'),
              'date_yesterday': yesterday.strftime('%Y-%m-%d'),
            }
        }

        async with self.pocket_graph_client_session.post(url='/', json=body, raise_for_status=True) as resp:
            response_json = await resp.json()
            scheduled_surface = response_json['data']['scheduledSurface']
            all_items = itertools.chain(scheduled_surface['items_today'], scheduled_surface['items_yesterday'])

            corpus_items = []
            for item in all_items:
                corpus_item: CorpusItemModel = CorpusItemModel.parse_obj(item['corpusItem'])
                corpus_items.append(corpus_item)
                self._corpus_item_scheduled_date[corpus_item.id] = item['scheduledDate']

        return corpus_items

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
        return f'{self.recommendation_surface_id}/{item.id}/{self._corpus_item_scheduled_date[item.id]}'

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

        # Sort newest to oldest. Python is stable, so it will preserve the Thompson sampling within a scheduled date.
        items.sort(key=lambda item: self._corpus_item_scheduled_date.get(item.id), reverse=True)

        return items
