import aioboto3
from aiocache import caches, decorators
from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List, Dict
from enum import Enum

from app.config import dynamodb as dynamodb_config
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
    @xray_recorder.capture_async('models_clickdata_get_clickdata_dynamodb')
    async def get_clickdata(module: RecommendationModules, item_list: List[str]) -> Dict[str, 'ClickdataModel']:
        # Key are namespaced by the module we are getting data from
        keys = {make_key(module, item) for item in item_list}

        # Always get the default key, it is used for items that don't have any clickstream data
        keys.add(make_key(module, "default"))
        keys = list(keys)

        clickdata = await ClickdataModel._query_cached_clickdata(keys)

        if not clickdata:
            raise ValueError(f"No results from DynamoDB: module {module.value}")

        return clickdata

    @staticmethod
    @xray_recorder.capture_async('models_clickdata_query_cached_clickdata')
    async def _query_cached_clickdata(clickdata_keys: List) -> Dict[str, 'ClickdataModel']:
        multi_cache = decorators.multi_cached("clickdata_keys", ttl=600, alias=app.cache.alias)
        multi_cache = multi_cache(ClickdataModel._query_clickdata)
        result = await multi_cache(clickdata_keys)
        return result

    @staticmethod
    @xray_recorder.capture_async('models_clickdata_query_clickdata')
    async def _query_clickdata(clickdata_keys: List):
        table = dynamodb_config['recommendation_api_clickdata_table']

        clickdata = dict()
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            for keychunk in chunks(clickdata_keys):
                request = {
                    table: {
                        "Keys": [{"mod_item": c} for c in keychunk]
                    }
                }
                responses = await dynamodb.batch_get_item(RequestItems=request)

                for item in (ClickdataModel.dynamodb_row_to_clickdata(row) for row in responses["Responses"][table]):
                    clickdata[item.mod_item.split("/")[1]] = item

        return clickdata
