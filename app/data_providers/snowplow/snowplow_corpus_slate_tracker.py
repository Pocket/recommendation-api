from typing import Optional

from aws_xray_sdk.core import xray_recorder
from snowplow_tracker import Tracker, Subject, SelfDescribingJson

from app.data_providers.snowplow.config import SnowplowConfig
from app.models.corpus_slate_model import CorpusSlateModel


class SnowplowCorpusSlateTracker:
    """
    Implements tracking the recommendation of a CorpusSlate in SnowPlow, with the goal of tracking any metadata that
    to CorpusRecommendation.id that we are interested in. Clients will only emit the CorpusRecommendation id in events.
    """

    def __init__(self, tracker: Tracker, snowplow_config: SnowplowConfig):
        self.tracker = tracker
        self.snowplow_config = snowplow_config

    @xray_recorder.capture_async('data_providers.SnowplowCorpusSlateTracker.track')
    async def track(self, corpus_slate: CorpusSlateModel, user_id: str):
        # NOTE: This blocks the eventloop. I could not find any asyncio Snowplow tracker.
        self.tracker.track_self_describing_event(
            event_json=self._get_object_update_event(object='corpus_slate', trigger='corpus_slate_recommendation'),
            event_subject=self._get_subject(user_id),
            context=[
                self._get_corpus_slate_entity(corpus_slate),
                self._get_user_entity(user_id),
            ],
        )

    def _get_subject(self, user_id: Optional[str]):
        return Subject().set_user_id(user_id)

    def _get_object_update_event(self, object: str, trigger: str) -> SelfDescribingJson:
        return SelfDescribingJson(
            schema=self.snowplow_config.OBJECT_UPDATE_SCHEMA,
            data={'object': object, 'trigger': trigger}
        )

    def _get_corpus_slate_entity(self, corpus_slate: CorpusSlateModel) -> SelfDescribingJson:
        return SelfDescribingJson(
            schema=self.snowplow_config.CORPUS_SLATE_SCHEMA,
            data={
                'id': corpus_slate.id,
                'recommendations': [
                    {
                        'id': recommendation.id,
                        'corpus_item': {
                            'id': recommendation.corpus_item.id,
                        }
                    }
                    for recommendation in corpus_slate.recommendations
                ]
            }
        )

    def _get_user_entity(self, user_id: str) -> SelfDescribingJson:
        return SelfDescribingJson(
            schema=self.snowplow_config.USER_SCHEMA,
            data={
                'user_id': int(user_id),
            }
        )
