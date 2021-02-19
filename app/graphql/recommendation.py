from graphene_pydantic import PydanticObjectType
from graphene_federation import key

from app.models.recommendation import RecommendationModel


@key('item { itemId }')
class Recommendation(PydanticObjectType):
    class Meta:
        model = RecommendationModel
