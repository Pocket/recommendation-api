from aio_snowplow_tracker import SelfDescribingJson, Subject

from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.user_ids import UserIds


def get_object_update_event(schema: str, object: str, trigger: str) -> SelfDescribingJson:
    """
    :param schema: Versioned Snowplow schema URI
    :param object: Describes _what_ is being updated. `object_update` contains an enum with allows values.
    :param trigger: Describes _why_ the object is updated. String is not validated. The convention is to use snake case.
    :return: Can be passed to 'event_json' of track_self_describing_event to emit an object_update event.
    """
    return SelfDescribingJson(schema=schema, data={'object': object, 'trigger': trigger})


def get_user_entity(schema: str, user_ids: UserIds) -> SelfDescribingJson:
    """
    :param schema: Versioned Snowplow schema URI
    :param user_ids:
    :return: Snowplow user entity
    """
    user_entity = {k: v for k, v in user_ids.dict().items() if v is not None}

    return SelfDescribingJson(schema=schema, data=user_entity)


def get_corpus_slate_entity(schema: str, corpus_slate: CorpusSlateModel) -> SelfDescribingJson:
    """
    :param schema: Versioned Snowplow schema URI
    :param corpus_slate:
    :return: Snowplow corpus_slate entity
    """
    return SelfDescribingJson(
        schema=schema,
        data={
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
        },
    )


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
            'slates': [get_corpus_slate_entity(corpus_slate) for corpus_slate in corpus_slate_lineup.slates]
        },
    )
