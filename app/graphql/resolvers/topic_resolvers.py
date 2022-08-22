from typing import List

import aioboto3

from app.data_providers.topic_provider import TopicProvider
from app.graphql.topic import Topic


async def list_topics() -> List[Topic]:
    topic_models = await TopicProvider(aioboto3_session=aioboto3.Session()).get_all()
    return [Topic.from_pydantic(topic_model) for topic_model in topic_models]
