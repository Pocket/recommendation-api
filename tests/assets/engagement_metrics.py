import datetime
from typing import Dict, List

from app.models.corpus_item_model import CorpusItemModel
from app.models.metrics.corpus_item_engagement_model import CorpusItemEngagementModel
from app.models.metrics.metrics_model import MetricsModel


def _get_metrics_model(**kwargs) -> 'MetricsModel':
    """
    :param kwargs: override any MetricsModel attributes
    :return: MetricsModel
    """
    default_values = {
        'id': 'home/999',
        'trailing_1_day_opens': 0,
        'trailing_1_day_impressions': 0,
        'trailing_7_day_opens': 0,
        'trailing_7_day_impressions': 0,
        'trailing_14_day_opens': 0,
        'trailing_14_day_impressions': 0,
        'trailing_28_day_opens': 0,
        'trailing_28_day_impressions': 0,
        'created_at': 0,
        'expires_at': 0
    }
    default_values.update(**kwargs)
    return MetricsModel.parse_obj(default_values)


def generate_metrics_model_dict(**kwargs) -> Dict[str, 'MetricsModel']:
    """
    :param kwargs: override any MetricsModel attributes
    :return: dict with value the MetricsModel and key the second component of the id
    """
    model = _get_metrics_model(**kwargs)
    return {model.id.split('/')[1]: model}


def generate_metrics(period) -> Dict[str, 'MetricsModel']:
    """
    Generates a dictionary of MetricsModel, mirroring AbstractMetricsFactory.get()
    :param period: Trailing day number to set metrics for: 1, 7, 14, or 28
    :return: Dictionary where values are FirefoxNewTabMetricsModel, with
             - item_id being "999999", "666666", "333333"
             - opens equal to the last two digits of the item id for the given period
             - impressions being equal to 999 for the given period
             - all other opens and impressions are 0
    """
    kwargs_list = [
        {
            "id": f"home/{item_id}",
            f"trailing_{period}_day_opens": int(item_id[:2]),
            f"trailing_{period}_day_impressions": 999,
        } for item_id in ["999999", "666666", "333333"]
    ]

    metrics = {}
    for kwargs in kwargs_list:
        metrics.update(generate_metrics_model_dict(**kwargs))

    return metrics


def generate_corpus_engagement(recommendations: List[CorpusItemModel]) -> Dict[str, 'CorpusItemEngagementModel']:
    """
    :return: Dictionary where keys are recommendation ids, and values are CorpusItemEngagementModel, with
             - trailing_1_day_opens equal to 33 * (i + 1), for the i'th recommendation
             - trailing_1_day_impressions being equal to 999
    """
    return {
        rec.id: CorpusItemEngagementModel(
            key=f'NEW_TAB_EN_US/edc5571f-7adb-537a-afd8-5612155d54da/{rec.id}',
            recommendation_surface_id='NEW_TAB_EN_US',
            corpus_slate_configuration_id='edc5571f-7adb-537a-afd8-5612155d54da',
            corpus_item_id=rec.id,
            trailing_1_day_opens=33 * (index + 1),  # 33, 66, 99, etc.
            trailing_1_day_impressions=999,
            trailing_7_day_opens=0,
            trailing_7_day_impressions=0,
            trailing_14_day_opens=0,
            trailing_14_day_impressions=0,
            trailing_21_day_opens=0,
            trailing_21_day_impressions=0,
            trailing_28_day_opens=0,
            trailing_28_day_impressions=0,
            updated_at=datetime.datetime.now(),
        ) for index, rec in enumerate(recommendations)
    }
