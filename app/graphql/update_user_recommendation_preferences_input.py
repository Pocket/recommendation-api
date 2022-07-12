import graphene

from app.graphql.topic_input import TopicInput


class UpdateUserRecommendationPreferencesInput(graphene.InputObjectType):
    preferredTopics = graphene.List(
        TopicInput,
        required=True,
        description="Topics that the user expressed interest in"
    )
