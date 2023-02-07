from typing import List, Dict


import app.config
from app.models.metrics.metrics_model import MetricsModel
from app.models.metrics.abstract_metrics_factory import AbstractMetricsFactory


class SlateMetricsFactory(AbstractMetricsFactory):
    _dynamodb_table: str = app.config.dynamodb['slate_metrics']['table']
    _primary_key_name: str = app.config.dynamodb['slate_metrics']['pk']

    # TODO: Replace with OT. 'models.metrics.SlateMetricsModel.get')
    async def get(self, slate_lineup_id: str, slate_ids: List[str]) -> Dict[str, 'MetricsModel']:
        """
        Get aggregated metrics for slates in a given lineup.

        :param slate_lineup_id:
        :param slate_ids:
        """
        return await super().get(slate_lineup_id, slate_ids)
