import logging
from typing import List, Dict

import botocore.exceptions
from aiocache import multi_cached

from app import config
from app.data_providers.feature_group.feature_group_client import FeatureGroupClient
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.metrics.corpus_item_engagement_model import CorpusItemEngagementModel


class CorpusEngagementProvider:

    class MissingRecord:
        pass

    def __init__(self, feature_group_client: FeatureGroupClient):
        self.feature_group_client = feature_group_client

    async def get(
            self,
            recommendation_surface_id: RecommendationSurfaceId,
            corpus_slate_configuration_id: str,
            items: List[CorpusItemModel],
    ) -> Dict[str, CorpusItemEngagementModel]:
        """
        :param recommendation_surface_id: Identifies where recommendations are surfaced. Currently only 'HOME'.
        :param corpus_slate_configuration_id: Identifies the slate configuration, e.g. a UUID for the 'For You' slate.
        :param items: A list of Corpus Item ids.
        :return: Corpus engagement models keyed on corpus item id.
        """
        engagement = await self._get_engagement_by_keys(
            [f'{recommendation_surface_id.value}/{corpus_slate_configuration_id}/{item.id}' for item in items])

        return {m.corpus_item_id: m for m in engagement.values() if m is not self.MissingRecord}

    @multi_cached(ttl=900, keys_from_attr='keys')
    async def _get_engagement_by_keys(self, keys: List[str]) -> Dict[str, CorpusItemEngagementModel]:
        """
        :param keys: Engagement is keyed on `recommendation_surface_id/corpus_slate_configuration_id/corpus_item_id`.
                     The input and output are keyed the same such that @multi_cached can cache this function.
        :return: Dict where the keys are equal to the input parameter and the values are engagement models.
                 Returns MissingRecord if key is not found.
        """
        try:
            records = await self.feature_group_client.batch_get_records(
                feature_group_name=self.feature_group_name,
                feature_names=self.feature_names,
                ids=keys
            )

            engagement_models = [self.parse_record(r) for r in records]
            models_by_key = {m.key: m for m in engagement_models}
        except Exception as e:
            # Engagement data powers Thompson sampling on Firefox New Tab and Home. Thompson sampling is an enhancement,
            # and missing engagement data should not prevent us from delivering recommendations, especially to Firefox.
            logging.error(f'Getting engagement data from {self.feature_group_name} caused an unexpected exception. '
                          f'Recommendations can still be served, but without Thompson sampling. {e}')
            # Setting models_by_key to an empty dict causes the input keys to be cached as `MissingRecord`. This
            # prevents cascading errors from happen, by not hitting the Feature Store again until the cache expires.
            models_by_key = {}

        # Missing records are cached to prevent a request going to the feature group on every function call.
        return {key: models_by_key.get(key, self.MissingRecord) for key in keys}

    @property
    def feature_group_name(self):
        return f'{config.ENV}-corpus-engagement-v1'

    @property
    def feature_names(self):
        return [
            'KEY',
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
