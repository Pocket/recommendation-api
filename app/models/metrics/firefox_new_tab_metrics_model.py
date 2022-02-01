from pydantic import BaseModel


class FirefoxNewTabMetricsModel(BaseModel):
    id: str
    unloaded_at: str = None
    url: str = None
    slate_id: str = None
    trailing_15_minute_opens: int
    trailing_15_minute_impressions: int
