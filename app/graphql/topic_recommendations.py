from graphene_pydantic import PydanticObjectType
from app.models.topic_recommendations import TopicRecommendationsModel
# This import needs to exist before TopicRecommendations  so that the below class can resolve the recommendation model
from app.graphql.recommendation import Recommendation


class TopicRecommendations(PydanticObjectType):
    class Meta:
        model = TopicRecommendationsModel
