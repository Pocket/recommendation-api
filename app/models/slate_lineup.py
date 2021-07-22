import uuid

from aws_xray_sdk.core import xray_recorder
from pydantic import BaseModel
from typing import List, Optional

from app.models.slate_lineup_config import SlateLineupConfigModel
from app.models.slate_lineup_experiment import SlateLineupExperimentModel
from app.models.slate import SlateModel, deduplicate_recommendations_across_slates


class SlateLineupModel(BaseModel):
    """
    Models a slate_lineup.
    """
    id: str
    requestId: str = None
    experimentId: str = None
    slates: List[SlateModel]

    @staticmethod
    @xray_recorder.capture_async('models_slate_lineup_get_slate_lineup')
    async def get_slate_lineup(slate_lineup_id: str, user_id: Optional[str] = None,
                               recommendation_count: Optional[int] = 10,
                               slate_count: Optional[int] = 8) -> 'SlateLineupModel':
        """
        Retrieves a slate_lineup based on the given `slate_lineup_id`

        :param slate_lineup_id: string id of the slate_lineup
        :param user_id: string user id (reserved for future use)
        :param recommendation_count: int, 0 = no recs, > 0 include this many recs
        :param slate_count: int, 0 = no slates, > 0 include this many slates
        :return: SlateLineupModel object
        """
        experiment = SlateLineupConfigModel.get_experiment_from_slate_lineup(slate_lineup_id)
        slates = await SlateLineupModel.__get_slates_from_experiment(slate_lineup_id,
                                                                     experiment,
                                                                     user_id=user_id,
                                                                     recommendation_count=recommendation_count,
                                                                     slate_count=slate_count)

        return SlateLineupModel(
            id=slate_lineup_id,
            experimentId=experiment.id,
            slates=slates,
            requestId=str(uuid.uuid4()),
        )

    @staticmethod
    async def __get_slates_from_experiment(slate_lineup_id: str,
                                           experiment: SlateLineupExperimentModel,
                                           user_id: str,
                                           recommendation_count: Optional[int] = 10,
                                           slate_count: Optional[int] = 8) -> List[SlateModel]:
        """
        Retrieves an experiment ID and a list of SlateModel objects

        :param experiment: a SlateLineupExperiment object
        :param recommendation_count: int, None = include unlimited recs, 0 = no recs, > 0 include this many recs
        :param slate_count: int, 0 = no slates, > 0 include this many slates
        :return: a list of SlateModel objects
        """
        # Client requested no slates so return an empty array
        if slate_count == 0:
            return []

        # get the requested slate_lineup from the config using the slate_lineup_id
        slate_configs = await SlateLineupConfigModel.get_slate_configs_from_experiment(slate_lineup_id, experiment,
                                                                                       user_id=user_id)

        # Client requested only a certain number of slates, so after it was ranked, split the list to the count
        slate_configs = slate_configs[:slate_count]

        slates = await SlateModel.get_slates_from_slate_configs(
            slate_configs, user_id, recommendation_count=recommendation_count)

        slates = await deduplicate_recommendations_across_slates(slates)

        return slates
