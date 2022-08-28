import strawberry
from typing import List, Optional

from app.graphql.topic import Topic


@strawberry.type
class UserRecommendationPreferences:
    preferred_topics: Optional[List['Topic']] = strawberry.field(description="Topics that the user expressed interest in.")
