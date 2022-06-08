import itertools
import random
from typing import Optional
import uuid
from asyncio import gather

from app.data_providers.corpus.corpus_fetchable import CorpusFetchable
from app.data_providers.metrics_client import MetricsFetchable
from app.data_providers.slate_provider import SlateProvider
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel


class Dispatch:
    """
    This class is responsible for accepting:

     a dependency to get items to rank (api_client),
     a strategy for ranking them (slate_provider),
     and the data to execute ranking (metrics_client),

     and then using those three things to shape the list of items to the order and size we serve to a client.

     If there are NO rankers, it sends the original list of items, with no reshaping, to the client.
    """
    def __init__(
            self,
            api_client: CorpusFetchable,
            slate_provider: SlateProvider,
            metrics_client: Optional[MetricsFetchable] = None
    ):
        self.api_client = api_client
        self.slate_provider = slate_provider
        self.metrics_client = metrics_client

    async def get_ranked_corpus_slate(self, slate_id, start_date=None, user_id=None) -> CorpusSlateModel:
        corpus_slate_schema = self.slate_provider.get(slate_id)

        # Choose an Experiment
        # TODO: Implement weighting
        experiment = random.choice(corpus_slate_schema.experiments)

        # Fetch Corporeal Candidates
        aggregate_corpus_response = await gather(*(
            self.api_client.get_ranked_corpus_items(corpus_id, start_date, user_id)
            for corpus_id in experiment.eligible_corpora)
        )

        flattened_unranked_items = list(itertools.chain(*aggregate_corpus_response))

        # If no rankers, return the same list in the same order that the corpus api handed us
        ranked_items = flattened_unranked_items

        # I do not check for duplicate rankers here. I know the old flow does.
        # This error is not catastrophic (at most, it reorders items a few times)
        # It's also not likely (an eng AND their reviewer would have to miss two identical lines next to each other)
        # And it's not insidious (would be easy to find and verify if we suspected it was happening)
        # So it's not worth complicating the code to check for IMO
        for ranker in experiment.rankers:
            ranker_kwargs = {}
            if self.metrics_client:
                ranker_kwargs = await self.metrics_client.get_engagement_metrics(ranked_items, ranker)

            ranked_items = ranker(ranked_items, **ranker_kwargs)

        recommendations = [CorpusRecommendationModel(id=uuid.uuid4().hex, corpus_item=item) for item in ranked_items]

        return CorpusSlateModel(
            id=slate_id,
            headline=corpus_slate_schema.displayName,
            subheadline=corpus_slate_schema.description,
            recommendations=recommendations,
        )


    
