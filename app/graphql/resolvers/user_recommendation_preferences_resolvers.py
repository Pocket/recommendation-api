import datetime

from strawberry.types import Info

from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.graphql.update_user_recommendation_preferences_input import UpdateUserRecommendationPreferencesInput
from app.graphql.user_recommendation_preferences import UserRecommendationPreferences
from app.graphql.util import get_request_user
from app.models.localemodel import LocaleModel
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel
from app.singletons import DiContainer


async def update_user_recommendation_preferences(
        root, info: Info, input: UpdateUserRecommendationPreferencesInput) -> UserRecommendationPreferences:
    di = DiContainer.get()

    topic_provider = TopicProvider(
        aioboto3_session=di.aioboto3_session,
        locale=LocaleModel.en_US,
        translation_provider=di.translation_provider,
    )

    preferences_provider = UserRecommendationPreferencesProvider(
        aioboto3_session=di.aioboto3_session,
        topic_provider=topic_provider
    )

    preferred_topics = await topic_provider.get_topics([t.id for t in input.preferred_topics])
    request_user = get_request_user(info)

    model = UserRecommendationPreferencesModel(
        hashed_user_id=request_user.hashed_user_id,
        updated_at=datetime.datetime.utcnow(),
        preferred_topics=preferred_topics
    )

    await preferences_provider.put(model)

    return UserRecommendationPreferences(preferred_topics=model.preferred_topics)
