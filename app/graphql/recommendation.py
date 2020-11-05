from graphene_pydantic import PydanticObjectType
from app.models.recommendation import RecommendationModel


class Recommendation(PydanticObjectType):
    class Meta:
        model = RecommendationModel
