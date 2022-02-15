import logging
from typing import List, Dict
from asyncio import gather

import aioboto3

from app import config
from aws_xray_sdk.core import xray_recorder

from app.models.metrics.firefox_new_tab_metrics_model import FirefoxNewTabMetricsModel
from app.models.metrics.metrics_model import MetricsModel


# Unfortunately boto3 doesn't use types for feature store records at the moment, so we define one ourselves.
# For example records see tests/assets/json/firefox_new_tab_engagement.json
FeatureStoreRecordType = List[Dict[str, str]]


class FirefoxNewTabMetricsFactory():
    _FEATURE_GROUP_VERSION: int = 3
    _FEATURE_NAMES: List[str] = [
        'ID',
        'UNLOADED_AT',
        'SCHEDULED_SURFACE_ITEM_ID',
        'SLATE_EXPERIMENT_ID',
        'URL',
        'SLATE_ID',
        'TRAILING_1_DAY_OPENS',
        'TRAILING_1_DAY_IMPRESSIONS',
    ]

    async def get(self, recommendation_ids: List[str]) -> Dict[str, 'FirefoxNewTabMetricsModel']:
        """
        Get engagement metrics for a Firefox New Tab slate experiment.
        TODO: This function should simply accept 'recommendation_ids', and we should generate these ids elsewhere.
        :param recommendation_ids: GUIDs uniquely represent a scheduled run of a corpus item in a slate experiment.
        :return: dictionary of FirefoxNewTabMetricsModel objects keyed on recommendation id
        """
        # Keys are namespaced by the slate that we are getting data from. First put them in a set to ensure unique keys.
        metrics = await self._query_metrics(recommendation_ids)
        if not metrics:
            logging.warning(f"No Firefox New Tab metrics for recommendation_ids={recommendation_ids}")

        # Convert from dict to Pydantic model and key on id.
        parsed_metrics = [self._parse_from_record(m) for m in metrics]
        parsed_metrics_by_id = {m.id: m for m in parsed_metrics}

        return parsed_metrics_by_id

    @classmethod
    def get_feature_group_name(cls):
        return f'{config.ENV}-firefox-new-tab-engagement-v{cls._FEATURE_GROUP_VERSION}'

    def _parse_from_record(self, record: FeatureStoreRecordType) -> FirefoxNewTabMetricsModel:
        """
        Converts a FeatureGroup record to a Pydantic FirefoxNewTabMetricsModel object
        :param record: dictionary containing all required keys for FirefoxNewTabMetricsModel
        :return: Parsed FirefoxNewTabMetricsModel
        """
        # Pydantic model uses lowercase keys.
        features = {feature['FeatureName'].lower(): feature['ValueAsString'] for feature in record}
        return FirefoxNewTabMetricsModel.parse_obj(features)

    @xray_recorder.capture_async('models.MetricsBaseModel._query_metrics')
    async def _query_metrics(self, metrics_keys: List[str]) -> List[FeatureStoreRecordType]:
        """
        Queries metrics from the Feature Group.

        :param metrics_keys: Feature record IDs to query
        :return: List with all metrics that were successfully queried from the Feature Store.
                 If metrics are missing from the output that means the feature group did not find a match, probably
                 because the recommendation is too recent.
        """
        metrics = []

        async with aioboto3.client('sagemaker-featurestore-runtime') as featurestore:
            # TODO: Update aioboto3 to v9 to improve performance with featurestore's batch_get_record.
            #       - boto3 1.17.92 introduces BatchGetRecord
            #       - aioboto3 8.3.0 pins aiobotocore[boto3]==1.2.2
            #       - aiobotocore 1.2.2 pins boto3 1.16.52
            promises = [featurestore.get_record(
                FeatureGroupName=self.get_feature_group_name(),
                RecordIdentifierValueAsString=metrics_key,
                FeatureNames=self._FEATURE_NAMES
            ) for metrics_key in metrics_keys]

            responses = await gather(*promises)

            for response in responses:
                # If FeatureStore can't find an ID, it returns a 200 response without a record.
                record = response.get('Record')
                if record:
                    metrics.append(record)

        return metrics
