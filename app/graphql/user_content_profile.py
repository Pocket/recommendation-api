import graphene

from app.graphql.topic import Topic


class UserContentProfile(graphene.ObjectType):
    preferredTopics = graphene.List(Topic, description="Topics that the user expressed interest in")
