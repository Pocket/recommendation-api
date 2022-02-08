import logging
from typing import List, Dict, Optional, Any
from asyncio import gather
import uuid

import aioboto3

from app import config
from aws_xray_sdk.core import xray_recorder

from app.models.metrics.firefox_new_tab_metrics_model import FirefoxNewTabMetricsModel
from app.models.metrics.metrics_model import MetricsModel


# Unfortunately boto3 doesn't use types for feature store records at the moment, so we define one ourselves.
# For example records see tests/assets/json/firefox_new_tab_engagement.json
FeatureStoreRecordType = List[Dict[str, str]]


class FirefoxNewTabMetricsFactory():
    _dynamodb_endpoint: str = None
    _dynamodb_table: str = None
    _PRIMARY_KEY_NAME: str = 'ID'
    _FEATURE_GROUP_VERSION: int = 2
    _FEATURE_NAMES: List[str] = [
        'ID',
        'UNLOADED_AT',
        'URL',
        'SLATE_ID',
        'TRAILING_15_MINUTE_OPENS',
        'TRAILING_15_MINUTE_IMPRESSIONS',
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
            logging.error(f"No Firefox New Tab metrics for recommendation_ids={recommendation_ids}")

        # Convert from dict to Pydantic model and key on id.
        parsed_metrics = [self.parse_from_record(m) for m in metrics]
        parsed_metrics_by_id = {m.id: m for m in parsed_metrics}

        return parsed_metrics_by_id

    @classmethod
    def get_feature_group_name(cls):
        return f'{config.ENV}-firefox-new-tab-engagement-v{cls._FEATURE_GROUP_VERSION}'

    def parse_from_record(self, record: FeatureStoreRecordType) -> FirefoxNewTabMetricsModel:
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

            # We're logging an error here because the full request context is available.
            # if not responses["Responses"][self._dynamodb_table]:
            #     logging.info(f"DynamoDB returned no metrics for query {request}")

        return metrics

    async def _generate_dummy_data(self, metrics_keys: List[str]):
        """
        TODO: Remove debug code.
        """
        metrics = {}
        import uuid

        async with aioboto3.client('sagemaker-featurestore-runtime') as featurestore:
            promises = [featurestore.put_record(
                FeatureGroupName=self.get_feature_group_name(),
                Record=[
                    {
                        'FeatureName': 'ID',
                        'ValueAsString': metrics_key
                    },
                    {
                        'FeatureName': 'UNLOADED_AT',
                        'ValueAsString': '2022-02-07T16:15:30Z'
                    },
                    {
                        'FeatureName': 'SCHEDULED_SURFACE_ITEM_ID',
                        'ValueAsString': str(uuid.uuid4()),
                    },
                    {
                        'FeatureName': 'SLATE_EXPERIMENT_ID',
                        'ValueAsString': '13055e0',
                    },
                    {
                        'FeatureName': 'URL',
                        'ValueAsString': f'https://example.com/{metrics_key}',
                    },
                    {
                        'FeatureName': 'SLATE_ID',
                        'ValueAsString': 'f99178fb-6bd0-4fa1-8109-cda181b697f6',
                    },
                    {
                        'FeatureName': 'TRAILING_15_MINUTE_OPENS',
                        'ValueAsString': str(100 * index),
                    },
                    {
                        'FeatureName': 'TRAILING_15_MINUTE_IMPRESSIONS',
                        'ValueAsString': str(100000),
                    },
                ],
            ) for index, metrics_key in enumerate(metrics_keys)]

            responses = await gather(*promises)
            print(responses)
