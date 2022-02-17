import itertools
import random
from asyncio import gather

from app.data_providers.curation_api_client import CurationAPIClient
from app.data_providers.slate_provider import SlateProvider
from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory
from app.models.metrics.slate_metrics_factory import SlateMetricsFactory
from app.rankers.algorithms import firefox_thompson_sampling_1day


class Dispatch:
    def __init__(
            self,
            api_client: CurationAPIClient = CurationAPIClient(),
            slate_provider: SlateProvider = SlateProvider()
    ):
        self.api_client = api_client
        self.slate_provider = slate_provider

    async def get_ranked_corpus_slate(self, slate_id, start_date=None, user_id=None):
        corpus_slate_schema = self.slate_provider.get(slate_id)

        # Choose an Experiment
        # TODO: Implement weighting
        experiment = random.choice(corpus_slate_schema.experiments)

        # Fetch Corporeal Candidates
        aggregate_corpus_response = await gather(*(
            self.api_client.get_scheduled_corpus_items(corpus_id, start_date, user_id)
            for corpus_id in experiment.eligible_corpora)
        )

        unranked_items = [individual_response.corpusItems for individual_response in aggregate_corpus_response]
        flattened_unranked_items = list(itertools.chain(*unranked_items))

        # If no rankers, return the same list in the same order that the corpus api handed us
        ranked_items = flattened_unranked_items

        # I do not check for duplicate rankers here. I know the old flow does.
        # This error is not catastrophic (at most, it reorders items a few times)
        # It's also not likely (an eng AND their reviewer would have to miss two identical lines next to each other)
        # And it's not insidious (would be easy to find and verify if we suspected it was happening)
        # So it's not worth complicating the code to check for IMO
        for ranker in experiment.rankers:
            ranker_kwargs = {}
            if ranker is firefox_thompson_sampling_1day:
                ranker_kwargs = {
                    'metrics': await FirefoxNewTabMetricsFactory().get([rec.id for rec in recommendations])
                }

            ranked_items = ranker(ranked_items, **ranker_kwargs)

        return ranked_items


    
