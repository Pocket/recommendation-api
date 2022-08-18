import strawberry

from app.models.topic import TopicModel


@strawberry.experimental.pydantic.type(model=TopicModel)
class Topic:
    id: strawberry.ID
    name: strawberry.auto
    # TODO: Extend
