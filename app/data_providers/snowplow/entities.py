from typing import Dict

from aio_snowplow_tracker import SelfDescribingJson

from app.data_providers.util import get_dict_without_none
from app.models.api_client import ApiClient
from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.unleash_assignment import UnleashAssignmentModel
from app.models.request_user import RequestUser


def get_object_update_event(schema: str, object: str, trigger: str) -> SelfDescribingJson:
    """
    :param schema: Versioned Snowplow schema URI
    :param object: Describes _what_ is being updated. `object_update` contains an enum with allows values.
    :param trigger: Describes _why_ the object is updated. String is not validated. The convention is to use snake case.
    :return: Can be passed to 'event_json' of track_self_describing_event to emit an object_update event.
    """
    return SelfDescribingJson(schema=schema, data={'object': object, 'trigger': trigger})


def get_user_entity(schema: str, user: RequestUser) -> SelfDescribingJson:
    """
    :param schema: Versioned Snowplow schema URI
    :param user:
    :return: Snowplow user entity
    """
    data = {
        'user_id': user.user_id,
        'hashed_user_id': user.hashed_user_id,
        'guid': user.guid,
        'hashed_guid': user.hashed_guid,
    }

    return SelfDescribingJson(schema=schema, data=get_dict_without_none(data))


def get_api_user_entity(schema: str, api_client: ApiClient) -> SelfDescribingJson:
    """
    :param schema: Versioned Snowplow schema URI
    :param api_client:
    :return: Snowplow api_user entity (a.k.a. 'api client')
    """
    data = {
        'api_id': int(api_client.api_id),
        'name': api_client.application_name,
        'is_native': api_client.is_native,
        'is_trusted': api_client.is_trusted,
    }

    return SelfDescribingJson(schema=schema, data=get_dict_without_none(data))


def get_api_user_entity(schema: str, api_client: ApiClient) -> SelfDescribingJson:
    """
    :param schema: Versioned Snowplow schema URI
    :param api_client:
    :return: Snowplow api_user entity (a.k.a. 'api client')
    """
    data = {
        'api_id': int(api_client.api_id),
        'name': api_client.application_name,
        'is_native': api_client.is_native,
        'is_trusted': api_client.is_trusted,
    }

    data_without_none = {k: v for k, v in data.items() if v is not None}

    return SelfDescribingJson(schema=schema, data=data_without_none)


def get_corpus_slate_data(corpus_slate: CorpusSlateModel) -> Dict:
    """
    :param corpus_slate:
    :return: Snowplow corpus_slate entity data
    """
    return {
        'corpus_slate_id': corpus_slate.id,
        'recommended_at': int(corpus_slate.recommended_at.timestamp()),
        'corpus_slate_configuration_id': corpus_slate.configuration_id,
        'recommendations': [
            {
                'corpus_recommendation_id': recommendation.id,
                'corpus_item': {
                    'corpus_item_id': recommendation.corpus_item.id,
                }
            }
            for recommendation in corpus_slate.recommendations
        ]
    }


def get_corpus_slate_entity(schema: str, corpus_slate: CorpusSlateModel) -> SelfDescribingJson:
    """
    :param schema: Versioned Snowplow schema URI
    :param corpus_slate:
    :return: Snowplow corpus_slate entity
    """
    return SelfDescribingJson(schema=schema, data=get_corpus_slate_data(corpus_slate))


def get_corpus_slate_lineup_entity(schema: str, corpus_slate_lineup: CorpusSlateLineupModel) -> SelfDescribingJson:
    """
    :param schema: Versioned Snowplow schema URI
    :param corpus_slate_lineup:
    :return: Snowplow corpus_slate_lineup entity
    """
    return SelfDescribingJson(
        schema=schema,
        data={
            'corpus_slate_lineup_id': corpus_slate_lineup.id,
            'recommended_at': int(corpus_slate_lineup.recommended_at.timestamp()),
            'recommendation_surface_id': corpus_slate_lineup.recommendation_surface_id.value,
            'slates': [get_corpus_slate_data(corpus_slate) for corpus_slate in corpus_slate_lineup.slates]
        },
    )


def get_feature_flag_entity(schema: str, assignment: UnleashAssignmentModel) -> SelfDescribingJson:
    """
    :param schema: Versioned Snowplow schema URI
    :param assignment: Unleash assignment a.k.a. 'feature flag'
    :return: Snowplow feature_flag entity
    """
    return SelfDescribingJson(schema=schema, data={
        'name': assignment.name,
        'variant': assignment.variant,
    })
