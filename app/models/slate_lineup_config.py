from collections import Counter
import os

from typing import Optional, List

from app.config import JSON_DIR, dynamodb
from app.json.utils import parse_to_dict
from app.models.metrics.slate_metrics_factory import SlateMetricsFactory
from app.models.slate_lineup_experiment import SlateLineupExperimentModel
from app.models.slate_config import SlateConfigModel
from app.rankers import get_ranker, PERSONALIZED_RANKERS
from app.models.personalized_topic_list import PersonalizedTopicList


class SlateLineupConfigModel:
    """
    Represents the experiments that we might run when a client requests a slate_lineup of this id. Data for this
    model lives in hard-coded JSON files (which will be incrementally updated through PRs).

    This JSON is parsed at startup, and instances of this model will be persisted in-memory
    for use by SlateLineup instances.

    Accepts on initialization:
    :param slate_lineup_id: str, the slate_lineup for which a request would run one of these experiments
    :param description: str, to provide clarity of what this slate_lineup includes
    """

    # store loaded slate_lineup configs (loaded at app startup)
    SLATE_LINEUP_CONFIGS_BY_ID = {}

    def __init__(self, slate_lineup_id: str, description: str, experiments: Optional[List['SlateLineupExperimentModel']] = None):
        self.id = slate_lineup_id
        self.description = description
        self.experiments = experiments or []

    @staticmethod
    def load_from_dict(slate_lineup_dict: dict) -> 'SlateLineupConfigModel':
        """
        instantiates a SlateLineupConfigModel object from a json-generated dictionary
        :param slate_lineup_dict: dictionary created from parsing json
        :return: SlateLineupConfigModel instance
        """
        return SlateLineupConfigModel(slate_lineup_dict["id"], slate_lineup_dict["description"])

    @staticmethod
    def load_slate_lineup_configs(
            slate_lineup_file=os.path.join(JSON_DIR, 'slate_lineup_configs.json'),
            schema_file=os.path.join(JSON_DIR, 'slate_lineup_config.schema.json')
    ) -> List['SlateLineupConfigModel']:
        """
        validates slate_lineup_file against schema_file and creates instances of SlateLineupConfigModel
        for each slate found in the json

        :param slate_lineup_file: path to the json file containing slates
        :param schema_file: path to the json schema file used to validate slate_file
        :return: a List of SlateLineup objects
        """
        # validate and retrieve the dictionary from json
        slate_lineups_dict = parse_to_dict(slate_lineup_file, schema_file)

        # get ready to store python Slate objects
        slate_lineups_objs = []

        for ld in slate_lineups_dict:
            # populate simple slate properties
            slate_lineup = SlateLineupConfigModel.load_from_dict(ld)

            # populate experiments for the slate
            for ex in ld["experiments"]:
                slate_lineup.experiments.append(SlateLineupExperimentModel.load_from_dict(ex))

            slate_lineups_objs.append(slate_lineup)

        validate_lineup_config(slate_lineups_objs)

        return slate_lineups_objs

    @staticmethod
    def find_by_id(slate_lineup_id: str):
        """
        Gets a slate_lineup config from the list of slate_lineup configs

        :param slate_lineup_id: slate_lineup id
        :return: a SlateLineupConfigModel object
        """
        slate_lineup_config = SlateLineupConfigModel.SLATE_LINEUP_CONFIGS_BY_ID.get(slate_lineup_id)

        if not slate_lineup_config:
            raise ValueError(f'slate_lineup id {slate_lineup_id} was not found in the slate_lineup configs')

        return slate_lineup_config

    @staticmethod
    def get_experiment_from_slate_lineup(slate_lineup_id: str) -> SlateLineupExperimentModel:
        slate_lineup_config = SlateLineupConfigModel.find_by_id(slate_lineup_id)
        # get the random experiment from the slate_lineup
        return SlateLineupExperimentModel.choose_experiment(slate_lineup_config.experiments)

    @staticmethod
    async def get_slate_configs_from_experiment(
            slate_lineup_id: str, experiment: SlateLineupExperimentModel,
            user_id: Optional[str] = None) -> List[SlateConfigModel]:
        """
        Gets a slate config from the list of slate configs

        :param slate_lineup_id:
        :param experiment: SlateLineupExperimentModel object
        :param user_id: user_id for personalized rankers
        :return: a list of SlateConfigModel objects
        """
        # get slate_ids from the experiment
        slate_ids = experiment.slates
        # get slates from the slate_ids
        slate_configs = []
        for slate_id in slate_ids:
            slate_configs.append(SlateConfigModel.find_by_id(slate_id))

        # apply rankers from the slate_lineup experiment on the slate_configs
        # each experiment in the slate_lineup has 0 - x number of rankers which will
        # change the order of the slate_configs within the slate_lineup's experiment
        for ranker in experiment.rankers:
            ranker_kwargs = {}
            if ranker == 'thompson-sampling':
                # thompson sampling requires slate metrics
                ranker_kwargs = {
                    'metrics': await SlateMetricsFactory(dynamodb_endpoint=dynamodb["endpoint_url"]).get(
                        slate_lineup_id,
                        [s.id for s in slate_configs])
                }
            elif ranker in PERSONALIZED_RANKERS:
                ranker_kwargs = {
                    "personalized_topics": await PersonalizedTopicList.get(user_id)
                }
            # slate configs get ranked and re-assigned for every ranker within the experiment
            # for example we might first take the top 15 slate configs(that is one ranker)
            # and then randomize those 15 (which would be the second ranker)
            slate_configs = get_ranker(ranker)(slate_configs, **ranker_kwargs)

        return slate_configs


def validate_lineup_config(lineup_configs: List[SlateLineupConfigModel]) -> None:
    """
    Validates that a GUID is not re-used in a slate config. Raises a `ValueError` if it is.
    """
    slate_ids = Counter([r.id for r in lineup_configs])
    dupes = [guid for guid, count in slate_ids.items() if count > 1]
    if dupes:
        raise ValueError(f"Slate GUIDs appears more than once in slate config: {dupes}")


def validate_unique_guids(lineup_configs: List[SlateLineupConfigModel], slate_configs: List[SlateConfigModel]) -> None:
    """
    Validate that GUIDs are unique across lineups and slates. Raises a `ValueError` if they are not.
    """
    lineup_guids = {r.id for r in lineup_configs}
    slate_guids = {r.id for r in slate_configs}
    guid_overlap = lineup_guids.intersection(slate_guids)
    if guid_overlap:
        raise ValueError(f"Lineup and Slates share GUIDS: {guid_overlap}")
