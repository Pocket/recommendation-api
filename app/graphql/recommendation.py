from graphene_pydantic import PydanticObjectType
from graphene import NonNull, String
from graphene_federation import key

from app.models.recommendation import RecommendationModel
from app.graphql.item import Item


@key('recSrc')
class Recommendation(PydanticObjectType):
    item_id = NonNull(String)
    item = NonNull(Item)
    rec_src = NonNull(String)

    class Meta:
        model = RecommendationModel
