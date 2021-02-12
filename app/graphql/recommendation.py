from graphene_pydantic import PydanticObjectType
from graphene import NonNull

from app.models.recommendation import RecommendationModel
from app.graphql.item import Item


class Recommendation(PydanticObjectType):
    item = NonNull(Item)

    class Meta:
        model = RecommendationModel
