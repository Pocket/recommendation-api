import random

from aws_xray_sdk.core import xray_recorder
from pydantic import BaseModel
from typing import List

from app.models.slate_experiment import SlateExperimentModel
from app.models.recommendation import RecommendationModel
from app.models.slate_config import SlateConfigModel
from asyncio import gather


class SlateModel(BaseModel):
    id: str
    requestID: str = None
    experimentID: str = None
    pageviewGUID: str = None
    display_name: str = None
    description: str = None
    recommendations: List[RecommendationModel] = None

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_slate')
    async def get_slate(slate_id: str) -> 'SlateModel':
        slate_config = SlateConfigModel.find_by_id(slate_id)
        return await SlateModel.__get_slate_from_slate_config(slate_config)

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_all')
    async def get_all() -> ['SlateModel']:
        slate_configs = SlateConfigModel.SLATE_CONFIGS_BY_ID.values()
        return await SlateModel.get_slates_from_slate_configs(slate_configs, with_recs=False)

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_slates_from_slate_configs')
    async def get_slates_from_slate_configs(slate_configs: List['SlateConfigModel'],
                                            with_recs: bool = True) -> ['SlateModel']:
        slate_models = []
        # for each slate, get random experiment
        for slate_config in slate_configs:
            slate_model = SlateModel.__get_slate_from_slate_config(slate_config, with_recs=with_recs)
            slate_models.append(slate_model)

        slate_models = await gather(*slate_models)
        return slate_models

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_slate_from_slate_config')
    async def __get_slate_from_slate_config(slate_config: 'SlateConfigModel', with_recs: bool = True) -> 'SlateModel':
        if with_recs:
            experiment = SlateExperimentModel.choose_experiment(slate_config.experiments)
            recommendations = await RecommendationModel.get_recommendations_from_experiment(experiment)
        else:
            experiment = None
            recommendations = []

        return SlateModel(
            id=slate_config.id,
            experimentID=experiment.id if experiment else None,
            description=slate_config.description,
            display_name=slate_config.displayName,
            recommendations=recommendations
        )
