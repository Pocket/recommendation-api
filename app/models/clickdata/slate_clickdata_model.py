from aws_xray_sdk.core import xray_recorder
from typing import List, Dict

import app.config

from app.models.clickdata.base_model import ClickdataBaseModel


class SlateClickdataModel(ClickdataBaseModel):
    _dynamodb_table: str = app.config.dynamodb['slate_clickdata']['table']
    _primary_key_name: str = app.config.dynamodb['slate_clickdata']['pk']

    @xray_recorder.capture_async('models.SlateClickdataModel.get')
    async def get(self, lineup_id: str, slate_ids: List[str]) -> Dict[str, 'ClickdataBaseModel']:
        """
        Get aggregated clickdata for slates in a given lineup.

        :param lineup_id:
        :param slate_ids:
        """
        return await super().get(lineup_id, slate_ids)
