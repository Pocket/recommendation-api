from abc import ABC # ABC stands for Abstract Base Class
import logging
from typing import List, Dict, Optional

import aioboto3
from aiocache import decorators
from aws_xray_sdk.core import xray_recorder
from app.models.metrics.metrics_model import MetricsModel

import app.cache
import app.config

# batch get has a 100 item limit
# https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html
_DYNAMODB_BATCH_GET_ITEM_LIMIT = 100


def _chunks(index, n=_DYNAMODB_BATCH_GET_ITEM_LIMIT):
    """Yield successive n-sized chunks from index."""
    for i in range(0, len(index), n):
        yield index[i: i + n]


class AbstractMetricsFactory(ABC):
    _dynamodb_endpoint: str = app.config.dynamodb['endpoint_url']
    _dynamodb_table: str = None
    _primary_key_name: str = None

    async def get(self, module_id: str, ids: List[str]) -> Dict[str, 'MetricsModel']:
        """
        Get engagement metrics for recommendations or slates.
        - recommendations: The module is a slate that contains the recommendation.
                           The primary key is <slate id>/<item id>.
        - slates: The module is the slate lineup that contains the slate.
                  The primary key is <lineup id>/<slate id>.

        :param module_id: The first part of the primary key
        :param ids: Used in the second part of the primary key.
        :return: dictionary of ClickdataModel objects keyed on item (i.e. not including the prefix)
        """
        # Keys are namespaced by the module we are getting data from
        keys = {self._make_key(module_id, i) for i in ids}

        # Always get the default key, it is used for items that don't have any metrics
        keys.add(self._make_key(module_id, "default"))
        keys = list(keys)

        metrics = await self._query_cached_metrics(keys)
        # Remove "/<modules>" suffix and remove None values
        # TODO: It might be cleaner if this method just returns List[MetricsBaseModel], and callers create the dict
        # of their choosing.
        metrics = {k.split("/")[0]: self.parse_from_record(v) for k, v in metrics.items() if v is not None}

        if not metrics:
            logging.error(f"No metrics for module {module_id} with keys={keys}")

        return metrics

    def parse_from_record(self, value: Dict):
        """
        Similar to Pydantic's parse_obj function, but sets the id field using the primary key.
        :param value: dictionary containing all required keys for MetricsBaseModel
        :return: Parsed MetricsBaseModel
        """
        return MetricsModel.parse_obj({**value, 'id': value[self._primary_key_name]})

    @xray_recorder.capture_async('models.metrics.MetricsBaseModel._query_cached_metrics')
    async def _query_cached_metrics(self, metrics_keys: List) -> Dict[str, Optional[Dict]]:
        multi_cache_wrapper = decorators.multi_cached(
            keys_from_attr="metrics_keys",
            ttl=app.config.elasticache['metrics_ttl'],
            alias=app.cache.metrics_alias)

        multi_cache = multi_cache_wrapper(self._query_metrics)

        # multi_cache will get metrics from cache when available, and call _query_metrics with all missing keys.
        results = await multi_cache(metrics_keys=metrics_keys)

        # Map app.cache's NoneValue to None. aiocache treats None as a cache miss, so we need a special token for this.
        return {k: None if v == app.cache.NoneValue else v for k, v in results.items()}

    @xray_recorder.capture_async('models.MetricsBaseModel._query_metrics')
    async def _query_metrics(self, metrics_keys: List):
        metrics = {}

        async with aioboto3.resource('dynamodb', endpoint_url=self._dynamodb_endpoint) as dynamodb:
            for keychunk in _chunks(metrics_keys):
                request = {
                    self._dynamodb_table: {
                        "Keys": [{self._primary_key_name: c} for c in keychunk]
                    }
                }
                responses = await dynamodb.batch_get_item(RequestItems=request)

                # TODO: Write a unit test when there are more than 100  rows. It seems this will fail because it's only
                #
                for row in responses["Responses"][self._dynamodb_table]:
                    pk = row[self._primary_key_name]
                    metrics[pk] = row

                if not responses["Responses"][self._dynamodb_table]:
                    logging.error(f"DynamoDB returned no metrics for query {request}")

        return {k: metrics.get(k) for k in metrics_keys}

    def _make_key(self, module: str, item_id: str) -> str:
        """
        Generate the primary key for the metrics database

        :param module: Prefix for which to get metrics
        :param item_id: Item for which to get metrics, or "default" for module prior
        :return: DynamoDB primary key value
        """
        return "%s/%s" % (item_id, module)
