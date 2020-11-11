from enum import Enum
from typing import Optional

from pydantic import BaseModel
import boto3
from app.config import dynamodb as dynamodb_config
from boto3.dynamodb.conditions import Key


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

    @staticmethod
    def get_all() -> ['TopicModel']:
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
        table = dynamodb.Table(dynamodb_config['explore_topics_metadata_table'])
        response = table.scan()
        return list(map(TopicModel.parse_obj, response['Items']))

    @staticmethod
    def get_topic(slug: str) -> Optional['TopicModel']:
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
        table = dynamodb.Table(dynamodb_config['explore_topics_metadata_table'])
        response = table.query(IndexName='slug', Limit=1, KeyConditionExpression=Key('slug').eq(slug))
        if response['Items']:
            return TopicModel.parse_obj(response['Items'][0])
        raise ValueError('Topic not found')
