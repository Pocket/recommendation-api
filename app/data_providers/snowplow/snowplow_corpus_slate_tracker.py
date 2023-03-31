from aio_snowplow_tracker import Tracker
from opentelemetry import trace

from app.data_providers.snowplow.config import SnowplowConfig
from app.data_providers.snowplow.entities import (
    get_corpus_slate_entity,
    get_object_update_event,
    get_user_entity,
)
from app.data_providers.snowplow.subject import get_subject
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.request_user import RequestUser


class SnowplowCorpusSlateTracker:
    """
    Implements tracking the recommendation of a CorpusSlate in SnowPlow, with the goal of tracking any metadata for a
    CorpusRecommendation that we are interested in. Clients will only emit `CorpusRecommendation.id` in events.
    """

    def __init__(self, tracker: Tracker, snowplow_config: SnowplowConfig):
        self.tracker = tracker
        self.snowplow_config = snowplow_config

    async def track(self, corpus_slate: CorpusSlateModel, user: RequestUser):
        """
        Track the recommendation of a CorpusSlate in Snowplow.
        :param corpus_slate: The slate that was recommended.
        :param user: The user that the slate was recommended to.
        """
        with trace.get_tracer(__name__).start_as_current_span('SnowplowCorpusSlateTracker.track'):
            await self.tracker.track_self_describing_event(
                event_json=get_object_update_event(
                    self.snowplow_config.OBJECT_UPDATE_SCHEMA,
                    object='corpus_slate',
                    trigger='corpus_slate_recommendation'
                ),
                event_subject=get_subject(user),
                context=[
                    get_corpus_slate_entity(self.snowplow_config.CORPUS_SLATE_SCHEMA, corpus_slate),
                    get_user_entity(self.snowplow_config.USER_SCHEMA, user),
                ],
            )
