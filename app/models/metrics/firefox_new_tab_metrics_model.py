from pydantic import BaseModel


class FirefoxNewTabMetricsModel(BaseModel):
    id: str
    unloaded_at: str = None
    scheduled_surface_item_id: str
    slate_experiment_id: str
    url: str
    slate_id: str
    trailing_1_day_opens: int
    trailing_1_day_impressions: int
