import itertools
import random
from asyncio import gather
from typing import Any

from app.data_providers.curation_api_client import CurationAPIClient
from app.data_providers.metrics_client import MetricsClient
from app.data_providers.slate_provider import SlateProvider
from app.models.ranked_corpus_items_instance import RankedCorpusItemsInstance
from snowplow_tracker import Tracker, Emitter, Subject, payload


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
            api_client: CurationAPIClient,
            slate_provider: SlateProvider,
            metrics_client: MetricsClient
    ):
        self.api_client = api_client
        self.slate_provider = slate_provider
        self.metrics_client = metrics_client

    async def get_ranked_corpus_slate(self, slate_id, start_date=None, user_id=None) -> RankedCorpusItemsInstance:
        corpus_slate_schema = self.slate_provider.get(slate_id)

        # Choose an Experiment
        # TODO: Implement weighting
        experiment = random.choice(corpus_slate_schema.experiments)

        # Fetch Corporeal Candidates
        aggregate_corpus_response = await gather(*(
            self.api_client.get_ranked_corpus_slate(corpus_id, start_date, user_id)
            for corpus_id in experiment.eligible_corpora)
        )

        flattened_unranked_items = list(itertools.chain(*aggregate_corpus_response))

        # If no rankers, return the same list in the same order that the corpus api handed us
        ranked_items = flattened_unranked_items

        for ranker in experiment.rankers:
            ranker_kwargs = await self.metrics_client.get_engagement_metrics(ranked_items, ranker)
            ranked_items = ranker(ranked_items, **ranker_kwargs)

        emitter = Emitter("some.uri.apparently")
        subject = Subject.set_user_id(user_id)
        tracker = Tracker(emitter, subject=subject)
        tracker.track(
            pb=payload.Payload().add_json(dict_={
                "recommendation_id": "UUID",
                "user_id": "Int",
                "items": [
                    {
                        "recommendation_item_id": "UUID",
                        "scheduled_corpus_item_id": "UUID"
                    }
                ],
            })
        )
        tracker.track(
            pb=payload.Payload().add_json(dict_={
                "scheduled_corpus_item_id": "UUID",
                "corpus_item_id": "UUID",
                "date": "String"
            })
        )
        tracker.track(
            pb=payload.Payload().add_json(dict_={
                "corpus_item_id": "UUID",
                "url": "String"
            })
        )

        return RankedCorpusItemsInstance(
            id=slate_id,
            description=corpus_slate_schema.description,
            corpusItems=ranked_items,
        )



    
