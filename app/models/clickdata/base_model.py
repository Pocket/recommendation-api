from typing import List, Dict

import aioboto3
from aiocache import decorators
from aws_xray_sdk.core import xray_recorder
from pydantic import BaseModel

import app.cache
import app.config

# batch get has a 100 item limit
# https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html
_DYNAMODB_BATCH_GET_ITEM_LIMIT = 100


def _chunks(index, n=_DYNAMODB_BATCH_GET_ITEM_LIMIT):
    """Yield successive n-sized chunks from index."""
    for i in range(0, len(index), n):
        yield index[i: i + n]


class ClickdataBaseModel(BaseModel):
    mod_item: str = None
    clicks: float = None
    impressions: float = None
    # TODO: Add 1, 14, 28 day metrics.
    # TODO: Change "training" to "trailing" once DynamoDB is updated.
    training_7_day_opens: float = None
    training_7_day_impressions: float = None
    created_at: int = None
    expires_at: int = None

    _dynamodb_endpoint: str = app.config.dynamodb['endpoint_url']
    _dynamodb_table: str = None
    _primary_key_name: str = None
    _opens_key: str = 'training_7_day_opens'
    _impressions_key: str = 'training_7_day_impressions'

    async def get(self, module_id: str, ids: List[str]) -> Dict[str, 'ClickdataBaseModel']:
        """
        Get clickdata for recommendations or slates that.
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

        # Always get the default key, it is used for items that don't have any clickstream data
        keys.add(self._make_key(module_id, "default"))
        keys = list(keys)

        clickdata = await self._query_cached_clickdata(keys)
        # Remove "/<modules>" suffix and remove None values
        clickdata = {k.split("/")[0]: ClickdataBaseModel.parse_obj(v) for k, v in clickdata.items() if v is not None}

        if not clickdata:
            raise ValueError(f"No results from DynamoDB: {module_id}")

        return clickdata

    @xray_recorder.capture_async('models.clickdata._query_cached_clickdata')
    async def _query_cached_clickdata(self, clickdata_keys: List) -> Dict[str, 'ClickdataBaseModel']:
        multi_cache_wrapper = decorators.multi_cached(
            "clickdata_keys",
            ttl=1, #app.config.elasticache['clickdata_ttl'],
            alias=app.cache.clickdata_alias)

        multi_cache = multi_cache_wrapper(self._query_clickdata)

        # multi_cache will get clickdata from cache when available, and call _query_clickdata with all missing keys.
        results = await multi_cache(clickdata_keys=clickdata_keys)

        # Map app.cache's NoneValue to None. aiocache treats None as a cache miss, so we need a special token for this.
        return {k: None if v == app.cache.NoneValue else v for k, v in results.items()}

    @xray_recorder.capture_async('models.clickdata._query_clickdata')
    async def _query_clickdata(self, clickdata_keys: List):
        async with aioboto3.resource('dynamodb', endpoint_url=self._dynamodb_endpoint) as dynamodb:
            for keychunk in _chunks(clickdata_keys):
                request = {
                    self._dynamodb_table: {
                        "Keys": [{self._primary_key_name: c} for c in keychunk]
                    }
                }
                responses = await dynamodb.batch_get_item(RequestItems=request)

                table = await dynamodb.Table(self._dynamodb_table)
                all_rows = await table.scan()

        clickdata = {row[self._primary_key_name]: row for row in responses["Responses"][self._dynamodb_table]}
        return {k: clickdata.get(k) for k in clickdata_keys}

    def _make_key(self, module: str, item_id: str) -> str:
        """
        Generate the primary key for the clickdata database

        :param module: Prefix for which to get clickdata
        :param item_id: Item for which to get clickdata, or "default" for module clickdata prior
        :return: Clickdata DynamoDB identifier
        """
        return "%s/%s" % (item_id, module)
