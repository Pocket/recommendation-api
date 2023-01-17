from typing import List

import aioboto3

from app.data_providers.topic_provider import TopicProvider
from app.graphql.topic import Topic
from app.models.localemodel import LocaleModel
from app.singletons import DiContainer


async def list_topics() -> List[Topic]:
    topic_models = await TopicProvider(
        aioboto3_session=aioboto3.Session(),
        locale=LocaleModel.en_US,
        translation_provider=DiContainer.get().translation_provider,
    ).get_all()
    return [Topic.from_pydantic(topic_model) for topic_model in topic_models]


async def resolve_recommendation_preference_topics() -> List[Topic]:
    topic_models = await TopicProvider(
        aioboto3_session=aioboto3.Session(),
        locale=LocaleModel.en_US,
        translation_provider=DiContainer.get().translation_provider,
    ).get_all()
    exclude_topic_names = ['Gaming', 'Sports', 'Education', 'Coronavirus']
    return [Topic.from_pydantic(t) for t in topic_models if t.name not in exclude_topic_names]
