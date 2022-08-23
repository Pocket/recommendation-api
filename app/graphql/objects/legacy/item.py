import strawberry

from app.models.item import ItemModel


@strawberry.federation.type(keys=["item_id"])
@strawberry.experimental.pydantic.type(model=ItemModel)
class Item:
    item_id: str  # This type is a 'str' and not an 'ID' in our graph.
