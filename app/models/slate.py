import uuid

from asyncio import gather
from aws_xray_sdk.core import xray_recorder
from pydantic import BaseModel
from typing import List, Optional

from app.models.recommendation import RecommendationModel
from app.models.slate_config import SlateConfigModel
from app.models.slate_experiment import SlateExperimentModel


class SlateModel(BaseModel):
    """
    Models a slate
    """
    id: str
    requestId: str = None
    experimentId: str = None
    display_name: str = None
    description: str = None
    recommendations: List[RecommendationModel] = None

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_slate')
    async def get_slate(slate_id: str, user_id: str = None, recommendation_count: Optional[int] = 10) -> 'SlateModel':
        """
        Retrieves a SlateModel from the database

        :param slate_id: string id of the slate to retrieve
        :param user_id: string user id (reserved for future use)
        :param recommendation_count: int, 0 = no recs, > 0 include this many recs
        :return: a SlateModel object
        """
        slate_config = SlateConfigModel.find_by_id(slate_id)
        return await SlateModel.__get_slate_from_slate_config(slate_config, recommendation_count=recommendation_count)

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_all')
    async def get_all(recommendation_count: Optional[int] = 10) -> List['SlateModel']:
        """
        Retrieves all slates from the database
        :param recommendation_count: int, 0 = no recs, > 0 include this many recs
        :return: a list fo SlateModel objects
        """
        slate_configs = SlateConfigModel.SLATE_CONFIGS_BY_ID.values()
        return await SlateModel.get_slates_from_slate_configs(slate_configs, recommendation_count=recommendation_count)

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_slates_from_slate_configs')
    async def get_slates_from_slate_configs(slate_configs: List['SlateConfigModel'],
                                            recommendation_count: Optional[int] = 10) -> List['SlateModel']:
        """

        :param slate_configs:
        :param recommendation_count: int, 0 = no recs, > 0 include this many recs
        :return: a list of SlateModel objects
        """
        slate_models = []

        # for each slate, get random experiment
        for slate_config in slate_configs:
            slate_model = SlateModel.__get_slate_from_slate_config(slate_config,
                                                                   recommendation_count=recommendation_count)
            slate_models.append(slate_model)

        slate_models = await gather(*slate_models)

        # unsure why this is failing the type hint - probably something to do with `gather`
        return slate_models

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_slate_from_slate_config')
    async def __get_slate_from_slate_config(slate_config: 'SlateConfigModel',
                                            recommendation_count: Optional[int] = 10) -> 'SlateModel':
        """
        Returns a slate model based on the supplied config

        :param slate_config: a SlateConfigModel object
        :param recommendation_count: int, 0 = no recs, > 0 include this many recs
        :return: a SlateModel object
        """

        experiment = None
        recommendations = []

        # If we have a > 0 recommendation count lets get some recommendations
        if recommendation_count > 0:
            experiment = SlateExperimentModel.choose_experiment(slate_config.experiments)
            recommendations = await RecommendationModel.get_recommendations_from_experiment(experiment)
            recommendations = recommendations[:recommendation_count]

        return SlateModel(
            id=slate_config.id,
            experimentId=experiment.id if experiment else None,
            description=slate_config.description,
            display_name=slate_config.displayName,
            recommendations=recommendations,
            requestId=str(uuid.uuid4()),
        )
