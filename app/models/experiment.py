from typing import List

# from app.models.rankers import Ranker
from app.rankers.rankers import RANKERS as ALL_RANKERS


class Experiment:
    # should this be in a config somewhere?
    DEFAULT_WEIGHT = 1

    def __init__(self, description: str, candidate_sets: List[str], rankers: List[str], weight: float = DEFAULT_WEIGHT):
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

        self.description = description
        self.candidate_sets = candidate_sets
        self.weight = weight

    @staticmethod
    def load_from_json(json: dict) -> 'Experiment':
        """
        creates an experiment object from a json-derived dictionary
        :param json: a dictionary derived from parsing json
        :return: an instance of Experiment
        """
        weight = json.get('weight', Experiment.DEFAULT_WEIGHT)
        return Experiment(json["description"], json["candidateSets"], json["rankers"], weight)

    @staticmethod
    def candidate_set_is_valid(candidate_set: str) -> bool:
        """
        :param candidate_set: string id of a candidate set to be verified
        :return: boolean (pronounced like "jolene")
        """
        # TODO: hit the database to make sure the candidate set exists
        # implement in https://getpocket.atlassian.net/browse/BACK-598
        return True
