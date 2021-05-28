from typing import List, Dict

from aws_xray_sdk.core import xray_recorder

import app.config
from app.models.metrics.base_model import MetricsBaseModel


class RecommendationMetricsModel(MetricsBaseModel):
    _dynamodb_table: str = app.config.dynamodb['recommendation_metrics']['table']
    _primary_key_name: str = app.config.dynamodb['recommendation_metrics']['pk']

    @xray_recorder.capture_async('models.metrics.RecommendationMetricsModel.get')
    async def get(self, slate_id: str, item_ids: List[str]) -> Dict[str, 'MetricsBaseModel']:
        """
        Get metrics for item recommendations in the given slate.

        :param item_ids:
        :type slate_id:
        """
        return await super().get(slate_id, item_ids)
