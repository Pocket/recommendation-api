from typing import Dict

from aio_snowplow_tracker import SelfDescribingJson

from app.data_providers.util import get_dict_without_none
from app.models.api_client import ApiClient
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_recommendations_send_event import CorpusRecommendationsSendEvent
from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.request_user import RequestUser
from app.models.unleash_assignment import UnleashAssignmentModel

_CORPUS_RECOMMENDATIONS_SEND_SCHEMA = 'iglu:com.pocket/corpus_recommendations_send/jsonschema/1-0-0'
_CORPUS_SLATE_SCHEMA = 'iglu:com.pocket/corpus_slate/jsonschema/4-0-0'
_CORPUS_SLATE_LINEUP_SCHEMA = 'iglu:com.pocket/corpus_slate_lineup/jsonschema/3-0-0'
_USER_SCHEMA = 'iglu:com.pocket/user/jsonschema/1-0-0'
_FEATURE_FLAG_SCHEMA = 'iglu:com.pocket/feature_flag/jsonschema/1-0-0'
_VARIANT_ENROLL_SCHEMA = 'iglu:com.pocket/variant_enroll/jsonschema/1-0-0'
_API_USER_SCHEMA = 'iglu:com.pocket/api_user/jsonschema/1-0-1'


def get_corpus_recommendations_send_event(event: CorpusRecommendationsSendEvent) -> SelfDescribingJson:
    """
    :return: Snowplow corpus_recommendations_send event, that is emitted with recommendation metadata when recommending
             a CorpusSlate or CorpusSlateLineup.
    """
    return SelfDescribingJson(schema=_CORPUS_RECOMMENDATIONS_SEND_SCHEMA, data={
        'recommended_at': int(event.recommended_at.timestamp()),
        'recommendation_surface_id': event.recommendation_surface_id.value,
        'locale': event.locale.value,
    })


def get_variant_enroll_event():
    """
    :return: Snowplow event used to track when users are enrolled in an experiment. Needed for the Mode Experiment
             Reports.
    """
    return SelfDescribingJson(schema=_VARIANT_ENROLL_SCHEMA, data={})


def get_user_entity(user: RequestUser) -> SelfDescribingJson:
    """
    :param user: Logged-in or logged-out user of Pocket
    :return: Snowplow user entity
    """
    return SelfDescribingJson(schema=_USER_SCHEMA, data=get_dict_without_none({
        'user_id': user.user_id,
        'hashed_user_id': user.hashed_user_id,
        'guid': user.guid,
        'hashed_guid': user.hashed_guid,
    }))


def get_api_user_entity(api_client: ApiClient) -> SelfDescribingJson:
    """
    :param api_client: ApiClient identifies the Pocket Client (for example the Web Client) that made the request.
    :return: Snowplow api_user entity (a.k.a. 'api client')
    """
    return SelfDescribingJson(schema=_API_USER_SCHEMA, data=get_dict_without_none({
        'api_id': int(api_client.api_id),
        'name': api_client.application_name,
        'is_native': api_client.is_native,
        'is_trusted': api_client.is_trusted,
    }))


def get_corpus_slate_entity(corpus_slate: CorpusSlateModel) -> SelfDescribingJson:
    return SelfDescribingJson(schema=_CORPUS_SLATE_SCHEMA, data={
        'corpus_slate_id': corpus_slate.id,
        'corpus_slate_configuration_id': corpus_slate.configuration_id,
        'recommendations': [_get_corpus_recommendation_data(r) for r in corpus_slate.recommendations]
    })


def _get_corpus_recommendation_data(recommendation: CorpusRecommendationModel) -> Dict:
    """
    :return: Dict with attributes that the corpus_slate entity expects for each CorpusRecommendation.
    """
    data = {
        'corpus_recommendation_id': recommendation.id,
        'corpus_item': {
            'corpus_item_id': recommendation.corpus_item.id,
        }
    }

    if recommendation.tile_id:
        data['corpus_recommendation_tile_id'] = recommendation.tile_id

    return data


def get_corpus_slate_lineup_entity(corpus_slate_lineup: CorpusSlateLineupModel) -> SelfDescribingJson:
    return SelfDescribingJson(
        schema=_CORPUS_SLATE_LINEUP_SCHEMA,
        data={
            'corpus_slate_lineup_id': corpus_slate_lineup.id,
            'slates': [{'corpus_slate_id': corpus_slate.id} for corpus_slate in corpus_slate_lineup.slates]
        },
    )


def get_feature_flag_entity(assignment: UnleashAssignmentModel) -> SelfDescribingJson:
    """
    :param assignment: Unleash assignment a.k.a. 'feature flag'
    :return: Snowplow feature_flag entity
    """
    return SelfDescribingJson(schema=_FEATURE_FLAG_SCHEMA, data={
        'name': assignment.name,
        'variant': assignment.variant,
    })
