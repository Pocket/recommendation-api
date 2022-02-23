import uuid
from abc import ABC

from snowplow_tracker import Emitter, Tracker, payload
import os

from app.graphql.corpus_item import CorpusItem


class SnowplowFetchable(ABC):
    async def log_event(self, user_id: int, items: [CorpusItem]) -> None:
        return NotImplemented

class SnowplowClient(SnowplowFetchable):
    def __init__(self, tracker=None):
        emitter = Emitter(os.getenv("SNOWPLOW_URI"))
        self.tracker = tracker if tracker else Tracker(emitter)

    async def log_event(
            self,
            user_id: int = 0, # I am assigning zero to "the null value user id" because according to the spec this has to be an int
            items: [CorpusItem]=[]
    ) -> None:
        tracking_payload = payload.Payload()
        tracking_payload.add_json(dict_={
            "recommendation_id": str(uuid.uuid4()),
            "slate_experiment_id": None,  # A null value for now
            "user_id": user_id,
            "items": [
                {
                    "recommendation_item_id": str(uuid.uuid4()),
                    "scheduled_corpus_item_id": item.id,
                } for item in items
            ],
        },
            encode_base64=False,
            type_when_encoded="encoded_recs_api_recommendations",
            type_when_not_encoded="recs_api_recommendations"
        )

        self.tracker.track(pb=tracking_payload)
