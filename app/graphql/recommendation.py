import strawberry
from strawberry import auto

from app.graphql.objects.legacy.item import Item
from app.models.recommendation import RecommendationModel


@strawberry.experimental.pydantic.type(model=RecommendationModel)
class Recommendation:
    id: strawberry.ID
    feed_item_id: auto
    feed_id: auto
    item_id: auto
    item: Item
    rec_src: auto
    publisher: auto
