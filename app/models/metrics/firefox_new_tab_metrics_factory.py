import logging
from typing import List, Dict, Optional, Any
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
    _dynamodb_endpoint: str = None
    _dynamodb_table: str = None
    _PRIMARY_KEY_NAME: str = 'ID'
    _FEATURE_GROUP_VERSION: int = 1
    _FEATURE_NAMES: List[str] = [
        'ID',
        'UNLOADED_AT',
        'URL',
        'SLATE_ID',
        'TRAILING_15_MINUTE_OPENS',
        'TRAILING_15_MINUTE_IMPRESSIONS',
    ]

    async def get(self, slate_id: str, content_ids: List[str]) -> Dict[str, 'FirefoxNewTabMetricsModel']:
        """
        Get engagement metrics for a Firefox New Tab slate.
        :param slate_id: The slate ('feed') for which to get metrics
        :param content_ids: The content ids for which to get metrics
        :return: dictionary of FirefoxNewTabMetricsModel objects keyed on content id (i.e. not including the slate_id)
        """
        # Keys are namespaced by the slate that we are getting data from. First put them in a set to ensure unique keys.
        keys = list({self._make_key(slate_id, i) for i in content_ids})

        metrics = await self._query_metrics(keys)
        if not metrics:
            logging.error(f"No Firefox New Tab metrics for slate {slate_id} with keys={keys}")

        # Convert from dict to Pydantic model and key on id.
        parsed_metrics = [self.parse_from_record(m) for m in metrics]
        # TODO: Add content_id to feature group so we can access this directly.
        parsed_metrics_by_id = {self._get_content_id_from_id(m.id): m for m in parsed_metrics}

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

    def _make_key(self, slate_id: str, content_id: str) -> str:
        """
        Generate the primary key for the metrics database

        :param slate_id: Slate for which to get metrics
        :param content_id: Content for which to get metrics
        :return: DynamoDB primary key value
        """
        return "%s/%s" % (content_id, slate_id)

    def _get_content_id_from_id(self, compound_id: str) -> str:
        """
        Extract the content id from the compounded id

        :param compound_id: Id formatted as content_id/slate_id
        :return: Content di
        """
        return compound_id.split('/')[0]
