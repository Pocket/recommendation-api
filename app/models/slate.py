import aioboto3

from aws_xray_sdk.core import xray_recorder
from pydantic import BaseModel
from typing import List

from app.config import dynamodb as dynamodb_config
from app.models.recommendation import RecommendationModel


class SlateModel(BaseModel):
    id: str
    requestID: str = None
    experimentID: str = None
    pageviewGUID: str = None
    display_name: str = None
    description: str = None
    recommendations: List[RecommendationModel]

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_slate')
    async def get_slate(slate_id: str) -> 'SlateModel':
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['recommendation_api_metadata_table'])
            response = await table.query(IndexName='slug', Limit=1, KeyConditionExpression=Key('slug').eq(slug))
        if response['Items']:
            return TopicModel.parse_obj(response['Items'][0])
        raise ValueError('Topic not found')

        return SlateModel.parse_obj({
            'id': slate_id,
            'requestID': '1',
            'experimentID': '1',
            'pageviewGUID': '1',
            'display_name': 'Fake slate',
            'description': 'Fake description for the people',
            'recommendations': [{
                'feed_item_id': '1',
                'item_id': '1',
                'feed_id': '1',
                'rec_src': 'RecommendationAPI',
                'publisher': 'Fake Times'
            }],
        })

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_all')
    async def get_all() -> ['SlateModel']:
        return [SlateModel.get_slate('fake1'), SlateModel.get_slate('fake2')]
