from graphene_pydantic import PydanticObjectType

# This import needs to exist before TopicRecommendations so that the below class can resolve the recommendation model
from app.graphql.recommendation import Recommendation
from app.models.topic_recommendations import TopicRecommendationsModel


class TopicRecommendations(PydanticObjectType):
    class Meta:
        model = TopicRecommendationsModel
