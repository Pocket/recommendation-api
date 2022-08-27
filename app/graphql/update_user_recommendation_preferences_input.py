import strawberry
import typing

from app.graphql.topic_input import TopicInput


@strawberry.input
class UpdateUserRecommendationPreferencesInput:
    preferred_topics: typing.List['TopicInput'] = strawberry.field(
        description='Topics that the user expressed interest in.'
    )
