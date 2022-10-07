from aws_xray_sdk.core import xray_recorder
from aio_snowplow_tracker import Tracker, Subject, SelfDescribingJson

from app.data_providers.snowplow.config import SnowplowConfig
from app.data_providers.snowplow.entities import get_corpus_slate_entity, get_corpus_slate_lineup_entity
from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.user_ids import UserIds


class SnowplowCorpusSlateLineupTracker:
    """
    Implements tracking the recommendation of a CorpusSlate in SnowPlow, with the goal of tracking any metadata for a
    CorpusRecommendation that we are interested in. Clients will only emit `CorpusRecommendation.id` in events.
    """

    def __init__(self, tracker: Tracker, snowplow_config: SnowplowConfig):
        self.tracker = tracker
        self.snowplow_config = snowplow_config

    @xray_recorder.capture_async('data_providers.SnowplowCorpusSlateTracker.track')
    async def track(self, corpus_slate_lineup: CorpusSlateLineupModel, user: UserIds):
        """
        Track the recommendation of a CorpusSlateLineup in Snowplow.
        :param corpus_slate_lineup: The slate lineup that was recommended.
        :param user: The user that the slate was recommended to.
        """
        await self.tracker.track_self_describing_event(
            event_json=self._get_object_update_event(object='corpus_slate', trigger='corpus_slate_recommendation'),
            event_subject=self._get_subject(user),
            context=[
                self._get_corpus_slate_lineup_entity(corpus_slate_lineup),
                self._get_user_entity(user),
            ],
        )

    def _get_subject(self, user: UserIds):
        return Subject().set_user_id(str(user.user_id))

    def _get_object_update_event(self, object: str, trigger: str) -> SelfDescribingJson:
        return SelfDescribingJson(
            schema=self.snowplow_config.OBJECT_UPDATE_SCHEMA,
            data={'object': object, 'trigger': trigger}
        )

    def _get_corpus_slate_lineup_entity(self, corpus_slate_lineup: CorpusSlateLineupModel) -> SelfDescribingJson:
        return SelfDescribingJson(
            schema=self.snowplow_config.CORPUS_SLATE_LINEUP_SCHEMA,
            data=get_corpus_slate_lineup_entity(corpus_slate_lineup),
        )

    def _get_user_entity(self, user: UserIds) -> SelfDescribingJson:
        user_entity = {k: v for k, v in user.dict().items() if v is not None}

        return SelfDescribingJson(
            schema=self.snowplow_config.USER_SCHEMA,
            data=user_entity,
        )
