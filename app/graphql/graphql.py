from graphene import ObjectType, String, Field, List, Schema

from app.models.topic import TopicModel
from app.models.topic_recommendations import TopicRecommendationsModel

from app.graphql.topic import Topic
from app.graphql.topic_recommendations import TopicRecommendations



class Query(ObjectType):
    get_topic_recommendations = Field(TopicRecommendations, slug=String(required=True))
    list_topics = List(Topic)

    def resolve_get_topic_recommendations(self, info, slug) -> TopicRecommendations:
        return TopicRecommendationsModel.get_recommendations(slug=slug)

    def resolve_list_topics(self, info) -> [TopicModel]:
        return TopicModel.get_all()


##
# Graphene requires that you define your schema programmatically.
# Looks like Graphene 3 will support loading from a .graphql file.
# For now this file should stay in sync with *.graphql
##
schema = Schema(query=Query)
