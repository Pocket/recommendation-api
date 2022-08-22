import aioboto3
import strawberry

from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProviderV2
from app.graphql.user_recommendation_preferences import UserRecommendationPreferences


@strawberry.federation.type(keys=["id"])
class User:
    id: strawberry.ID = strawberry.field(description='User id, provided by the user service.')
    recommendation_preferences: UserRecommendationPreferences = strawberry.field(
        description='Preferences for recommendations that the user has explicitly set.')

    @classmethod
    async def resolve_reference(cls, id: strawberry.ID):
        aioboto3_session = aioboto3.Session()

        topic_provider = TopicProvider(aioboto3_session=aioboto3_session)

        recommendation_preferences_provider_v2 = UserRecommendationPreferencesProviderV2(
            aioboto3_session=aioboto3_session,
            topic_provider=topic_provider
        )

        preferences_model = await recommendation_preferences_provider_v2.fetch(id)

        return User(
            id=id,
            recommendation_preferences=UserRecommendationPreferences(
                # If the user does not have any preferences set, return an empty list of preferred topics.
                preferred_topics=preferences_model.preferred_topics if preferences_model else []
            ),
        )
