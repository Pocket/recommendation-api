import aioboto3

from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from enum import Enum
from pydantic import BaseModel
from typing import Dict, Optional, Set

from app.config import dynamodb as dynamodb_config


class PageType(str, Enum):
    """
    Define the possible page types for a topic.
    """
    editorial_collection = 'editorial_collection'
    topic_page = 'topic_page'


class TopicModel(BaseModel):
    """
    Models a topic, e.g. Technology, Gaming.
    """
    id: str
    corpus_topic_id: str
    name: str
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
    def from_dict(item: Dict) -> 'TopicModel':
        # Map display_name to name. display_name is being deprecated, but still present in the database.
        return TopicModel.parse_obj(dict({'name': item['display_name']}, **item))

    @staticmethod
    @xray_recorder.capture_async('models_topic_get_all')
    async def get_all() -> ['TopicModel']:
        """
        Retrieves all topics from dynamo db

        :return: a list of TopicModel objects
        """
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['metadata']['table'])
            response = await table.scan()
        return sorted(list(map(TopicModel.from_dict, response['Items'])), key=lambda topic: topic.slug)

    @staticmethod
    async def get_topics(topics_ids: Set[str]) -> ['TopicModel']:
        """
        Retrieves all topics from dynamo db

        :return: a list of TopicModel objects
        """
        all_topics = await TopicModel.get_all()
        return [t for t in all_topics if t.id in topics_ids]

    @staticmethod
    @xray_recorder.capture_async('models_topic_get_topic')
    async def get_topic(slug: str) -> Optional['TopicModel']:
        """
        Retrieves a single topic from dynamo db

        :param slug: string slug of the topic to be retrieved
        :return: a TopicModel object
        """
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['metadata']['table'])
            response = await table.query(IndexName='slug', Limit=1, KeyConditionExpression=Key('slug').eq(slug))
        if response['Items']:
            return TopicModel.from_dict(response['Items'][0])
        raise ValueError('Topic not found')
