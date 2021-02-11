from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List, Tuple
from time import perf_counter

from app.models.slate import SlateModel
from app.models.layout_config import LayoutConfigModel
from app.models.layout_experiment import LayoutExperimentModel


class LayoutModel(BaseModel):
    id: str
    requestID: str = None
    experimentID: str = None
    slates: List[SlateModel]

    @staticmethod
    @xray_recorder.capture_async('models_layout_get_layout')
    async def get_layout(layout_id: str) -> 'LayoutModel':
        layout_experiment, slates = await LayoutModel.__get_slates_from_layout(layout_id)

        layout = LayoutModel.parse_obj({
            'id': layout_id,
            'experimentID': layout_experiment.id,
            'slates': []
        })
        layout.slates = slates

        return layout

    @staticmethod
    async def __get_slates_from_layout(layout_id) -> Tuple[LayoutExperimentModel, List[SlateModel]]:
        # get the requested layout from the config using the layout_id
        experiment, slate_configs = LayoutConfigModel.get_slate_configs_from_layout(layout_id)

        return experiment, await SlateModel.get_slates_from_slate_configs(slate_configs)
