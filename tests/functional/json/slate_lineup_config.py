import re

from app.models.slate_lineup_experiment import SlateLineupExperimentModel
from app.models.slate_config import SlateConfigModel
from app.models.slate_lineup_config import SlateLineupConfigModel


def test_slate_exists():
    """
    Test that all slates referenced in the slate_lineup config exist.
    """
    SlateConfigModel.SLATE_CONFIGS_BY_ID = {s.id: s for s in SlateConfigModel.load_slate_configs()}
    SlateLineupConfigModel.SLATE_LINEUP_CONFIGS = SlateLineupConfigModel.load_slate_lineup_configs()

    for slate_lineup_config in SlateLineupConfigModel.SLATE_LINEUP_CONFIGS:
        for experiment in slate_lineup_config.experiments:
            for slate in experiment.slates:
                if not SlateLineupExperimentModel.slate_id_exists(slate):
                    raise ValueError(f'slate {slate_lineup_config.id}|{experiment.description}|{slate} was not found')


def test_explore_topic_slates():
    """
    Test that all Explore Topic lineups have a curated and algorithmic slate, in this order.
    """
    slate_configs_by_id = {s.id: s for s in SlateConfigModel.load_slate_configs()}
    slate_lineup_configs = SlateLineupConfigModel.load_slate_lineup_configs()

    for slate_lineup_config in slate_lineup_configs:
        match = re.match(r'^Explore (.*?) Topic SlateLineup$', slate_lineup_config.description)
        if match:
            topic_name = match.group(1)
            for experiment in slate_lineup_config.experiments:
                slates = [slate_configs_by_id[slate_id] for slate_id in experiment.slates]

                assert topic_name in slates[0].displayName
                assert topic_name in slates[1].displayName

                assert "Curated" in slates[0].displayName
                assert "Algorithmic" in slates[1].displayName
