from graphene import ObjectType, String, List, Schema
from app.graphql.topic_recommendations import TopicRecommendations
from app.graphql.topic import Topic
from app.models.topic import Topic as TopicModel


class Query(ObjectType):
    get_topic_recommendations = List(slug=String(required=True), of_type=TopicRecommendations)
    list_topics = List(Topic)

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_get_topic_recommendations(self, info, slug):
        topic_recommendations = TopicRecommendations()
        topic_recommendations.algorithmic_recommendations = List()
        topic_recommendations.curated_recommendations = List()
        return topic_recommendations

    def resolve_list_topics(self, info):
        return TopicModel.get_all()


##
# Graphene requires that you define your schema programaticaly.
# Looks like Graphene 3 will support loading from a .graphql file.
# For now this file should stay in sync with *.graphql
##
schema = Schema(query=Query)
