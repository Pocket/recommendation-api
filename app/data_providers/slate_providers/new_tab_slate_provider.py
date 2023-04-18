from typing import List

from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.models.corpus_item_model import CorpusItemModel
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

    @property
    def candidate_set_id(self) -> str:
        # TODO: Query the candidate from the GraphQL scheduledSurface.items object. [DIS-452]
        if self.locale == LocaleModel.en_US:
            return '5f0dae93-a5a8-439a-a2e2-5d418c04bc98'
        elif self.locale == LocaleModel.de_DE:
            return '92013292-bc4b-4ee1-815a-0e51c5953ff2'
        else:
            raise ValueError(f'Unexpected locale {self.locale} for {self.provider_name}')

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
        # TODO: When scheduledSurface.items is queried from the Graph, fill in the scheduledDate below. [DIS-452]
        return f'{self.recommendation_surface_id}/{item.id}/<TODO: pull in ScheduledSurfaceItem.scheduledDate>'

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

        return items
