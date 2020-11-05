from graphene import ObjectType, String, Field, List, Schema
from app.graphql.topic_recommendations import TopicRecommendations

from app.models.topic import TopicModel
from app.graphql.topic import Topic

from app.models.recommendation import RecommendationModel


class Query(ObjectType):
    get_topic_recommendations = Field(TopicRecommendations, slug=String(required=True))
    list_topics = List(Topic)

    def resolve_get_topic_recommendations(self, info, slug):
        topic_recommendations = TopicRecommendations()
        topic_recommendations.algorithmic_recommendations = RecommendationModel.get_algorithmic_recommendations(
            topic=slug)
        topic_recommendations.curated_recommendations = RecommendationModel.get_curated_recommendations(topic=slug)
        return topic_recommendations

    def resolve_list_topics(self, info):
        return TopicModel.get_all()


##
# Graphene requires that you define your schema programmatically.
# Looks like Graphene 3 will support loading from a .graphql file.
# For now this file should stay in sync with *.graphql
##
schema = Schema(query=Query)
