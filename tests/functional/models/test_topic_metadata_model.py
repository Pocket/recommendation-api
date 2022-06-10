from tests.assets.topics import business_topic, technology_topic, populate_topics
from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.models.topic import TopicModel


class TestTopicMetadata(TestDynamoDBBase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        populate_topics(self.metadata_table)

    async def test_main_list_topics(self):
        executed = await TopicModel.get_all()
        assert executed == [business_topic, technology_topic]

    async def test_main_get_topic(self):
        executed = await TopicModel.get_topic('business')
        assert executed == business_topic

    async def test_main_get_nonexistent_topic(self):
        with self.assertRaises(ValueError):
            await TopicModel.get_topic(slug='stonks')

