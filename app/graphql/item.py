import graphene

from graphene_pydantic import PydanticObjectType
from graphene_federation import external, extend

from app.models.item import ItemModel


@extend(fields='itemId')
class Item(PydanticObjectType):
    item_id = external(graphene.String(required=True))

    class Meta:
        model = ItemModel

