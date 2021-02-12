import hashlib
import json
import random

from abc import ABCMeta, abstractmethod
from typing import List, Type

from app.rankers import get_all_rankers


class ExperimentModel(metaclass=ABCMeta):
    """
    This is a base class for Slate experiments and Layout experiments. As of writing, these implementations are nearly
    identical - slate experiments have candidate sets (an array of strings) while layout experiments have slates (also
    an array of strings). This base class seemed the most appropriate abstraction at the time, but may require
    revisiting if experiments diverge further.
    """
    # should this be in a config somewhere?
    DEFAULT_WEIGHT = 1

    def __init__(self, experiment_id: str, description: str, rankers: List[str], weight: float = DEFAULT_WEIGHT):
        # initialize values
        self.rankers = []

        for ranker in rankers:
            # the ranker must exist in our pre-defined global list
            if ranker not in get_all_rankers():
                raise KeyError(f'{ranker} is not a valid ranker')

            # the ranker cannot be duplicated in a single experiment
            if ranker in self.rankers:
                raise KeyError(f'{ranker} was previously included in this list')

            self.rankers.append(ranker)

        self.id = experiment_id
        self.description = description
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
    def choose_experiment(experiments: List['ExperimentModel']):
        """
        There's no return type-hint here as there's no easy way (I could find) to have python set the return type to
        be the implementing/child class. We *could* overrdie this method in each child class to specify the return type,
        but that seemed, well, to be doing a lot just for a type hint.
        :param experiments: a list of child classes of this class
        :return: ExperimentModel instance
        """
        # pull all the weights for each experiment
        weights = [e.weight for e in experiments]

        # use python's magic to make a random, weighted choice
        return random.choices(experiments, weights=weights)[0]

    @staticmethod
    @abstractmethod
    def load_from_dict(experiment_dict: dict) -> Type['ExperimentModel']:
        pass
