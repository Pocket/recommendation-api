from typing import List

import strawberry
from strawberry import auto

from app.graphql.recommendation import Recommendation
from app.models.slate import SlateModel


@strawberry.experimental.pydantic.type(model=SlateModel)
class Slate:
    id: strawberry.ID
    requestId: strawberry.ID
    experimentId: strawberry.ID
    display_name: auto
    description: auto
    recommendations: List[Recommendation]
