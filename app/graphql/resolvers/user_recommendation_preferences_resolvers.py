import asyncio
import datetime
from typing import Optional

import aioboto3
from strawberry.types import Info

from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import (
    UserRecommendationPreferencesProvider,
    UserRecommendationPreferencesProviderV2,
)
from app.graphql.update_user_recommendation_preferences_input import UpdateUserRecommendationPreferencesInput
from app.graphql.user_recommendation_preferences import UserRecommendationPreferences
from app.graphql.util import get_user_ids
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel, \
    UserRecommendationPreferencesModelV2


async def update_user_recommendation_preferences(
        root, info: Info, input: UpdateUserRecommendationPreferencesInput) -> Optional[UserRecommendationPreferences]:
    aioboto3_session = aioboto3.Session()

    topic_provider = TopicProvider(aioboto3_session=aioboto3_session)

    preferences_provider = UserRecommendationPreferencesProvider(
        aioboto3_session=aioboto3_session,
        topic_provider=topic_provider
    )

    preferences_provider_v2 = UserRecommendationPreferencesProviderV2(
        aioboto3_session=aioboto3_session,
        topic_provider=topic_provider
    )

    preferred_topics = await topic_provider.get_topics([t.id for t in input.preferred_topics])
    user_ids = get_user_ids(info)

    model = UserRecommendationPreferencesModel(
        user_id=user_ids.user_id,  # Integer user id
        updated_at=datetime.datetime.utcnow(),
        preferred_topics=preferred_topics
    )

    model_v2 = UserRecommendationPreferencesModelV2(
        hashed_user_id=user_ids.hashed_user_id,
        updated_at=datetime.datetime.utcnow(),
        preferred_topics=preferred_topics
    )

    await asyncio.gather(
        preferences_provider.put(model),
        preferences_provider_v2.put(model_v2),
    )

    return UserRecommendationPreferences(preferred_topics=model.preferred_topics)
