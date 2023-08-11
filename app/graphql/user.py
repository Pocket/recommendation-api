from typing import Optional

import strawberry

from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.graphql.user_recommendation_preferences import UserRecommendationPreferences
from app.models.localemodel import LocaleModel
from app.singletons import DiContainer


@strawberry.federation.type(keys=["id"])
class User:
    id: strawberry.ID = strawberry.field(description='User id, provided by the user service.')
    recommendation_preferences: Optional[UserRecommendationPreferences] = strawberry.field(
        description='Preferences for recommendations that the user has explicitly set.')

    @classmethod
    async def resolve_reference(cls, id: strawberry.ID):
        di = DiContainer.get()

        topic_provider = TopicProvider(
            aioboto3_session=di.aioboto3_session,
            locale=LocaleModel.en_US,
            translation_provider=di.translation_provider,
        )

        recommendation_preferences_provider = UserRecommendationPreferencesProvider(
            aioboto3_session=di.aioboto3_session,
            topic_provider=topic_provider
        )

        preferences_model = await recommendation_preferences_provider.fetch(id)

        return User(
            id=id,
            recommendation_preferences=UserRecommendationPreferences(
                # If the user does not have any preferences set, return an empty list of preferred topics.
                preferred_topics=preferences_model.preferred_topics if preferences_model else []
            ),
        )
