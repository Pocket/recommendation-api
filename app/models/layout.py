import uuid

from aws_xray_sdk.core import xray_recorder
from pydantic import BaseModel
from typing import List

from app.models.layout_config import LayoutConfigModel
from app.models.layout_experiment import LayoutExperimentModel
from app.models.slate import SlateModel


class LayoutModel(BaseModel):
    """
    Models a layout.
    """
    id: str
    requestID: str = None
    experimentID: str = None
    slates: List[SlateModel]

    @staticmethod
    @xray_recorder.capture_async('models_layout_get_layout')
    async def get_layout(layout_id: str, user_id: str = None) -> 'LayoutModel':
        """
        Retrieves a layout based on the given `layout_id`

        :param layout_id: string id of the layout
        :param user_id: string user id (reserved for future use)
        :return: LayoutModel object
        """
        experiment = LayoutConfigModel.get_experiment_from_layout(layout_id)
        slates = await LayoutModel.__get_slates_from_experiment(experiment)

        return LayoutModel(
            id=layout_id,
            experimentID=experiment.id,
            slates=slates,
            requestID=str(uuid.uuid4()),
        )

    @staticmethod
    async def __get_slates_from_experiment(experiment: LayoutExperimentModel) -> List[SlateModel]:
        """
        Retrieves an experiment ID and a list of SlateModel objects

        :param experiment: a LayoutExperiment object
        :return: a list of SlateModel objects
        """
        # get the requested layout from the config using the layout_id
        slate_configs = LayoutConfigModel.get_slate_configs_from_experiment(experiment)

        return await SlateModel.get_slates_from_slate_configs(slate_configs)
