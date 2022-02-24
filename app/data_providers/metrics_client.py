from abc import ABC

from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory
from app.rankers.algorithms import firefox_thompson_sampling_1day

class MetricsFetchable(ABC):
    async def get_engagement_metrics(self, ranked_items, ranker):
        return NotImplemented

class MetricsClient(MetricsFetchable):
    def __init__(self, firefox_newtab_metrics_factory):
        self.firefox_newtab_metrics_factory = firefox_newtab_metrics_factory

    async def get_engagement_metrics(self, ranked_items, ranker):
        ranker_kwargs = {}

        # If this turns into a skyscraper of conditionals I recommend we consider a jump table instead
        if ranker is firefox_thompson_sampling_1day:
            ranker_kwargs = {
                'metrics': await self.firefox_newtab_metrics_factory.get([rec.id for rec in ranked_items])
            }
        return ranker_kwargs
