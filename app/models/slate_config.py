import os
import random

from typing import List, Tuple

from app.config import JSON_DIR
from app.json.utils import parse_to_dict
from app.models.slate_experiment import SlateExperimentModel
from app.models.layout_config import LayoutConfigModel
from app.models.layout_experiment import LayoutExperimentModel
from app.rankers import RANKERS


class SlateConfigModel:
    """
    Represents the experiments that we might run when a layout or a client requests a slate of this id. Data for this
    model lives in hard-coded JSON files (which will be incrementally updated through PRs).

    This JSON is parsed at startup, and instances of this model will be persisted in-memory for use by Slate instances.

    Accepts on initialization:
    :param slate_id: str, the slate for which a request would run one of these experiments
    :param display_name: str, to provide clarity of what this slate includes (especially for topic slates)
    :param description: str, to provide clarity of what this slate includes when it's more complicated than a single
            topic
    """

    # store loaded slate configs
    SLATE_CONFIGS = []
    SLATE_CONFIGS_BY_ID = {}

    def __init__(self, slate_id: str, display_name: str, description: str, experiments=None):
        self.id = slate_id
        self.displayName = display_name
        self.description = description
        self.experiments = experiments or []

    @staticmethod
    def load_from_dict(slate_dict: dict) -> 'SlateConfigModel':
        """
        instantiates a SlateConfigModel object from a json-generated dictionary
        :param slate_dict: dictionary created from parsing json
        :return: SlateConfigModel instance
        """
        return SlateConfigModel(slate_dict["id"], slate_dict["displayName"], slate_dict["description"])

    @staticmethod
    def load_slate_configs(
            slate_file=os.path.join(JSON_DIR, 'slate_configs.json'),
            schema_file=os.path.join(JSON_DIR, 'slate_config.schema.json')
    ) -> List['SlateConfigModel']:
        """
        validates slate_file against schema_file and creates instances of SlateConfigModel for each slate found in the
        json

        :param slate_file: path to the json file containing slates
        :param schema_file: path to the json schema file used to validate slate_file
        :return: a List of Slate objects
        """
        # validate and retrieve the dictionary from json
        slates_dict = parse_to_dict(slate_file, schema_file)

        # get ready to store python Slate objects
        slates_objs = []

        for s in slates_dict:
            # populate simple slate properties
            slate = SlateConfigModel.load_from_dict(s)

            # populate experiments for the slate
            for ex in s["experiments"]:
                slate.experiments.append(SlateExperimentModel.load_from_dict(ex))

            slates_objs.append(slate)

        return slates_objs

    @staticmethod
    def find_by_id(slate_id: str) -> 'SlateConfigModel':
        """
        Gets a slate config from the list of slate configs

        :param slate_id: slate id
        :return: a SlateConfigModel object
        """
        slate_config = SlateConfigModel.SLATE_CONFIGS_BY_ID.get(slate_id)

        if not slate_config:
            raise ValueError(f'slate id {slate_id} was not found in the slate configs')

        return slate_config

    @staticmethod
    def get_configs_from_layout_config(
            layout_config: LayoutConfigModel) -> Tuple[LayoutExperimentModel, List['SlateConfigModel']]:
        """
        Gets a slate config from the list of slate configs

        :param layout_config: LayoutConfigModel object
        :return: a list of SlateConfigModel objects
        """
        # get the random experiment from the layout
        experiment = random.choice(layout_config.experiments)
        # get slate_ids from the experiment
        slate_ids = experiment.slates
        # get slates from the slate_ids
        slate_configs = []
        for slate_id in slate_ids:
            slate_configs.append(SlateConfigModel.find_by_id(slate_id))
        # apply rankers from the layout experiment on the slates
        for ranker in experiment.rankers:
            slate_configs = RANKERS[ranker](slate_configs)

        return experiment, slate_configs
