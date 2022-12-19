from typing import List, Dict

from app import config
from app.data_providers.feature_group.feature_group_client import FeatureGroupClient
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.metrics.corpus_item_engagement_model import CorpusItemEngagementModel


class CorpusEngagementProvider:

    def __init__(self, feature_group_client: FeatureGroupClient):
        self.feature_group_client = feature_group_client

    async def get(
            self,
            recommendation_surface_id: RecommendationSurfaceId,
            corpus_slate_configuration_id: str,
            items: List[CorpusItemModel],
    ) -> Dict[str, CorpusItemEngagementModel]:
        """
        :param recommendation_surface_id: Identifies where (e.g. 'HOME') on which recommendations are surfaced.
        :param corpus_slate_configuration_id: Identifies the slate in which recommendations are shown.
        :param items: A list of Corpus Item ids.
        :return: Corpus engagement models keyed on corpus item id.
        """
        records = await self.feature_group_client.batch_get_records(
            feature_group_name=self.feature_group_name,
            feature_names=self.feature_names,
            ids=[f'{recommendation_surface_id.value}/{corpus_slate_configuration_id}/{item.id}' for item in items]
        )

        engagement_models = [self.parse_record(r) for r in records]
        return {m.corpus_item_id: m for m in engagement_models}

    @property
    def feature_group_name(self):
        return f'{config.ENV}-corpus-engagement-v1'

    @property
    def feature_names(self):
        return [
            'UPDATED_AT',
            'RECOMMENDATION_SURFACE_ID',
            'CORPUS_SLATE_CONFIGURATION_ID',
            'CORPUS_ITEM_ID',
            'TRAILING_1_DAY_OPENS',
            'TRAILING_1_DAY_IMPRESSIONS',
            'TRAILING_7_DAY_OPENS',
            'TRAILING_7_DAY_IMPRESSIONS',
            'TRAILING_14_DAY_OPENS',
            'TRAILING_14_DAY_IMPRESSIONS',
            'TRAILING_21_DAY_OPENS',
            'TRAILING_21_DAY_IMPRESSIONS',
            'TRAILING_28_DAY_OPENS',
            'TRAILING_28_DAY_IMPRESSIONS',
        ]

    @staticmethod
    def parse_record(record: Dict[str, str]) -> CorpusItemEngagementModel:
        lowercase_record = {k.lower(): v for k, v in record.items()}
        return CorpusItemEngagementModel.parse_obj(lowercase_record)
