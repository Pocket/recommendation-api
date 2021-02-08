import hashlib
import json

from typing import List

from app.rankers.rankers import RANKERS as ALL_RANKERS


class ExperimentModel:
    # should this be in a config somewhere?
    DEFAULT_WEIGHT = 1

    def __init__(self, experiment_id: str, description: str, candidate_sets: List[str], rankers: List[str],
                 weight: float = DEFAULT_WEIGHT):
        # initialize values
        self.rankers = []

        # validate candidate sets
        if len(candidate_sets) < 1:
            raise ValueError('no candidate sets provided for experiment')

        # validate rankers
        if len(rankers) < 1:
            raise ValueError('no rankers provided for experiment')
        else:
            for ranker in rankers:
                # the ranker must exist in our pre-defined global list
                if ranker not in ALL_RANKERS:
                    raise KeyError(f'{ranker} is not a valid ranker')

                # the ranker cannot be duplicated in a single experiment
                if ranker in self.rankers:
                    raise KeyError(f'{ranker} was previously included in this list')

                self.rankers.append(ranker)

        self.id = experiment_id
        self.description = description
        self.candidate_sets = candidate_sets
        self.weight = weight

    @staticmethod
    def generate_experiment_id(experiment_dict: dict) -> str:
        """
        Generates an ID for an experiment based on the dictionary representation of the experiment. This will ensure that
        if an experiment changes, the ID will also change (which helps analytics).
        :param experiment_dict: dictionary representation of an experiment (after parsing from json)
        :return: first 7 characters of the hash created
        """
        hashed = hashlib.sha1(
            json.dumps(experiment_dict, sort_keys=True).encode()
        ).hexdigest()

        return hashed[:7]

    @staticmethod
    def load_from_dict(experiment_dict: dict) -> 'ExperimentModel':
        """
        creates an experiment object from a json-derived dictionary
        :param experiment_dict: a dictionary derived from parsing json
        :return: an instance of Experiment
        """
        # generate an id for the experiment
        experiment_id = ExperimentModel.generate_experiment_id(experiment_dict)

        # determine the weight
        weight = experiment_dict.get('weight', ExperimentModel.DEFAULT_WEIGHT)

        return ExperimentModel(experiment_id, experiment_dict["description"], experiment_dict["candidateSets"],
                               experiment_dict["rankers"], weight)

    @staticmethod
    def candidate_set_is_valid(candidate_set: str) -> bool:
        """
        :param candidate_set: string id of a candidate set to be verified
        :return: boolean (pronounced like "jolene")
        """
        # TODO: hit the database to make sure the candidate set exists
        # implement in https://getpocket.atlassian.net/browse/BACK-598
        return True
