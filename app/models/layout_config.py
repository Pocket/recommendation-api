import os
import random

from typing import List

from app.config import JSON_DIR
from app.json.utils import parse_to_dict
from app.models.layout_experiment import LayoutExperimentModel
from app.models.slate_config import SlateConfigModel
from app.rankers import get_ranker


class LayoutConfigModel:
    """
    Represents the experiments that we might run when a client requests a layout of this id. Data for this
    model lives in hard-coded JSON files (which will be incrementally updated through PRs).

    This JSON is parsed at startup, and instances of this model will be persisted in-memory for use by Layout instances.

    Accepts on initialization:
    :param layout_id: str, the layout for which a request would run one of these experiments
    :param description: str, to provide clarity of what this layout includes
    """

    # store loaded layout configs
    LAYOUT_CONFIGS_BY_ID = {}

    def __init__(self, layout_id: str, description: str, experiments=None):
        self.id = layout_id
        self.description = description
        self.experiments = experiments or []

    @staticmethod
    def load_from_dict(layout_dict: dict) -> 'LayoutConfigModel':
        """
        instantiates a LayoutConfigModel object from a json-generated dictionary
        :param layout_dict: dictionary created from parsing json
        :return: LayoutConfigModel instance
        """
        return LayoutConfigModel(layout_dict["id"], layout_dict["description"])

    @staticmethod
    def load_layout_configs(
            layout_file=os.path.join(JSON_DIR, 'layout_configs.json'),
            schema_file=os.path.join(JSON_DIR, 'layout_config.schema.json')
    ) -> List['LayoutConfigModel']:
        """
        validates layout_file against schema_file and creates instances of LayoutConfigModel for each slate found in
        the json

        :param layout_file: path to the json file containing slates
        :param schema_file: path to the json schema file used to validate slate_file
        :return: a List of Layout objects
        """
        # validate and retrieve the dictionary from json
        layouts_dict = parse_to_dict(layout_file, schema_file)

        # get ready to store python Slate objects
        layouts_objs = []

        for ld in layouts_dict:
            # populate simple slate properties
            layout = LayoutConfigModel.load_from_dict(ld)

            # populate experiments for the slate
            for ex in ld["experiments"]:
                layout.experiments.append(LayoutExperimentModel.load_from_dict(ex))

            layouts_objs.append(layout)

        return layouts_objs

    @staticmethod
    def find_by_id(layout_id: str):
        """
        Gets a layout config from the list of layout configs

        :param layout_id: layout id
        :return: a LayoutConfigModel object
        """
        layout_config = LayoutConfigModel.LAYOUT_CONFIGS_BY_ID.get(layout_id)

        if not layout_config:
            raise ValueError(f'layout id {layout_id} was not found in the layout configs')

        return layout_config

    @staticmethod
    def get_slate_configs_from_layout(layout_id):
        """
        Gets a slate config from the list of slate configs

        :param layout_id: LayoutConfigModel object
        :return: a list of SlateConfigModel objects
        """

        layout_config = LayoutConfigModel.find_by_id(layout_id)
        # get the random experiment from the layout
        experiment = random.choice(layout_config.experiments)
        # get slate_ids from the experiment
        slate_ids = experiment.slates
        # get slates from the slate_ids
        slate_configs = []
        for slate_id in slate_ids:
            slate_configs.append(SlateConfigModel.find_by_id(slate_id))

        # apply rankers from the layout experiment on the slate_configs
        # each experiment in the layout has 0 - x number of rankers which will
        # change the order of the slate_configs within the layout's experiment
        for ranker in experiment.rankers:
            # slate configs get ranked and re-assigned for every ranker within the experiment
            # for example we might first take the top 15 slate configs(that is one ranker)
            # and then randomize those 15 (which would be the second ranker)
            slate_configs = get_ranker(ranker)(slate_configs)

        return experiment, slate_configs
