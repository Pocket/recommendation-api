import os

from app.models.experiment import Experiment
from typing import List

from app.config import JSON_DIR
from app.json.utils import parse_to_dict


# store loaded slates
SLATE_CONFIGS = []


class SlateConfigModel:
    def __init__(self, slate_id: str, display_name: str, description: str, experiments=None):
        self.id = slate_id
        self.displayName = display_name
        self.description = description
        self.experiments = experiments or []

    @staticmethod
    def load_from_dict(slate_dict: dict) -> 'SlateConfigModel':
        """
        instantiates a Slate object from a json-generated dictionary
        :param slate_dict: dictionary created from parsing json
        :return: Slate instance
        """
        return SlateConfigModel(slate_dict["id"], slate_dict["displayName"], slate_dict["description"])

    @staticmethod
    def load_slateconfigs(
            slate_file=os.path.join(JSON_DIR, 'slateconfigs.json'),
            schema_file=os.path.join(JSON_DIR, 'slateconfig.schema.json')
    ) -> List['SlateConfigModel']:
        """
        validates slate_file against schema_file and creates instances of Slate for each slate found in the json

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
                slate.experiments.append(Experiment.load_from_json(ex))

            slates_objs.append(slate)

        return slates_objs
