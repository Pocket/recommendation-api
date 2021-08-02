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

    __QA_USER_IDS = ['47372502']
    __QA_SLATE_MAP = {
        "2e3ddc90-8def-46d7-b85f-da7525c66fb1": "9dc26792-10ed-4fbe-a13d-6cce3a89b0a1",
        "0c09627b-a409-4768-b87d-7e1d29259785": "e8251442-ef97-422f-ad65-0f28e6f7a0d6",
        "0f322865-64e6-472d-8147-b3d6637a7d67": "b70d65c6-9171-40bf-bddb-5a60d42dd03f",
    }

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
        return await SlateModel.__get_slate_from_slate_config(
            slate_config,
            user_id,
            recommendation_count=recommendation_count)

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_all')
    async def get_all(user_id: str, recommendation_count: Optional[int] = 10) -> List['SlateModel']:
        """
        Retrieves all slates from the database
        :param recommendation_count: int, 0 = no recs, > 0 include this many recs
        :param user_id: ID of user we are getting slates for.
        :return: a list fo SlateModel objects
        """
        slate_configs = SlateConfigModel.SLATE_CONFIGS_BY_ID.values()
        return await SlateModel.get_slates_from_slate_configs(
            slate_configs, user_id,
            recommendation_count=recommendation_count)

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_slates_from_slate_configs')
    async def get_slates_from_slate_configs(slate_configs: List['SlateConfigModel'],
                                            user_id: str,
                                            recommendation_count: Optional[int] = 10) -> List['SlateModel']:
        """

        :param slate_configs:
        :param user_id: Identifies user to deliver personalized recommendations
        :param recommendation_count: int, 0 = no recs, > 0 include this many recs
        :return: a list of SlateModel objects
        """
        slate_models = []

        # for each slate, get random experiment
        for slate_config in slate_configs:
            slate_model = SlateModel.__get_slate_from_slate_config(
                slate_config,
                user_id,
                recommendation_count=recommendation_count)
            slate_models.append(slate_model)

        slate_models = await gather(*slate_models)

        # unsure why this is failing the type hint - probably something to do with `gather`
        return slate_models

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_slate_from_slate_config')
    async def __get_slate_from_slate_config(slate_config: 'SlateConfigModel',
                                            user_id: str,
                                            recommendation_count: Optional[int] = 10) -> 'SlateModel':
        """
        Returns a slate model based on the supplied config

        :param slate_config: a SlateConfigModel object
        :param recommendation_count: int, 0 = no recs, > 0 include this many recs
        :return: a SlateModel object
        """

        experiment = None
        recommendations = []


        """
        HACK: For a particular set of QA users, change the slate to a QA slate.
        This allows us to track the QA user's impression and open events through our engagement pipeline.
        This code is intended to be temporary. A better long-term solution would be to use Unleash,
        which is a feature flag service that supports putting specific users into an experiment branch.
        """
        if user_id in SlateModel.__QA_USER_IDS and slate_config.id in SlateModel.__QA_SLATE_MAP:
            slate_config = SlateConfigModel.find_by_id(SlateModel.__QA_SLATE_MAP[slate_config.id])

        # If we have a > 0 recommendation count lets get some recommendations
        if recommendation_count > 0:
            experiment = SlateExperimentModel.choose_experiment(slate_config.experiments)
            recommendations = await RecommendationModel.get_recommendations_from_experiment(slate_config.id,
                                                                                            experiment,
                                                                                            user_id)
            recommendations = recommendations[:recommendation_count]

        return SlateModel(
            id=slate_config.id,
            experimentId=experiment.id if experiment else None,
            description=slate_config.description,
            display_name=slate_config.displayName,
            recommendations=recommendations,
            requestId=str(uuid.uuid4()),
        )


async def deduplicate_recommendations_across_slates(slates: List[SlateModel]) -> List[SlateModel]:
    seen_item_ids = set()

    for slate in slates:
        # Remove recommendations that exist in previous slates
        slate.recommendations = [r for r in slate.recommendations if r.item_id not in seen_item_ids]
        # Add all item ids from slate to seen_item_ids
        seen_item_ids |= {r.item_id for r in slate.recommendations}

    return slates
