from typing import Any, Dict

from app.models.corpus_slate_lineup_model import CorpusSlateLineupModel
from app.models.corpus_slate_model import CorpusSlateModel


def get_corpus_slate_entity(corpus_slate: CorpusSlateModel) -> Dict[str, Any]:
    """
    :param corpus_slate:
    :return: Snowplow corpus_slate entity
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


def get_corpus_slate_lineup_entity(corpus_slate_lineup: CorpusSlateLineupModel) -> Dict[str, Any]:
    """
    :param corpus_slate_lineup:
    :return: Snowplow corpus_slate_lineup entity
    """
    return {
        'corpus_slate_lineup_id': corpus_slate_lineup.id,
        'recommended_at': int(corpus_slate_lineup.recommended_at.timestamp()),
        'recommendation_surface_id': 'HOME',  # TODO: Get this value as an argument.
        'slates': [get_corpus_slate_entity(corpus_slate) for corpus_slate in corpus_slate_lineup.slates]
    }
