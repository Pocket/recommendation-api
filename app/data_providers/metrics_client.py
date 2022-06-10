from abc import ABC
from typing import List, Callable

from app.models.corpus_item_model import CorpusItemModel
from app.rankers.algorithms import firefox_thompson_sampling_1day


class MetricsFetchable(ABC):
    async def rank_items(self, items: List[CorpusItemModel], rankers: List[Callable]):
        return NotImplemented


class MetricsClient(MetricsFetchable):
    def __init__(self, firefox_newtab_metrics_factory):
        self.firefox_newtab_metrics_factory = firefox_newtab_metrics_factory

    async def rank_items(self, items: List[CorpusItemModel], rankers: List[Callable]) -> List[CorpusItemModel]:
        # I do not check for duplicate rankers here. I know the old flow does.
        # This error is not catastrophic (at most, it reorders items a few times)
        # It's also not likely (an eng AND their reviewer would have to miss two identical lines next to each other)
        # And it's not insidious (would be easy to find and verify if we suspected it was happening)
        # So it's not worth complicating the code to check for IMO
        for ranker in rankers:
            ranker_kwargs = await self.get_engagement_metrics(items, ranker)
            items = ranker(items, **ranker_kwargs)

        return items

    async def get_engagement_metrics(self, ranked_items, ranker):
        ranker_kwargs = {}

        # If this turns into a skyscraper of conditionals I recommend we consider a jump table instead
        if ranker is firefox_thompson_sampling_1day:
            ranker_kwargs = {
                'metrics': await self.firefox_newtab_metrics_factory.get([rec.id for rec in ranked_items])
            }
        return ranker_kwargs
