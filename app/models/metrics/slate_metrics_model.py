from aws_xray_sdk.core import xray_recorder
from typing import List, Dict

import app.config

from app.models.metrics.base_model import MetricsBaseModel


class SlateMetricsModel(MetricsBaseModel):
    _dynamodb_table: str = app.config.dynamodb['slate_metrics']['table']
    _primary_key_name: str = app.config.dynamodb['slate_metrics']['pk']

    @xray_recorder.capture_async('models.metrics.SlateMetricsModel.get')
    async def get(self, slate_lineup_id: str, slate_ids: List[str]) -> Dict[str, 'MetricsBaseModel']:
        """
        Get aggregated metrics for slates in a given lineup.

        :param slate_lineup_id:
        :param slate_ids:
        """
        return await super().get(slate_lineup_id, slate_ids)
