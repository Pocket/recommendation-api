import graphene

from app.graphql.topic import Topic


class UserRecommendationPreferences(graphene.ObjectType):
    preferredTopics = graphene.List(Topic, description="Topics that the user expressed interest in")
