from typing import List

import strawberry
from strawberry import auto

from app.graphql.slate import Slate
from app.models.slate_lineup import SlateLineupModel


@strawberry.experimental.pydantic.type(model=SlateLineupModel)
class SlateLineup:
    id: strawberry.ID
    requestId: auto
    experimentId: auto
    slates: List[Slate]
