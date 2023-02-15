import uuid

from asyncio import gather
from pydantic import BaseModel, Field
from typing import List, Optional

from app.models.recommendation import RecommendationModel
from app.models.slate_config import SlateConfigModel
from app.models.slate_experiment import SlateExperimentModel
import app.config


class SlateModel(BaseModel):
    """
    Models a slate
    """
    id: str
    requestId: str = Field(
        default=None,
        description='A guid that is unique to every API request that returned slates, such as `getSlateLineup` or '
                    '`getSlate`. The API will provide a new request id every time apps hit the API.')
    experimentId: str = Field(
        default=None,
        description='A unique guid/slug, provided by the Data & Learning team that can identify a specific experiment. '
                    'Production apps typically won\'t request a specific one, but can for QA or during a/b testing.')
    display_name: str = Field(default=None, description='The name to show to the user for this set of recommendations')
    description: str = Field(default=None, description='The description of the the slate')
    recommendations: List[RecommendationModel] = Field(
        default=None, description='An ordered list of the recommendations to show to the user')

    @staticmethod
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
        HACK: For a particular set of QA users, change the slate to a QA slate if qa_slate_map has a replacement.
        This allows us to track the QA user's impression and open events through our engagement pipeline.
        This code is intended to be temporary. A better long-term solution would be to use Unleash,
        which is a feature flag service that supports putting specific users into an experiment branch.
        """
        if user_id in app.config.qa_user_ids and slate_config.id in app.config.qa_slate_map:
            slate_config = SlateConfigModel.find_by_id(app.config.qa_slate_map[slate_config.id])

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
