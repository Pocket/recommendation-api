from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List
from app.models.recommendation import RecommendationModel


class SlateModel(BaseModel):
    id: str
    requestID: str = None
    experimentID: str = None
    pageviewGUID: str = None
    display_name: str = None
    description: str = None
    recommendations: List[RecommendationModel]

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_slate')
    async def get_slate(slate_id: str) -> ['SlateModel']:
        return SlateModel.parse_obj({
            'id': slate_id,
            'requestID': '1',
            'experimentID': '1',
            'pageviewGUID': '1',
            'display_name': 'Fake slate',
            'recommendations': [{
                'feed_item_id': '1',
                'item_id': '1',
                'feed_id': '1',
                'rec_src': 'RecommendationAPI',
                'publisher': 'Fake Times'
            }],
        })
