from graphene import ObjectType, String, Field, List, Schema
from app.graphql.topic_recommendations import TopicRecommendations
from app.graphql.recommendation import Recommendation
from app.graphql.topic import Topic
from app.models.topic import Topic as TopicModel


class Query(ObjectType):
    get_topic_recommendations = Field(TopicRecommendations, slug=String(required=True))
    list_topics = List(Topic)

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_get_topic_recommendations(self, info, slug):
        topic_recommendations = TopicRecommendations()

        recommendation = Recommendation()
        recommendation.feed_item_id = 'ExploreTopics/123'
        recommendation.feed_id = 1
        recommendation.item_id = 123

        topic_recommendations.algorithmic_recommendations = [recommendation]
        topic_recommendations.curated_recommendations = []
        return topic_recommendations

    def resolve_list_topics(self, info):
        return TopicModel.get_all()


##
# Graphene requires that you define your schema programmatically.
# Looks like Graphene 3 will support loading from a .graphql file.
# For now this file should stay in sync with *.graphql
##
schema = Schema(query=Query)
