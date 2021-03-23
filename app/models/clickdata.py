import aioboto3
from aiocache import caches, decorators
from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List, Dict
from enum import Enum

import app.config
import app.cache


# batch get has a 100 item limit
# https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html
def _chunks(index, n=100):
    """Yield successive n-sized chunks from index."""
    for i in range(0, len(index), n):
        yield index[i: i + n]


def _make_key(slate_id: str, key: str) -> str:
    return "%s/%s" % (slate_id, key)


class ClickdataModel(BaseModel):
    mod_item: str = None
    clicks: float = None
    impressions: float = None
    created_at: int = None
    expires_at: int = None

    @staticmethod
    @xray_recorder.capture_async('models.clickdata.get')
    async def get(slate_id: str, item_list: List[str]) -> Dict[str, 'ClickdataModel']:
        """
        Retrieves click data for the given items in the given module (home/topic)

        :param module: the module to filter against - home or topic currently
        :param item_list: list of string item ids
        :return: dictionary of ClickdataModel objects with keys of their respective `mod_item` values
        """
        # Keys are namespaced by the module we are getting data from
        keys = {_make_key(slate_id, item) for item in item_list}

        # Always get the default key, it is used for items that don't have any clickstream data
        keys.add(_make_key(slate_id, "default"))
        keys = list(keys)

        clickdata = await ClickdataModel._query_cached_clickdata(keys)
        # Remove "<modules>/" prefix and remove None values
        clickdata = {k.split("/")[1]: ClickdataModel.parse_obj(v) for k, v in clickdata.items() if v is not None}

        if not clickdata:
            raise ValueError(f"No results from DynamoDB: slate_id {slate_id}")

        return clickdata

    @staticmethod
    @xray_recorder.capture_async('models.clickdata._query_cached_clickdata')
    async def _query_cached_clickdata(clickdata_keys: List) -> Dict[str, 'ClickdataModel']:
        multi_cache = decorators.multi_cached(
            "clickdata_keys",
            ttl=app.config.elasticache['clickdata_ttl'],
            alias=app.cache.clickdata_alias)(ClickdataModel._query_clickdata)

        # multi_cache will get clickdata from cache when available, and call _query_clickdata with all missing keys.
        results = await multi_cache(clickdata_keys)

        # Map app.cache's NoneValue to None. aiocache treats None as a cache miss, so we need a special token for this.
        return {k: None if v == app.cache.NoneValue else v for k, v in results.items()}

    @staticmethod
    @xray_recorder.capture_async('models.clickdata._query_clickdata')
    async def _query_clickdata(clickdata_keys: List):
        table = app.config.dynamodb['recommendation_api_clickdata_table']

        async with aioboto3.resource('dynamodb', endpoint_url=app.config.dynamodb['endpoint_url']) as dynamodb:
            for keychunk in _chunks(clickdata_keys):
                request = {
                    table: {
                        "Keys": [{"mod_item": c} for c in keychunk]
                    }
                }
                responses = await dynamodb.batch_get_item(RequestItems=request)

        clickdata = {row["mod_item"]: row for row in responses["Responses"][table]}
        return {k: clickdata.get(k) for k in clickdata_keys}
