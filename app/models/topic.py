import aioboto3

from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from enum import Enum
from pydantic import BaseModel
from typing import Optional

from app.config import dynamodb as dynamodb_config


class PageType(str, Enum):
    editorial_collection = 'editorial_collection'
    topic_page = 'topic_page'


class TopicModel(BaseModel):
    id: str
    display_name: str
    page_type: PageType
    slug: str
    query: str
    curator_label: str
    is_displayed: bool
    is_promoted: bool
    display_note: str = None
    social_title: str = None
    social_description: str = None
    social_image: str = None
    custom_feed_id: str = None

    @staticmethod
    @xray_recorder.capture_async('models_topic_get_all')
    async def get_all() -> ['TopicModel']:
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['recommendation_api_metadata_table'])
            response = await table.scan()
        return sorted(list(map(TopicModel.parse_obj, response['Items'])), key=lambda topic: topic.slug)

    @staticmethod
    @xray_recorder.capture_async('models_topic_get_topic')
    async def get_topic(slug: str) -> Optional['TopicModel']:
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['recommendation_api_metadata_table'])
            response = await table.query(IndexName='slug', Limit=1, KeyConditionExpression=Key('slug').eq(slug))
        if response['Items']:
            return TopicModel.parse_obj(response['Items'][0])
        raise ValueError('Topic not found')
