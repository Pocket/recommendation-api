from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List
from app.models.slate import SlateModel


class LayoutModel(BaseModel):
    id: str
    name: str = None
    requestID: str = None
    experimentID: str = None
    slates: List[SlateModel]

    @staticmethod
    @xray_recorder.capture_async('models_layout_get_layout')
    async def get_layout(layout_id: str) -> 'LayoutModel':
        # TODO: pull this out of dynamodb
        layout = LayoutModel.parse_obj({
            'id': layout_id,
            'requestID': '1',
            'experimentID': '1',
            'pageviewGUID': '1',
            'display_name': 'Fake slate',
            'slates': []
        })
        layout.slates = [SlateModel.get_slate(slate_id='1234')]
        return layout
