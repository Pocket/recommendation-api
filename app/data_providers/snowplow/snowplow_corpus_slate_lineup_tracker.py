from aio_snowplow_tracker import Tracker
from aws_xray_sdk.core import xray_recorder

from app.data_providers.snowplow.config import SnowplowConfig
from app.data_providers.snowplow.entities import (
    get_corpus_slate_lineup_entity,
    get_object_update_event,
    get_user_entity,
)
from app.data_providers.snowplow.subject import get_subject
from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel
from app.models.user_ids import UserIds


class SnowplowCorpusSlateLineupTracker:
    """
    Implements tracking the recommendation of a CorpusSlateLineup in SnowPlow, with the goal of tracking any metadata
    for a CorpusRecommendation that we are interested in. Clients will only emit `CorpusRecommendation.id` in events.
    """

    def __init__(self, tracker: Tracker, snowplow_config: SnowplowConfig):
        self.tracker = tracker
        self.snowplow_config = snowplow_config

    @xray_recorder.capture_async('SnowplowCorpusSlateLineupTracker.track')
    async def track(self, corpus_slate_lineup: CorpusSlateLineupModel, user: UserIds):
        """
        Track the recommendation of a CorpusSlateLineup in Snowplow.
        :param corpus_slate_lineup: The slate lineup that was recommended.
        :param user: The user that the slate was recommended to.
        """
        await self.tracker.track_self_describing_event(
            event_json=get_object_update_event(
                self.snowplow_config.OBJECT_UPDATE_SCHEMA,
                object='corpus_slate_lineup',
                trigger='corpus_slate_lineup_recommendation'
            ),
            event_subject=get_subject(user),
            context=[
                get_corpus_slate_lineup_entity(self.snowplow_config.CORPUS_SLATE_LINEUP_SCHEMA, corpus_slate_lineup),
                get_user_entity(self.snowplow_config.USER_SCHEMA, user),
            ],
        )
