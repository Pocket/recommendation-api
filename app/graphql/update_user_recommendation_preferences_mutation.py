import datetime

import aioboto3
import graphene

from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.graphql.topic import Topic
from app.graphql.update_user_recommendation_preferences_input import UpdateUserRecommendationPreferencesInput
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel


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

        model = UserRecommendationPreferencesModel(
            user_id=info.context.get('user_id'),
            updated_at=datetime.datetime.utcnow(),
            preferred_topics=await topic_provider.get_topics([t.id for t in input.preferredTopics])
        )

        await preferences_provider.put(model)

        return UpdateUserRecommendationPreferences(preferred_topics=model.preferred_topics)
