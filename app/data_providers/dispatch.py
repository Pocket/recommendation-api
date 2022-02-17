import random

from app.data_providers.curation_api_client import CurationAPIClient
from app.data_providers.slate_provider import SlateProvider


class Dispatch:
    def __init__(
            self,
            api_client: CurationAPIClient = CurationAPIClient,
            slate_provider: SlateProvider = SlateProvider
    ):
        self.api_client = api_client
        self.slate_provider = slate_provider

    async def get_ranked_items(self, slate_id, start_date=None, user_id=None):
        corpus_slate_schema = self.slate_provider.get(slate_id)

        # Choose an Experiment
        # TODO: Implement weighting
        experiment = random.choice(corpus_slate_schema.experiments)

        # Fetch Corporeal Candidates
        # TODO: Collect results from multiple corpora
        corpus_response = await self.api_client.get_scheduled_corpus_items(slate_id, start_date, user_id)
        unranked_items = corpus_response.corpusItems

        ranked_items = []
        # I do not check for duplicate rankers here. I know the old flow does.
        # This error is not catastrophic (at most, it reorders items a few times)
        # It's also not likely (an eng AND their reviewer would have to miss two identical lines next to each other)
        # And it's not insidious (would be easy to find and verify if we suspected it was happening)
        # So it's not worth complicating the code to check for IMO
        for ranker in experiment.rankers:
            # TODO: Make this work for rankers that take data in addition to the unranked items
            ranked_items = ranker(unranked_items)

        return ranked_items


    
