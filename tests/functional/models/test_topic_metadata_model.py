import aioboto3

from app.data_providers.topic_provider import TopicProvider
from tests.assets.topics import business_topic, technology_topic, populate_topics
from tests.functional.test_dynamodb_base import TestDynamoDBBase


class TestTopicMetadata(TestDynamoDBBase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        populate_topics(self.metadata_table, topics=[business_topic, technology_topic])
        self.topic_provider = TopicProvider(aioboto3_session=aioboto3.Session())

    async def test_main_list_topics(self):
        executed = await self.topic_provider.get_all()
        assert executed == [business_topic, technology_topic]

    async def test_main_get_topic(self):
        executed = await self.topic_provider.get_topic('business')
        assert executed == business_topic

    async def test_main_get_nonexistent_topic(self):
        with self.assertRaises(ValueError):
            await self.topic_provider.get_topic(slug='stonks')

