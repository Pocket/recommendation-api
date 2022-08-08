import datetime
from typing import List

from pydantic import BaseModel

from app.models.topic import TopicModel


class UserRecommendationPreferencesModel(BaseModel):
    user_id: str
    updated_at: datetime.datetime
    preferred_topics: List[TopicModel]


class UserRecommendationPreferencesModelV2(BaseModel):
    hashed_user_id: str  # Only difference between v1 and v2 is that this column is renamed
    updated_at: datetime.datetime
    preferred_topics: List[TopicModel]
