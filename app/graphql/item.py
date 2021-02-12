import graphene

from pydantic import BaseModel
from graphene_pydantic import PydanticObjectType
from graphene_federation import external, extend


class ItemModel(BaseModel):
    item_id: str


@extend(fields='itemId')
class Item(PydanticObjectType):
    item_id = external(graphene.String(required=True))

    class Meta:
        model = ItemModel

