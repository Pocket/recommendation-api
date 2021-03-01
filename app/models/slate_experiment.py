from typing import List

from app.models.experiment import ExperimentModel


class SlateExperimentModel(ExperimentModel):
    """
    Models a slate experiment
    """
    def __init__(self, experiment_id: str, description: str, rankers: List[str], candidate_sets: List[str],
                 weight: float = ExperimentModel.DEFAULT_WEIGHT):
        ExperimentModel.__init__(self, experiment_id, description, rankers, weight)

        # validate candidate sets
        if len(candidate_sets) < 1:
            raise ValueError('no candidate sets provided for experiment')

        self.candidate_sets = candidate_sets

    @staticmethod
    def load_from_dict(experiment_dict: dict) -> 'SlateExperimentModel':
        """
        Creates an experiment object from a json-derived dictionary

        :param experiment_dict: a dictionary derived from parsing json
        :return: a SlateExperimentModel object
        """
        # generate an id for the experiment
        experiment_id = ExperimentModel.generate_experiment_id(experiment_dict)

        # determine the weight
        weight = experiment_dict.get('weight', ExperimentModel.DEFAULT_WEIGHT)

        return SlateExperimentModel(experiment_id, experiment_dict["description"], experiment_dict["rankers"],
                                    experiment_dict["candidateSets"], weight)
