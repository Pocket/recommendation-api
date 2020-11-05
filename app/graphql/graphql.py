from graphene import ObjectType, String, Field, List, Schema
from app.graphql.topic_recommendations import TopicRecommendations

from app.models.topic import TopicModel
from app.graphql.topic import Topic

from app.models.recommendation import RecommendationModel, RecommendationType


class Query(ObjectType):
    get_topic_recommendations = Field(TopicRecommendations, slug=String(required=True))
    list_topics = List(Topic)

    def resolve_get_topic_recommendations(self, info, slug) -> TopicRecommendations:
        topic_recommendations = TopicRecommendations()
        topic_recommendations.algorithmic_recommendations = RecommendationModel.get_recommendations(
            slug=slug,
            recommendation_type=RecommendationType.ALGORITHMIC
        )
        topic_recommendations.curated_recommendations = RecommendationModel.get_recommendations(
            slug=slug,
            recommendation_type=RecommendationType.CURATED
        )
        return topic_recommendations

    def resolve_list_topics(self, info) -> [TopicModel]:
        return TopicModel.get_all()


##
# Graphene requires that you define your schema programmatically.
# Looks like Graphene 3 will support loading from a .graphql file.
# For now this file should stay in sync with *.graphql
##
schema = Schema(query=Query)
