from abc import ABC
from typing import Any

from snowplow_tracker import Emitter, Tracker, payload
import os

class SnowplowFetchable(ABC):
    async def log_event(self, user_id: int, items: [Any]) -> None:
        return NotImplemented

class SnowplowClient(SnowplowFetchable):
    def __init__(self, tracker):
        emitter = Emitter(os.getenv("SNOWPLOW_URI"))
        self.tracker = tracker if tracker else Tracker(emitter)

    async def log_event(self, user_id: int, items: [Any]) -> None:
        tracking_payload = payload.Payload()
        tracking_payload.add_json(dict_={
            "recommendation_id": "UUID",  # Generated literally here. Like uuid.uuid()
            "slate_experiment_id": "UUID",  # possibly a null value for now
            "user_id": int(user_id),
            "items": [
                {
                    "recommendation_item_id": "UUID",  # Generated literally here. Like uuid.uuid()
                    "scheduled_corpus_item_id": "UUID"  # this comes straight from curation tools api on each item
                }
            ],
        },
            encode_base64=False,
            type_when_encoded="encoded_recs_api_recommendations",
            type_when_not_encoded="recs_api_recommendations"
        )

        self.tracker.track(pb=tracking_payload)
