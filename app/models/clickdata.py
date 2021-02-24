import aioboto3
from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List, Dict
from enum import Enum
from app.config import dynamodb as dynamodb_config


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
    @xray_recorder.capture_async('models_clickdata_get_clickdata')
    async def get_clickdata(module: RecommendationModules, item_list: List[str]) -> Dict[str, 'ClickdataModel']:
        """
        Retrieves click data for the given items in the given module (home/topic)

        :param module: the module to filter against - home or topic currently
        :param item_list: list of string item ids
        :return: dictionary of ClickdataModel objects with keys of their respective `mod_item` values
        """
        table = dynamodb_config['recommendation_api_clickdata_table']

        # Key are namespaced by the module we are getting data from
        keys = {make_key(module, item) for item in item_list}

        # Always get the default key, it is used for items that don't have any clickstream data
        keys.add(make_key(module, "default"))
        keys = list(keys)

        clickdata = {}

        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            for keychunk in chunks(keys):
                request = {
                    table: {
                        "Keys": [{"mod_item": c} for c in keychunk]
                        }
                    }

                responses = await dynamodb.batch_get_item(RequestItems=request)

                for item in (ClickdataModel.parse_obj(row) for row in responses["Responses"][table]):
                    clickdata[item.mod_item.split("/")[1]] = item

        if not clickdata:
            raise ValueError(f"No results from DynamoDB: module {module.value}")

        return clickdata
