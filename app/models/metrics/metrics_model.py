from typing import Dict

from pydantic import BaseModel

# opens and impressions could be int, but we are leaving as float as we may store slate level prior
# parameters in dynamodb using a predefined key, and these will be floats
class MetricsModel(BaseModel):
    id: str
    trailing_1_day_opens: float
    trailing_1_day_impressions: float
    trailing_7_day_opens: float
    trailing_7_day_impressions: float
    trailing_14_day_opens: float
    trailing_14_day_impressions: float
    trailing_28_day_opens: float
    trailing_28_day_impressions: float
    created_at: int = None
    expires_at: int = None
