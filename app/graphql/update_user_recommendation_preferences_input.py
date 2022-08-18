import strawberry
import typing

from app.graphql.topic_input import TopicInput


@strawberry.input
class UpdateUserRecommendationPreferencesInput:
    preferredTopics: typing.List['TopicInput'] = strawberry.field(
        description="Topics that the user expressed interest in"
    )
