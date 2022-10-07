from typing import NewType

import strawberry

from app.models.link import LinkModel

Url = strawberry.scalar(
    NewType("Url", str),
)


@strawberry.experimental.pydantic.type(
    model=LinkModel,
    description='Web link')
class Link:
    url: Url
    text: strawberry.auto
