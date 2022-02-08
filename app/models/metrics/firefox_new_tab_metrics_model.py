from pydantic import BaseModel


class FirefoxNewTabMetricsModel(BaseModel):
    id: str
    unloaded_at: str = None
    scheduled_surface_item_id: str = None
    slate_experiment_id: str = None
    url: str = None
    slate_id: str = None
    trailing_15_minute_opens: int
    trailing_15_minute_impressions: int
