from typing import List

from app.data_providers.topic_provider import TopicProvider
from app.models.topic import TopicModel
from tests.assets.topics import all_topic_fixtures


class MockTopicProvider(TopicProvider):

    async def get_all(self) -> List[TopicModel]:
        return all_topic_fixtures
