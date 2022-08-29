from typing import List

import strawberry

from app.graphql.recommendation import Recommendation
from app.models.slate import SlateModel


@strawberry.experimental.pydantic.type(
    model=SlateModel,
    description='A grouping of item recommendations that relate to each other under a specific name and description')
class Slate:
    id: strawberry.auto
    requestId: strawberry.ID
    experimentId: strawberry.ID
    display_name: strawberry.auto
    description: strawberry.auto
    recommendations: List[Recommendation]
