from aws_xray_sdk.core import xray_recorder
from aio_snowplow_tracker import Tracker, Subject, SelfDescribingJson

from app.data_providers.snowplow.config import SnowplowConfig
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
            data={
                'corpus_slate_lineup_id': corpus_slate_lineup.id,
                'recommended_at': int(corpus_slate_lineup.recommended_at.timestamp()),
                'recommendation_surface_id': 'HOME',  # TODO: Get this value as an argument.
                'slates': [
                    # TODO: Reuse logic from _get_corpus_slate_entity
                    {
                        'corpus_slate_id': corpus_slate.id,
                        'recommended_at': int(corpus_slate.recommended_at.timestamp()),
                        'corpus_slate_configuration_id': '92af3dae-25c9-46c3-bf05-18082aacc7e1',  # TODO: Replace dummy
                        'recommendations': [
                            {
                                'corpus_recommendation_id': recommendation.id,
                                'corpus_item': {
                                    'corpus_item_id': recommendation.corpus_item.id,
                                }
                            }
                            for recommendation in corpus_slate.recommendations
                        ]
                    } for corpus_slate in corpus_slate_lineup.slates
                ]
            }
        )

    def _get_user_entity(self, user: UserIds) -> SelfDescribingJson:
        user_entity = {k: v for k, v in user.dict().items() if v is not None}

        return SelfDescribingJson(
            schema=self.snowplow_config.USER_SCHEMA,
            data=user_entity,
        )
