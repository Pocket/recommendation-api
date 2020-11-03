from graphene import ObjectType, List
from app.graphql.recommendation import Recommendation


class TopicRecommendations(ObjectType):
    curated_recommendations = List(of_type=Recommendation, required=True)
    algorithmic_recommendations = List(of_type=Recommendation, required=True)
