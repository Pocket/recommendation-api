from typing import Dict, List

from app.models.metrics.firefox_new_tab_metrics_model import FirefoxNewTabMetricsModel
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


def _get_firefox_new_tab_metrics_model(**kwargs) -> 'FirefoxNewTabMetricsModel':
    """
    :param kwargs: override any MetricsModel attributes
    :return: MetricsModel
    """
    default_values = {
        'id': 'home/999',
        'trailing_15_minute_opens': 0,
        'trailing_15_minute_impressions': 0,
        'unloaded_at': '2022-02-02',
        'url': 'http://example.com/999',
        'slate_id': '',
    }
    default_values.update(**kwargs)
    return FirefoxNewTabMetricsModel.parse_obj(default_values)


def _get_metrics_model_dict(**kwargs) -> Dict[str, 'MetricsModel']:
    """
    :param kwargs: override any MetricsModel attributes
    :return: dict with value the MetricsModel and key the second component of the id
    """
    model = _get_metrics_model(**kwargs)
    return {model.id.split('/')[1]: model}


def _get_firefox_new_tab_metrics_model_dict(**kwargs) -> Dict[str, 'FirefoxNewTabMetricsModel']:
    """
    :param kwargs: override any FirefoxNewTabMetricsModel attributes
    :return: dict with value the FirefoxNewTabMetricsModel and key the second component of the id
    """
    model = _get_firefox_new_tab_metrics_model(**kwargs)
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
        metrics.update(_get_metrics_model_dict(**kwargs))

    return metrics


def generate_firefox_metrics(item_ids: List[str], slate_id="1234-0000") -> Dict[str, 'FirefoxNewTabMetricsModel']:
    """
    Generates a dictionary of FirefoxNewTabMetricsModel, mirroring FirefoxNewTabMetricsFactory.get()
    :param item_ids: List of item ids strings.
    :return: Dictionary where values are FirefoxNewTabMetricsModel, with
             - trailing_15_minute_opens equal to the last two digits of the item id
             - trailing_15_minute_impressions being equal to 999
    """
    kwargs_list = [
        {
            "id": f"{slate_id}/{item_id}",
            f"trailing_15_minute_opens": int(item_id[:2]),
            f"trailing_15_minute_impressions": 999,
        } for item_id in item_ids
    ]

    metrics = {}
    for kwargs in kwargs_list:
        metrics.update(_get_firefox_new_tab_metrics_model_dict(**kwargs))

    return metrics
