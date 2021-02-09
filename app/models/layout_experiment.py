from typing import List

from app.models.experiment import ExperimentModel


class LayoutExperimentModel(ExperimentModel):
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
        creates an experiment object from a json-derived dictionary
        :param experiment_dict: a dictionary derived from parsing json
        :return: an instance of LayoutExperimentModel
        """
        # generate an id for the experiment
        experiment_id = ExperimentModel.generate_experiment_id(experiment_dict)

        # determine the weight
        weight = experiment_dict.get('weight', ExperimentModel.DEFAULT_WEIGHT)

        return LayoutExperimentModel(experiment_id, experiment_dict["description"], experiment_dict["rankers"],
                                     experiment_dict["slates"], weight)

    @staticmethod
    def slate_is_valid(slate_id: str) -> bool:
        """
        :param slate_id: string id of a slate to be verified
        :return: boolean (pronounced like "jolene")
        """
        # TODO: hit the database to make sure the slate exists
        # implement in https://getpocket.atlassian.net/browse/BACK-???
        return True
