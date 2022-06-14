from enum import Enum

import aioboto3
from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from typing import List, Optional, Set, Sequence

from app.config import dynamodb as dynamodb_config
from app.models.topic import TopicModel


class TopicProvider:

    def __init__(self, aioboto3_session: aioboto3.session.Session):
        self.aioboto3_session = aioboto3_session

    @xray_recorder.capture_async('models_topic_get_all')
    async def get_all(self) -> List[TopicModel]:
        """
        Retrieves all topics from dynamo db

        :return: a list of TopicModel objects
        """
        async with self.aioboto3_session.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['metadata']['table'])
            response = await table.scan()
        return sorted(list(map(TopicModel.from_dict, response['Items'])), key=lambda topic: topic.slug)

    async def get_topics(self, topics_ids: Sequence[str]) -> List[TopicModel]:
        """
        :param topics_ids: List or tuple of topic ids. Invalid ids are ignored.
        :return: A list of TopicModel objects for the given topic_ids.
        """
        all_topics = await self.get_all()
        topics_by_id = {topic.id: topic for topic in all_topics}
        return [topics_by_id[topic_id] for topic_id in topics_ids if topic_id in topics_by_id]

    @xray_recorder.capture_async('models_topic_get_topic')
    async def get_topic(self, slug: str) -> TopicModel:
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