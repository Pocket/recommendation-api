import asyncio

import aioboto3
import graphene

from graphene_federation import external, extend

from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProviderV2
from app.graphql.user_recommendation_preferences import UserRecommendationPreferences


@extend(fields='id')
class User(graphene.ObjectType):
    id = external(graphene.ID(required=True))
    recommendation_preferences = graphene.Field(UserRecommendationPreferences, required=False)

    def __resolve_reference(self, info, **kwargs):
        """
        TODO: Graphene does not support async __resolve_reference. We should upgrade from Graphene to Strawberry.

        :param info:
        :param kwargs:
        :return:
        """
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.__async_resolve_reference(info, **kwargs))

    async def __async_resolve_reference(self, info, **kwargs):
        aioboto3_session = aioboto3.Session()

        topic_provider = TopicProvider(aioboto3_session=aioboto3_session)

        recommendation_preferences_provider_v2 = UserRecommendationPreferencesProviderV2(
            aioboto3_session=aioboto3_session,
            topic_provider=topic_provider
        )

        recommendation_preferences = await recommendation_preferences_provider_v2.fetch(self.id)
        if recommendation_preferences is None:
            # If the user does not have any preferences set, return an empty list of preferred topics.
            recommendation_preferences = UserRecommendationPreferences(preferredTopics=[])

        return User(
            id=self.id,
            recommendation_preferences=recommendation_preferences,
        )
