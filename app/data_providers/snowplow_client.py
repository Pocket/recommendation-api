import uuid
from abc import ABC

from snowplow_tracker import Emitter, Tracker, payload, SelfDescribingJson
import os

from app.graphql.corpus_item import CorpusItem


class SnowplowFetchable(ABC):
    async def log_event(self, user_id: int, items: [CorpusItem]) -> None:
        return NotImplemented


class SnowplowClient(SnowplowFetchable):
    def __init__(self, tracker=None):
        emitter = Emitter(endpoint=os.getenv("SNOWPLOW_URI_DEV"), protocol='https')
        self.tracker = tracker if tracker else Tracker(emitter, app_id="recs-api")

    async def log_event(
            self,
            slate_id: str,
            # I am assigning zero to "the null value user id" because according to the spec this has to be an int
            user_id: int = 0,
            items: [CorpusItem] = []
    ) -> None:
        self.tracker.track_self_describing_event(
            context=[SelfDescribingJson(
                'iglu:com.pocket/recommendation_result/jsonschema/1-0-0',
                await self.recommendation_result_snowplow_dict(items, slate_id))],
            event_json=SelfDescribingJson(
                'iglu:com.pocket/object_update/jsonschema/1-0-6',
                {
                    "trigger": 'result_recommended',
                    "object": 'recommendation_result'
                }))

        for corpus_item in items:
            self.tracker.track_self_describing_event(
                context=[SelfDescribingJson(
                    'iglu:com.pocket/tile_recommendation_mapping/jsonschema/1-0-0',
                    await self.tile_recommendation_mapping_dict(corpus_item, slate_id))],
                event_json=SelfDescribingJson(
                    'iglu:com.pocket/object_update/jsonschema/1-0-6',
                    {
                        "trigger": 'result_recommended',
                        "object": 'tile_recommendation_mapping'
                    }))
        self.tracker.flush()

    async def tile_recommendation_mapping_dict(self, corpus_item, slate_id):
        return {
            "tile_id": "Blocked on Info",
            "scheduled_corpus_item_external_id": corpus_item.id,
            "slate_id": slate_id,
            "slate_experiment_id": None,  # A null value for now
            "url": corpus_item.id  # For corpus items, the ID is a url
        }

    async def recommendation_result_snowplow_dict(self, items, slate_id):
        return {
            "recommendation_result_id": str(uuid.uuid4()),
            "slate_id": slate_id,
            "slate_experiment_id": None,  # A null value for now
            "recommendation_result_items": [
                {
                    "recommendation_item_id": str(uuid.uuid4()),
                    "scheduled_corpus_item_id": corpus_item.id,
                } for corpus_item in items
            ]
        }
