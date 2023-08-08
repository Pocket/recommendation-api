import datetime
from typing import List

from pydantic import BaseModel

from app.models.topic import TopicModel


class UserRecommendationPreferencesModelV2(BaseModel):
    hashed_user_id: str  # The difference between v1 and v2 is that this column is renamed to store the hashed user id.
    updated_at: datetime.datetime
    preferred_topics: List[TopicModel]
