import strawberry
import typing

from app.graphql.topic import Topic


@strawberry.type
class UserRecommendationPreferences:
    preferred_topics: typing.List['Topic'] = strawberry.field(description="Topics that the user expressed interest in.")
