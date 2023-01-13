from typing import List

import pytest

from app.data_providers.topic_provider import TopicProvider
from app.models.localemodel import LocaleModel
from app.models.topic import TopicModel
from tests.assets.topics import all_topic_fixtures


class MockTopicProvider(TopicProvider):

    async def get_all(self) -> List[TopicModel]:
        return all_topic_fixtures


@pytest.fixture
def topic_provider_en_us(translation_provider):
    return MockTopicProvider(aioboto3_session=None, locale=LocaleModel.en_US, translation_provider=translation_provider)
