import aioboto3

from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from enum import Enum
from pydantic import BaseModel
from typing import Optional, List

from app.config import dynamodb as dynamodb_config
from app.graphql.page_type import PageType


class TopicModel(BaseModel):
    """
    Models a topic, e.g. Technology, Gaming.
    """
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
        """
        Retrieves all topics from dynamo db

        :return: a list of TopicModel objects
        """
        session = aioboto3.Session()
        async with session.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['metadata']['table'])
            response = await table.scan()
        return sorted(list(map(TopicModel.parse_obj, response['Items'])), key=lambda topic: topic.slug)

    @staticmethod
    @xray_recorder.capture_async('models_topic_get_topic')
    async def get_topic(slug: str) -> Optional['TopicModel']:
        """
        Retrieves a single topic from dynamo db

        :param slug: string slug of the topic to be retrieved
        :return: a TopicModel object
        """
        session = aioboto3.Session()
        async with session.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['metadata']['table'])
            response = await table.query(IndexName='slug', Limit=1, KeyConditionExpression=Key('slug').eq(slug))
        if response['Items']:
            return TopicModel.parse_obj(response['Items'][0])
        raise ValueError('Topic not found')
