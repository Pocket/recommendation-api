from typing import Optional

import strawberry
from strawberry import auto, UNSET
from strawberry.federation.schema_directives import Key

from app.graphql.item import Item
from app.models.recommendation import RecommendationModel


@strawberry.experimental.pydantic.type(
    model=RecommendationModel,
    # Currently, the `strawberry.federation.type` cannot be combined with `strawberry.experimental.pydantic.type`,
    # so set the key as a directive.
    directives=[Key(fields="item { itemId }", resolvable=UNSET)],
    description='Represents a Recommendation from Pocket',
)
class Recommendation:
    id: strawberry.ID
    feed_item_id: Optional[strawberry.ID] = strawberry.field(deprecation_reason="Use `id`")
    feed_id: auto
    item_id: strawberry.ID
    item: Item = strawberry.federation.field(shareable=True)
    rec_src: str
    publisher: auto
