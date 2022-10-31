import asyncio

from aio_snowplow_tracker import Tracker, SelfDescribingJson
from aws_xray_sdk.core import xray_recorder

from app.data_providers.snowplow.config import SnowplowConfig
from app.data_providers.snowplow.entities import (
    get_corpus_slate_lineup_entity,
    get_object_update_event,
    get_user_entity, get_feature_flag_entity, get_api_user_entity,
)
from app.data_providers.snowplow.subject import get_subject
from app.models.api_client import ApiClient
from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel
from app.models.unleash_assignment import UnleashAssignmentModel
from app.models.request_user import RequestUser


class SnowplowCorpusSlateLineupTracker:
    """
    Implements tracking the recommendation of a CorpusSlateLineup in SnowPlow, with the goal of tracking any metadata
    for a CorpusRecommendation that we are interested in. Clients will only emit `CorpusRecommendation.id` in events.
    """

    def __init__(self, tracker: Tracker, snowplow_config: SnowplowConfig):
        self.tracker = tracker
        self.snowplow_config = snowplow_config

    @xray_recorder.capture_async('SnowplowCorpusSlateLineupTracker.track')
    async def track(self, corpus_slate_lineup: CorpusSlateLineupModel, user: RequestUser, api_client: ApiClient):
        """
        Track the recommendation of a CorpusSlateLineup in Snowplow.
        :param corpus_slate_lineup: The slate lineup that was recommended.
        :param user: The user that the slate was recommended to.
        :param api_client: The client that originated the request.
        """
        track_calls = [self.track_recommendation_metadata(corpus_slate_lineup, user=user)]
        if corpus_slate_lineup.experiment:
            track_calls.append(
                self.track_variant_enroll(assignment=corpus_slate_lineup.experiment, user=user, api_client=api_client))

        await asyncio.gather(*track_calls)

    async def track_recommendation_metadata(self, corpus_slate_lineup: CorpusSlateLineupModel, user: RequestUser):
        """
        Track the recommendation of a CorpusSlateLineup in Snowplow.
        :param corpus_slate_lineup: The slate lineup that was recommended.
        :param user: The user that the slate was recommended to.
        """

        context = [
            get_corpus_slate_lineup_entity(self.snowplow_config.CORPUS_SLATE_LINEUP_SCHEMA, corpus_slate_lineup),
            get_user_entity(self.snowplow_config.USER_SCHEMA, user),
        ]

        if corpus_slate_lineup.experiment:
            context.append(
                get_feature_flag_entity(self.snowplow_config.FEATURE_FLAG_SCHEMA, corpus_slate_lineup.experiment))

        await self.tracker.track_self_describing_event(
            event_json=get_object_update_event(
                self.snowplow_config.OBJECT_UPDATE_SCHEMA,
                object='corpus_slate_lineup',
                trigger='corpus_slate_lineup_recommendation'
            ),
            event_subject=get_subject(user),
            context=context,
        )

    async def track_variant_enroll(self, assignment: UnleashAssignmentModel, user: RequestUser, api_client: ApiClient):
        """
        Track that the user was enrolled in an experiment.
        :param assignment: The experiment that the user was enrolled in.
        :param user: The user that the slate was recommended to.
        :param api_client: The client that originated the request.
        """
        await self.tracker.track_self_describing_event(
            event_json=SelfDescribingJson(schema=self.snowplow_config.VARIANT_ENROLL_SCHEMA, data={}),
            event_subject=get_subject(user),
            context=[
                get_feature_flag_entity(self.snowplow_config.FEATURE_FLAG_SCHEMA, assignment),
                get_user_entity(self.snowplow_config.USER_SCHEMA, user),
                get_api_user_entity(self.snowplow_config.API_USER_SCHEMA, api_client),
            ],
        )
