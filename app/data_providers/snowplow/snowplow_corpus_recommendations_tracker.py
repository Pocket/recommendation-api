import asyncio

from aio_snowplow_tracker import Tracker
from opentelemetry import trace

from app.data_providers.snowplow.config import SnowplowConfig
from app.data_providers.snowplow.entities import (
    get_corpus_slate_lineup_entity,
    get_user_entity, get_feature_flag_entity, get_api_user_entity, get_corpus_slate_entity,
    get_corpus_recommendations_send_event, get_variant_enroll_event,
)
from app.data_providers.snowplow.subject import get_subject
from app.models.api_client import ApiClient
from app.models.corpus_recommendations_send_event import CorpusRecommendationsSendEvent
from app.models.unleash_assignment import UnleashAssignmentModel
from app.models.request_user import RequestUser


class SnowplowCorpusRecommendationsTracker:
    """
    Implements tracking the recommendation of a CorpusSlate or CorpusSlateLineup in SnowPlow, with the goal of tracking
    any metadata for a CorpusRecommendation that we are interested in. Clients will only emit `CorpusRecommendation.id`
    in events.
    """

    def __init__(self, tracker: Tracker, snowplow_config: SnowplowConfig):
        self.tracker = tracker
        self.snowplow_config = snowplow_config

    async def track(self, event: CorpusRecommendationsSendEvent):
        """
        Track the recommendation of a CorpusSlate or CorpusSlateLineup in Snowplow.
        :param event: Context for the slate or slate lineup being recommended to the client.
        """
        with trace.get_tracer(__name__).start_as_current_span('SnowplowCorpusRecommendationsTracker.track'):
            track_calls = [self.track_corpus_recommendations_event_send(event)]
            if event.experiment:
                track_calls.append(
                    self.track_variant_enroll(assignment=event.experiment, user=event.user, api_client=event.api_client)
                )

            await asyncio.gather(*track_calls)

    async def track_corpus_recommendations_event_send(self, event: CorpusRecommendationsSendEvent):
        """
        Track the recommendation of a CorpusSlate or CorpusSlateLineup in Snowplow.
        :param event: Context for the slate or slate lineup being recommended to the client.
        """
        context = []

        if event.corpus_slate_lineup:
            context.append(get_corpus_slate_lineup_entity(event.corpus_slate_lineup))
            context += [get_corpus_slate_entity(slate) for slate in event.corpus_slate_lineup.slates]
        elif event.corpus_slate:
            context.append(get_corpus_slate_entity(event.corpus_slate))
        else:
            raise ValueError("Can't emit a corpus_recommendation_send without corpus_slate_lineup or corpus_slate.")

        if event.user:
            context.append(get_user_entity(event.user))

        if event.experiment:
            context.append(get_feature_flag_entity(event.experiment))

        if event.api_client:
            context.append(get_api_user_entity(event.api_client))

        await self.tracker.track_self_describing_event(
            event_json=get_corpus_recommendations_send_event(event=event),
            event_subject=get_subject(event.user) if event.user else None,
            context=context,
        )

    async def track_variant_enroll(self, assignment: UnleashAssignmentModel, user: RequestUser, api_client: ApiClient):
        """
        Track that the user was enrolled in an experiment.
        :param assignment: The experiment that the user was enrolled in.
        :param user: The user that the slate was recommended to.
        :param api_client: The client that originated the request.
        """
        context = [
            get_feature_flag_entity(assignment),
        ]
        if user:
            context.append(get_user_entity(user))

        if api_client:
            context.append(get_api_user_entity(api_client))
        await self.tracker.track_self_describing_event(
            event_json=get_variant_enroll_event(),
            event_subject=get_subject(user) if user else None,
            context=context,
        )
