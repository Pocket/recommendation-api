from typing import List

from app.models.experiment import ExperimentModel
from app.models.slate_config import SlateConfigModel


class LayoutExperimentModel(ExperimentModel):
    """
    Models a layout experiment
    """
    def __init__(self, experiment_id: str, description: str, rankers: List[str],slates: List[str],
                 weight: float = ExperimentModel.DEFAULT_WEIGHT):
        ExperimentModel.__init__(self, experiment_id, description, rankers, weight)

        # validate slates
        if len(slates) < 1:
            raise ValueError('no slates provided for experiment')

        self.slates = slates

    @staticmethod
    def load_from_dict(experiment_dict: dict) -> 'LayoutExperimentModel':
        """
        Creates an experiment object from a json-derived dictionary

        :param experiment_dict: a dictionary derived from parsing json
        :return: a LayoutExperimentModel object
        """
        # generate an id for the experiment
        experiment_id = ExperimentModel.generate_experiment_id(experiment_dict)

        # determine the weight
        weight = experiment_dict.get('weight', ExperimentModel.DEFAULT_WEIGHT)

        return LayoutExperimentModel(experiment_id, experiment_dict["description"], experiment_dict["rankers"],
                                     experiment_dict["slates"], weight)

    @staticmethod
    def slate_id_exists(slate_id: str) -> bool:
        """
        Verify that the slate id exists

        :param slate_id: string id of a slate to be verified
        :return: boolean (pronounced like "jolene")
        """
        return slate_id in SlateConfigModel.SLATE_CONFIGS_BY_ID
