import aioboto3

from app.config import TRANSLATIONS_DIR
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.translation import TranslationProvider
from app.models.localemodel import LocaleModel
from tests.assets.topics import business_topic, technology_topic, populate_topics, gaming_topic
from tests.functional.test_dynamodb_base import TestDynamoDBBase


class TestTopicProvider(TestDynamoDBBase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        populate_topics(self.metadata_table, topics=[business_topic, technology_topic])
        self.topic_provider = TopicProvider(
            aioboto3_session=aioboto3.Session(),
            locale=LocaleModel.en_US,
            translation_provider=TranslationProvider(translations_dir=TRANSLATIONS_DIR)
        )

    async def test_get_all(self):
        executed = await self.topic_provider.get_all()
        assert executed == [business_topic, technology_topic]

    async def test_cached_get_all(self):
        assert await self.topic_provider.get_all() == [business_topic, technology_topic]

        # Due to caching, a new 'Gaming' topic is not available instantly from get_all().
        populate_topics(self.metadata_table, topics=[gaming_topic])
        assert await self.topic_provider.get_all() == [business_topic, technology_topic]

        # After caches are reset, the new topic is available.
        await self.topic_provider._scan_table.cache.clear()
        assert await self.topic_provider.get_all() == [business_topic, gaming_topic, technology_topic]
