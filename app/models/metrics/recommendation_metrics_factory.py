from typing import List, Dict


import app.config
from app.models.metrics.metrics_model import MetricsModel
from app.models.metrics.abstract_metrics_factory import AbstractMetricsFactory


class RecommendationMetricsFactory(AbstractMetricsFactory):
    _dynamodb_table: str = app.config.dynamodb['recommendation_metrics']['table']
    _primary_key_name: str = app.config.dynamodb['recommendation_metrics']['pk']

    # TODO: Replace with OT. 'models.metrics.RecommendationMetricsModel.get')
    async def get(self, slate_id: str, item_ids: List[str]) -> Dict[str, 'MetricsModel']:
        """
        Get metrics for item recommendations in the given slate.

        :param item_ids:
        :type slate_id:
        """
        return await super().get(slate_id, item_ids)
