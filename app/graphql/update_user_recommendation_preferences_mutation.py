import datetime

import graphene

from app.data_providers.user_recommendation_preferences import UserRecommendationPreferencesProvider
from app.graphql.topic import Topic
from app.graphql.update_user_recommendation_preferences_input import UpdateUserRecommendationPreferencesInput
from app.models.topic import TopicModel
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel


class UpdateUserRecommendationPreferences(graphene.Mutation):
    class Arguments:
        input = UpdateUserRecommendationPreferencesInput(required=True)

    preferred_topics = graphene.List(Topic, description="Topics that the user expressed interest in")

    async def mutate(root, info, input):
        model = UserRecommendationPreferencesModel(
            user_id=info.context.get('user_id'),
            updated_at=datetime.datetime.utcnow(),
            preferred_topics=await TopicModel.get_topics({t.id for t in input.preferredTopics})
        )

        await UserRecommendationPreferencesProvider().put(model)

        return UpdateUserRecommendationPreferences(preferred_topics=model.preferred_topics)
