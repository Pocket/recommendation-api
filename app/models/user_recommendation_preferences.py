import datetime
from typing import List

from pydantic import BaseModel

from app.models.topic import TopicModel


class UserRecommendationPreferencesModel(BaseModel):
    user_id: str
    updated_at: datetime.datetime
    preferred_topics: List[TopicModel]
