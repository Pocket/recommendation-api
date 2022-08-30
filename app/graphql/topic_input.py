import strawberry


@strawberry.input
class TopicInput:
    id: strawberry.ID = strawberry.field(description='The id of the topic')
