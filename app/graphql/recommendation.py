import strawberry
from strawberry import auto, UNSET
from strawberry.federation.schema_directives import Key

from app.graphql.objects.legacy.item import Item
from app.models.recommendation import RecommendationModel


@strawberry.experimental.pydantic.type(
    model=RecommendationModel,
    # Currently, the `strawberry.federation.type` cannot be combined with `strawberry.experimental.pydantic.type`,
    # so set the key as a directive.
    directives=[Key("item { itemId }", UNSET)],
    description='Represents a Recomendation from Pocket',
)
class Recommendation:
    id: strawberry.ID
    feed_item_id: auto = strawberry.field(deprecation_reason="Use `id`")
    feed_id: auto
    item_id: auto
    item: Item = strawberry.federation.field(shareable=True)
    rec_src: auto
    publisher: auto
