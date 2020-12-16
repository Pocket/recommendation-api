import boto3
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
    return "%s/%s" % (module, key)


class ClickdataModel(BaseModel):
    mod_item: str = None
    clicks: int = None
    impressions: int = None
    created_at: int = None
    expires_at: int = None

    @staticmethod
    def dynamodb_row_to_clickdata(row: Dict):
        clickdata = ClickdataModel().parse_obj(row)
        return clickdata

    @staticmethod
    @xray_recorder.capture_async('model_clickdata_get_clickdata')
    async def get_clickdata(module: RecommendationModules, item_list: List[str]) -> Dict[str, 'ClickdataModel']:

        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
        table = dynamodb_config['explore_clickdata_table']

        # Key are namespaced by the module we are getting data from
        keys = {make_key(module, item) for item in item_list}

        # Always get the default key, it is used for items that don't have any clickstream data
        keys.add(make_key(module, "default"))

        clickdata = dict()
        for c in chunks(keys):
            request = {
                table: {
                    "Keys": [{"mod_item": "/".join([module, str(c_id)])} for c_id in c]
                    }
                }
            responses = dynamodb.batch_get_item(RequestItems=request)

            for item in map(ClickdataModel.dynamodb_row_to_clickdata, responses["Responses"][table][0]['candidates']):
                clickdata[item.mod_item.split("/")[1]] = item

        return clickdata
