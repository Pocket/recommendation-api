import strawberry

from app.models.item import ItemModel


@strawberry.federation.type(extend=True, keys=["item_id"])
@strawberry.experimental.pydantic.type(model=ItemModel)
class Item:
    item_id: strawberry.auto = strawberry.federation.field(external=True)
