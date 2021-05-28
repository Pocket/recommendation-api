from typing import Dict

from pydantic import BaseModel


class MetricsModel(BaseModel):
    id: str = None
    clicks: float = None
    impressions: float = None
    # TODO: Add 1, 14, 28 day metrics.
    # TODO: Change "training" to "trailing" once DynamoDB is updated.
    trailing_7_day_opens: float = None
    trailing_7_day_impressions: float = None
    created_at: int = None
    expires_at: int = None
