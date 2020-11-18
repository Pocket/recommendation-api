from graphene import ObjectType, String, Field, List, Schema, Int

from app.models.topic import TopicModel
from app.models.topic_recommendations import TopicRecommendationsModel

from app.graphql.topic import Topic
from app.graphql.topic_recommendations import TopicRecommendations


class Query(ObjectType):
    get_topic_recommendations = Field(TopicRecommendations, slug=String(required=True, description="Topic slug to get "
                                                                                                   "recommendations "
                                                                                                   "for"),
                                      algorithmic_count=Int(default_value=20, description="Number of algorithmic "
                                                                                          "results to return"),
                                      curated_count=Int(default_value=5, description="Number of curated "
                                                                                      "results to return"))
    list_topics = List(Topic)

    def resolve_get_topic_recommendations(self, info, slug: str, algorithmic_count: int,
                                          curated_count: int) -> TopicRecommendations:
        return TopicRecommendationsModel.get_recommendations(slug=slug, algorithmic_count=algorithmic_count,
                                                             curated_count=curated_count)

    def resolve_list_topics(self, info) -> [TopicModel]:
        return TopicModel.get_all()


##
# Graphene requires that you define your schema programmatically.
# Looks like Graphene 3 will support loading from a .graphql file.
# For now this file should stay in sync with *.graphql
##
schema = Schema(query=Query)
