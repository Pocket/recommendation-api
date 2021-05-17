from typing import List, Dict

from aws_xray_sdk.core import xray_recorder

import app.config
from app.models.clickdata.base_model import ClickdataBaseModel


class RecommendationClickdataModel(ClickdataBaseModel):
    _dynamodb_table: str = app.config.dynamodb['recommendation_clickdata']['table']
    _primary_key_name: str = app.config.dynamodb['recommendation_clickdata']['pk']

    @xray_recorder.capture_async('models.ClickdataModel.get')
    async def get(self, slate_id: str, item_ids: List[str]) -> Dict[str, 'ClickdataBaseModel']:
        """
        Get clickdata for item recommendations in the given slate.

        :param item_ids:
        :type slate_id:
        """
        return await super().get(slate_id, item_ids)
