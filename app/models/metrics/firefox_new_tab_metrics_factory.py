import logging
from typing import List, Dict, Optional, Any
from asyncio import gather

import aioboto3

from app import config
from aws_xray_sdk.core import xray_recorder

from app.models.metrics.firefox_new_tab_metrics_model import FirefoxNewTabMetricsModel
from app.models.metrics.metrics_model import MetricsModel


class FirefoxNewTabMetricsFactory():
    _dynamodb_endpoint: str = None
    _dynamodb_table: str = None
    _PRIMARY_KEY_NAME: str = 'ID'
    _FEATURE_GROUP_VERSION: int = 1

    async def get(self, slate_id: str, content_ids: List[str]) -> Dict[str, 'MetricsModel']:
        """
        Get engagement metrics for a Firefox New Tab slate.
        :param slate_id: The last part of the primary key
        :param content_ids: The first part of the primary key
        :return: dictionary of FirefoxNewTabMetricsModel objects keyed on id (i.e. not including the slate_id)
        """
        # Keys are namespaced by the module we are getting data from. First put them in a set to ensure unique keys.
        keys = list({self._make_key(slate_id, i) for i in content_ids})

        metrics = await self._query_metrics(keys)
        # Remove "/<modules>" suffix and remove None values
        # TODO: It might be cleaner if this method just returns List[MetricsBaseModel], and callers create the dict
        # of their choosing.
        metrics = {k.split("/")[0]: self.parse_from_record(v) for k, v in metrics.items() if v is not None}

        if not metrics:
            logging.error(f"No metrics for module {slate_id} with keys={keys}")

        return metrics

    def _get_feature_group_name(self):
        return f'{config.ENV}-firefox-new-tab-engagement-v{self._FEATURE_GROUP_VERSION}'

    def parse_from_record(self, record: Dict[str, Any]) -> FirefoxNewTabMetricsModel:
        """
        Converts a FeatureGroup record Dict to a Pydantic FirefoxNewTabMetricsModel object
        :param record: dictionary containing all required keys for FirefoxNewTabMetricsModel
        :return: Parsed FirefoxNewTabMetricsModel
        """
        # Pydantic model uses lowercase keys, and FeatureGroup uppercase.
        return FirefoxNewTabMetricsModel.parse_obj({k.lower(): v for k, v in record.items()})

    @xray_recorder.capture_async('models.MetricsBaseModel._query_metrics')
    async def _query_metrics(self, metrics_keys: List[str]) -> Dict[str, Optional[Dict]]:
        """
        Queries metrics from the Dynamodb table specified in self._dynamodb_table, using self._primary_key_name.

        :param metrics_keys: Primary keys to match against self._primary_key_name
        :return: Dictionary where all metrics_keys are present as keys, and values are a metrics dictionary or None.
        """
        metrics = {}

        async with aioboto3.client('sagemaker-featurestore-runtime') as featurestore:
            # TODO: Update aioboto3 to v9 to improve performance with featurestore's batch_get_record.
            #       - boto3 1.17.92 introduces BatchGetRecord
            #       - aioboto3 8.3.0 pins aiobotocore[boto3]==1.2.2
            #       - aiobotocore 1.2.2 pins boto3 1.16.52
            promises = [featurestore.get_record(
                FeatureGroupName=self._get_feature_group_name(),
                RecordIdentifierValueAsString=metrics_key,
                FeatureNames=[
                    'ID',
                    'UNLOADED_AT',
                    'URL',
                    'SLATE_ID',
                    'TRAILING_15_MINUTE_OPENS',
                    'TRAILING_15_MINUTE_IMPRESSIONS',
                ]
            ) for metrics_key in metrics_keys]

            responses = await gather(*promises)

            for response in responses:
                features = {feature['FeatureName']: feature['ValueAsString'] for feature in response['Record']}
                pk = features[self._PRIMARY_KEY_NAME]
                metrics[pk] = features

            # TODO: We are somewhat confident that every slate and lineup has at least some metrics available by
            #  now. If this error does not occur in practice, it would be better to change it to an exception.
            # We're logging an error here because the full request context is available.
            # if not responses["Responses"][self._dynamodb_table]:
            #     logging.info(f"DynamoDB returned no metrics for query {request}")

        return {k: metrics.get(k) for k in metrics_keys}

    @xray_recorder.capture_async('models.MetricsBaseModel._query_metrics')
    async def _generate_dummy_data(self, metrics_keys: List[str]) -> Dict[str, Optional[Dict]]:
        """
        TODO: Remove debug code.
        """
        metrics = {}

        async with aioboto3.client('sagemaker-featurestore-runtime') as featurestore:
            promises = [featurestore.put_record(
                FeatureGroupName=self._get_feature_group_name(),
                Record=[
                    {
                        'FeatureName': 'ID',
                        'ValueAsString': metrics_key
                    },
                    {
                        'FeatureName': 'UNLOADED_AT',
                        'ValueAsString': '2022-01-31T16:15:30Z'
                    },
                    {
                        'FeatureName': 'URL',
                        'ValueAsString': f'https://example.com/{metrics_key}',
                    },
                    {
                        'FeatureName': 'SLATE_ID',
                        'ValueAsString': metrics_key.split('/')[1],
                    },
                    {
                        'FeatureName': 'TRAILING_15_MINUTE_OPENS',
                        'ValueAsString': metrics_key.split('/')[0],
                    },
                    {
                        'FeatureName': 'TRAILING_15_MINUTE_IMPRESSIONS',
                        'ValueAsString': str(100 + int(metrics_key.split('/')[0])),
                    },
                ],
            ) for metrics_key in metrics_keys]

            responses = await gather(*promises)
            print(responses)

    def _make_key(self, module: str, item_id: str) -> str:
        """
        Generate the primary key for the metrics database

        :param module: Prefix for which to get metrics
        :param item_id: Item for which to get metrics
        :return: DynamoDB primary key value
        """
        return "%s/%s" % (item_id, module)
