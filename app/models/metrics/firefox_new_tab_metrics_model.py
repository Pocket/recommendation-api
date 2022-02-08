from pydantic import BaseModel


class FirefoxNewTabMetricsModel(BaseModel):
    id: str
    unloaded_at: str = None
    scheduled_surface_item_id: str
    slate_experiment_id: str
    url: str
    slate_id: str
    trailing_15_minute_opens: int
    trailing_15_minute_impressions: int
