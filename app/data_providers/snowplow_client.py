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
        emitter = Emitter(os.getenv("SNOWPLOW_URI"))
        self.tracker = tracker if tracker else Tracker(emitter)

    async def log_event(
            self,
            user_id: int = 0,
            # I am assigning zero to "the null value user id" because according to the spec this has to be an int
            items: [CorpusItem] = []
    ) -> None:
        tracking_payload = payload.Payload()
        tracking_payload.add_json(dict_={
            "recommendation_id": str(uuid.uuid4()),
            "slate_experiment_id": None,  # A null value for now
            "user_id": user_id,
            "items": [
                {
                    "recommendation_item_id": str(uuid.uuid4()),
                    "scheduled_corpus_item_id": corpus_item.id,
                } for corpus_item in items
            ],
        },
            encode_base64=False,
            type_when_encoded="encoded_recs_api_recommendations",
            type_when_not_encoded="recs_api_recommendations"
        )

        self.tracker.track_self_describing_event(
            event_json=SelfDescribingJson(
                'iglu:com.pocket/scheduled_corpus_item/jsonschema/1-0-1',
                {
                    "object_version": 'new',
                    "scheduled_corpus_item_external_id": '789-xyz',
                    "scheduled_at": 1893456000,
                    "url": 'thisisjonathanandchelseassweeturl.com',
                    "approved_corpus_item_external_id": '123-abc',
                    "scheduled_surface_id": 'NEW_TAB_EN_US',
                    "created_at": 1647372554,
                    "created_by": 'Chelsea',
                    "updated_at": 1647372554,
                    "updated_by": 'Chelsea',
                    "scheduled_surface_name": 'New Tab (en-US)',
                    "scheduled_surface_utc_offset": '-500'
                }
            ),
            context=[SelfDescribingJson(
                'iglu:com.snowplowanalytics.snowplow/unstruct_event/jsonschema/1-0-0',
                {
                    'iglu:com.pocket/object_update/jsonschema/1-0-5',
                    {
                        "trigger": 'scheduled_corpus_item_removed',
                        "object": 'scheduled_corpus_item'
                    }
                }
            )]
        )
