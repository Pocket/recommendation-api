from datetime import datetime

from pydantic import BaseModel


class CorpusItemEngagementModel(BaseModel):
    key: str
    recommendation_surface_id: str
    corpus_slate_configuration_id: str
    corpus_item_id: str
    trailing_1_day_opens: int
    trailing_1_day_impressions: int
    trailing_7_day_opens: int
    trailing_7_day_impressions: int
    trailing_14_day_opens: int
    trailing_14_day_impressions: int
    trailing_21_day_opens: int
    trailing_21_day_impressions: int
    trailing_28_day_opens: int
    trailing_28_day_impressions: int
    updated_at: datetime
