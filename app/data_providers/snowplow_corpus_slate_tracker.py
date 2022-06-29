import os
from abc import ABC
from typing import List, Any, Dict, Optional

from aws_xray_sdk.core import xray_recorder
from snowplow_tracker import Tracker, Subject, SelfDescribingJson, Emitter

from app.models.corpus_slate_model import CorpusSlateModel
from app.config import ENV, ENV_PROD


class CorpusSlateTrackable(ABC):
    """
    Abstract class to track the recommendation of a CorpusSlate.
    """

    async def track(self, corpus_slate: CorpusSlateModel, user_id: Optional[str]):
        return NotImplemented


class SnowplowConfig:
    APP_ID = f'pocket-data-products-recommendation-api-{ENV}'

    PROD_ENDPOINT_URL = 'com-getpocket-prod1.collector.snplow.net'
    DEV_ENDPOINT_URL = 'com-getpocket-prod1.mini.snplow.net'
    ENDPOINT_URL = PROD_ENDPOINT_URL if ENV == ENV_PROD else DEV_ENDPOINT_URL

    CORPUS_SLATE_SCHEMA = 'iglu:com.pocket/corpus_slate/jsonschema/1-0-0'
    USER_SCHEMA = 'iglu:com.pocket/user/jsonschema/1-0-0'
    OBJECT_UPDATE_SCHEMA = 'iglu:com.pocket/object_update/jsonschema/1-0-7'


class SnowplowCorpusSlateTracker(CorpusSlateTrackable):
    """
    Implements tracking the recommendation of a CorpusSlate in SnowPlow, with the goal of tracking any metadata that
    to CorpusRecommendation.id that we are interested in. Clients will only emit the CorpusRecommendation id in events.
    """

    def __init__(self, tracker: Tracker, snowplow_config: SnowplowConfig):
        self.tracker = tracker
        self.snowplow_config = snowplow_config

    @xray_recorder.capture_async('data_providers.SnowplowCorpusSlateTracker.track')
    async def track(self, corpus_slate: CorpusSlateModel, user_id: Optional[str]):
        context = [self._get_corpus_slate_entity(corpus_slate)]

        if user_id is not None:
            context.append(self._get_user_entity(user_id))

        # NOTE: This blocks the eventloop. I could not find any asyncio Snowplow tracker.
        self.tracker.track_self_describing_event(
            event_json=self._get_object_update_event(object='corpus_slate', trigger='corpus_slate_recommendation'),
            context=context,
            event_subject=self._get_subject(user_id),
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


def create_snowplow_tracker() -> Tracker:
    """
    Helper method to instantiate a Snowplow Tracker.
    :return:
    """
    # NOTE: Snowplow has an 'Emitter' and a 'AsyncEmitter'. The latter works with threads, and it still blocks the
    # eventloop. I did not find any implementation of an asyncio Snowplow tracker.
    emitter = Emitter(
        SnowplowConfig.ENDPOINT_URL,
        protocol='https',
    )
    return Tracker(emitter, app_id=SnowplowConfig.APP_ID)
