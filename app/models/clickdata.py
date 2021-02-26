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
def chunks(index, n=100):
    """Yield successive n-sized chunks from index."""
    for i in range(0, len(index), n):
        yield index[i: i + n]


class RecommendationModules(Enum):
    HOME = 'home'
    TOPIC = 'topic'


def make_key(module: RecommendationModules, key: str):
    return "%s/%s" % (module.value, key)


class ClickdataModel(BaseModel):
    mod_item: str = None
    clicks: float = None
    impressions: float = None
    created_at: int = None
    expires_at: int = None

    @staticmethod
    def dynamodb_row_to_clickdata(row: Dict):
        clickdata = ClickdataModel().parse_obj(row)
        return clickdata


    @staticmethod
    @xray_recorder.capture_async('models.clickdata.get')
    async def get(module: RecommendationModules, item_list: List[str]) -> Dict[str, 'ClickdataModel']:
        # Keys are namespaced by the module we are getting data from
        keys = {make_key(module, item) for item in item_list}

        # Always get the default key, it is used for items that don't have any clickstream data
        keys.add(make_key(module, "default"))
        keys = list(keys)

        clickdata = await ClickdataModel._query_cached_clickdata(keys)
        # Remove "<modules>/" prefix and remove None values
        clickdata = {k.split("/")[1]: ClickdataModel.parse_obj(v) for k, v in clickdata.items() if v is not None}

        if not clickdata:
            raise ValueError(f"No results from DynamoDB: module {module.value}")

        return clickdata

    @staticmethod
    @xray_recorder.capture_async('models.clickdata._query_cached_clickdata')
    async def _query_cached_clickdata(clickdata_keys: List) -> Dict[str, 'ClickdataModel']:
        multi_cache = decorators.multi_cached(
            "clickdata_keys",
            ttl=app.config.elasticache['clickdata_ttl'],
            alias=app.cache.clickdata_alias)(ClickdataModel._query_clickdata)

        results = await multi_cache(clickdata_keys)

        # Map app.cache's NoneValue to None. aiocache treats None as a cache miss, so we need a special token for this.
        return {k: None if v == app.cache.NoneValue else v for k, v in results.items()}

    @staticmethod
    @xray_recorder.capture_async('models.clickdata._query_clickdata')
    async def _query_clickdata(clickdata_keys: List):
        table = app.config.dynamodb['recommendation_api_clickdata_table']

        async with aioboto3.resource('dynamodb', endpoint_url=app.config.dynamodb['endpoint_url']) as dynamodb:
            for keychunk in chunks(clickdata_keys):
                request = {
                    table: {
                        "Keys": [{"mod_item": c} for c in keychunk]
                    }
                }
                responses = await dynamodb.batch_get_item(RequestItems=request)

        clickdata = {row["mod_item"]: row for row in responses["Responses"][table]}
        return {k: clickdata.get(k) for k in clickdata_keys}
