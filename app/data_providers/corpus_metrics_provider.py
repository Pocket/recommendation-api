import logging
from asyncio import gather
from datetime import datetime
from typing import List, Dict

import aioboto3
from aws_xray_sdk.core import xray_recorder

from app import config
from app.data_providers.util.feature_store import FeatureStoreRecordType, BATCH_GET_RECORD_MAX_ITEMS
from app.data_providers.util.iteration import chunks
from app.models.metrics.corpus_metrics_model import CorpusMetricsModel, CorpusMetricsSegmentModel
from app.models.metrics.firefox_new_tab_metrics_model import FirefoxNewTabMetricsModel
from app.models.metrics.metrics_model import MetricsModel
from app.models.surface import Surface


class CorpusMetricsProvider():
    _FEATURE_GROUP_VERSION: int = 1
    _FEATURE_NAMES: List[str] = [
        'UPDATED_AT',
        'SURFACE',
        'CORPUS_SLATE_CONFIG_ID'
        'CORPUS_ITEM_ID'
        'TRAILING_1_DAY_OPENS',
        'TRAILING_1_DAY_IMPRESSIONS',
        'TRAILING_7_DAY_OPENS',
        'TRAILING_7_DAY_IMPRESSIONS',
        'TRAILING_14_DAY_OPENS',
        'TRAILING_14_DAY_IMPRESSIONS',
        'TRAILING_28_DAY_OPENS',
        'TRAILING_28_DAY_IMPRESSIONS',
    ]

    def __init__(self, aioboto3_session: aioboto3.session.Session = None):
        self.aioboto3_session = aioboto3_session if aioboto3_session else aioboto3.Session()

    async def fetch(self, segments: List[CorpusMetricsSegmentModel]) -> List[CorpusMetricsModel]:
        """
        Get engagement metrics for Corpus Recommendations.
        :param segments: Segments of metrics to query.
        :return: List of metric models, not necessarily in the same order as the input.
        """
        keys = map(self._format_key, segments)

        metrics = await self._query_metrics(keys)

        # Convert from dict to Pydantic model
        parsed_metrics = [self._parse_from_record(m) for m in metrics]
        parsed_metrics_by_id = {m.id: m for m in parsed_metrics}

        return parsed_metrics_by_id

    @classmethod
    def get_feature_group_name(cls):
        return f'{config.ENV}-corpus-engagement-v{cls._FEATURE_GROUP_VERSION}'

    @staticmethod
    def _format_key(segment: CorpusMetricsSegmentModel) -> str:
        """
        Formats the Feature Group key that identifies a given segment
        :param segment:
        :return:
        """
        return '/'.join([segment.surface, segment.corpus_slate_config_id, segment.corpus_item_id])

    def _parse_from_record(self, record: FeatureStoreRecordType) -> CorpusMetricsModel:
        """
        Converts a FeatureGroup record to a Pydantic CorpusMetricsModel object
        :param record: dictionary containing all required keys for FirefoxNewTabMetricsModel
        :return: Parsed CorpusMetricsModel
        """
        # Pydantic model uses lowercase keys.
        return CorpusMetricsModel(
            segment=CorpusMetricsSegmentModel(
                surface=record['SURFACE'],
                corpus_slate_config_id=record['CORPUS_SLATE_CONFIG_ID'],
                corpus_item_id=record['CORPUS_ITEM_ID'],
            ),
            updated_at=datetime.fromisoformat(record['UPDATED_AT']),
            trailing_1_day_opens=record['TRAILING_1_DAY_OPENS'],
            trailing_1_day_impressions=record['TRAILING_1_DAY_IMPRESSIONS'],
            trailing_7_day_opens=record['TRAILING_7_DAY_OPENS'],
            trailing_7_day_impressions=record['TRAILING_7_DAY_IMPRESSIONS'],
            trailing_14_day_opens=record['TRAILING_14_DAY_OPENS'],
            trailing_14_day_impressions=record['TRAILING_14_DAY_IMPRESSIONS'],
            trailing_28_day_opens=record['TRAILING_28_DAY_OPENS'],
            trailing_28_day_impressions=record['TRAILING_28_DAY_IMPRESSIONS'],
        )

    @xray_recorder.capture_async('CorpusMetricsProvider._query_metrics')
    async def _query_metrics(self, metrics_keys: List[str]) -> List[FeatureStoreRecordType]:
        """
        Queries metrics from the Feature Group.

        :param metrics_keys: Feature record IDs to query
        :return: List with all metrics that were successfully queried from the Feature Store.
                 If metrics are missing from the output that means the feature group did not find a match, probably
                 because the recommendation is too recent.
        """
        records = []

        async with self.aioboto3_session.client('sagemaker-featurestore-runtime') as featurestore:
            promises = [featurestore.batch_get_record(
                Identifiers=[
                    {
                        'FeatureGroupName': self.get_feature_group_name(),
                        'RecordIdentifiersValueAsString': metrics_key_chunk,
                        'FeatureNames': self._FEATURE_NAMES
                    },
                ]
            ) for metrics_key_chunk in chunks(metrics_keys, BATCH_GET_RECORD_MAX_ITEMS)]

            responses = await gather(*promises)

            for response in responses:
                # If FeatureStore can't find an ID, it returns a 200 response without a record.
                record = response.get('Record')
                if record:
                    records.append(record)

        return records
