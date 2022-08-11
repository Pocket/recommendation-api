from asyncio import gather
from datetime import datetime
from typing import List, Dict

import aioboto3
from aws_xray_sdk.core import xray_recorder

from app import config
from app.data_providers.util.feature_store import FeatureStoreRecordType, BATCH_GET_RECORD_MAX_ITEMS, \
    feature_store_record_to_dict
from app.data_providers.util.iteration import chunks
from app.models.metrics.corpus_metrics_model import CorpusMetricsModel, CorpusMetricsSegmentModel
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

    async def fetch_by_corpus_item_ids(
        self,
        surface: Surface,
        corpus_slate_config_id: str,
        corpus_item_ids: List[str],
    ) -> Dict[str, CorpusMetricsModel]:
        """
        Get corpus item engagement metrics for a given surface and slate config.
        :param surface:
        :param corpus_slate_config_id:
        :param corpus_item_ids:
        :return: The metrics are returned keyed on corpus_item_id. If no metrics are available keys will be missing.
        """
        metrics = await self.fetch([CorpusMetricsSegmentModel(
            surface=surface,
            corpus_slate_config_id=corpus_slate_config_id,
            corpus_item_id=corpus_item_id,
        ) for corpus_item_id in corpus_item_ids])

        return {metric.segment.corpus_item_id: metric for metric in metrics}

    async def fetch(self, segments: List[CorpusMetricsSegmentModel]) -> List[CorpusMetricsModel]:
        """
        Get engagement metrics for Corpus Recommendations.
        :param segments: Segments of metrics to query.
        :return: List of metric models, not necessarily in the same order as the input.
        """
        keys = list(map(self._format_key, segments))

        return await self._query_metrics(keys)

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

    @staticmethod
    def _parse_from_record(record: FeatureStoreRecordType) -> CorpusMetricsModel:
        """
        Converts a FeatureGroup record to a Pydantic CorpusMetricsModel object
        :param record: dictionary containing all required keys for FirefoxNewTabMetricsModel
        :return: Parsed CorpusMetricsModel
        """
        record_dict = feature_store_record_to_dict(record, lowercase_names=True)
        segment_dict = {k: record_dict[k] for k in CorpusMetricsSegmentModel.__fields__.keys()}
        metrics_model_dict = dict({'segment': segment_dict}, **record_dict)

        return CorpusMetricsModel.parse_obj(metrics_model_dict)

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
