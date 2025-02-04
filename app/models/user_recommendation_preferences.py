import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from app.models.topic import TopicModel


class UserRecommendationPreferencesModel(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    hashed_user_id: str
    updated_at: datetime.datetime
    preferred_topics: List[TopicModel]
