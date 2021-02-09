import os

from typing import List

from app.config import JSON_DIR
from app.json.utils import parse_to_dict
from app.models.layout_experiment import LayoutExperimentModel


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
    LAYOUT_CONFIGS = []

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
        :return: a List of Slate objects
        """
        # validate and retrieve the dictionary from json
        layouts_dict = parse_to_dict(layout_file, schema_file)

        # get ready to store python Slate objects
        layouts_objs = []

        for l in layouts_dict:
            # populate simple slate properties
            layout = LayoutConfigModel.load_from_dict(l)

            # populate experiments for the slate
            for ex in l["experiments"]:
                layout.experiments.append(LayoutExperimentModel.load_from_dict(ex))

            layouts_objs.append(layout)

        return layouts_objs
