import strawberry

from app.models.topic import TopicModel


@strawberry.experimental.pydantic.type(model=TopicModel, all_fields=True)
class Topic:
    id: strawberry.ID
