import asyncio
import datetime

import aioboto3
import graphene

from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import (
    UserRecommendationPreferencesProvider,
    UserRecommendationPreferencesProviderV2,
)
from app.graphql.topic import Topic
from app.graphql.update_user_recommendation_preferences_input import UpdateUserRecommendationPreferencesInput
from app.models.user import User
from app.models.user_recommendation_preferences import (
    UserRecommendationPreferencesModel,
    UserRecommendationPreferencesModelV2,
)


class UpdateUserRecommendationPreferences(graphene.Mutation):
    class Arguments:
        input = UpdateUserRecommendationPreferencesInput(required=True)

    preferred_topics = graphene.List(Topic, description="Topics that the user expressed interest in")

    async def mutate(root, info, input):
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

        preferred_topics = await topic_provider.get_topics([t.id for t in input.preferredTopics])
        user: User = info.context['user']

        model = UserRecommendationPreferencesModel(
            user_id=user.user_id,  # Integer user id
            updated_at=datetime.datetime.utcnow(),
            preferred_topics=preferred_topics
        )

        model_v2 = UserRecommendationPreferencesModelV2(
            hashed_user_id=user.hashed_user_id,
            updated_at=datetime.datetime.utcnow(),
            preferred_topics=preferred_topics
        )

        await asyncio.gather(
            preferences_provider.put(model),
            preferences_provider_v2.put(model_v2),
        )

        return UpdateUserRecommendationPreferences(preferred_topics=model.preferred_topics)
