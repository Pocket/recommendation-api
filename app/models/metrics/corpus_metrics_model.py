from datetime import datetime

from pydantic import BaseModel

from app.models.surface import Surface


class CorpusMetricsSegmentModel(BaseModel):
    """
    Defines the dimensions along which metrics are segmented
    """
    surface: Surface
    corpus_slate_config_id: str
    corpus_item_id: str


class CorpusMetricsModel(BaseModel):
    """
    Extends the above segment model with metrics.
    """
    segment: CorpusMetricsSegmentModel
    updated_at: datetime = None
    trailing_1_day_opens: int
    trailing_1_day_impressions: int
    trailing_7_day_opens: int
    trailing_7_day_impressions: int
    trailing_14_day_opens: int
    trailing_14_day_impressions: int
    trailing_28_day_opens: int
    trailing_28_day_impressions: int
