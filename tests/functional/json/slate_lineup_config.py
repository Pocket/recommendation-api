import re

from app.models.slate_lineup_experiment import SlateLineupExperimentModel
from app.models.slate_config import SlateConfigModel
from app.models.slate_lineup_config import SlateLineupConfigModel, validate_unique_guids
import pytest


def test_validate_config():
    # Overlapping GUIDs between configs
    slate_config = [SlateConfigModel("617d9613-d338-4cc0-92ba-9a90831f6a46", "dupe slate", "dupe slate")]
    lineup_config = [SlateLineupConfigModel("617d9613-d338-4cc0-92ba-9a90831f6a46", "Duplicated GUID")]
    with pytest.raises(ValueError):
        validate_unique_guids(lineup_config, slate_config)


def test_slate_exists():
    """
    Test that slate and lineup configs are valid
    """
    SlateConfigModel.SLATE_CONFIGS_BY_ID = {s.id: s for s in SlateConfigModel.load_slate_configs()}
    SlateLineupConfigModel.SLATE_LINEUP_CONFIGS = SlateLineupConfigModel.load_slate_lineup_configs()

    validate_unique_guids(SlateLineupConfigModel.SLATE_LINEUP_CONFIGS, list(SlateConfigModel.SLATE_CONFIGS_BY_ID.items()))

    # Check that referenced slates exist
    for slate_lineup_config in SlateLineupConfigModel.SLATE_LINEUP_CONFIGS:
        for experiment in slate_lineup_config.experiments:
            for slate in experiment.slates:
                if not SlateLineupExperimentModel.slate_id_exists(slate):
                    raise ValueError(f'slate {slate_lineup_config.id}|{experiment.description}|{slate} was not found')


def test_explore_topic_slates():
    """
    Test that all Explore Topic lineups have a curated and algorithmic slate, in this order.

    The Web repo currently relies on this ordering in src/Discover/RecommendationAPIClient.php:getTopicRecommendations
    to return curated and algorithmic slates via the legacy v3/discover/topics endpoint.
    """
    slate_configs_by_id = {s.id: s for s in SlateConfigModel.load_slate_configs()}
    slate_lineup_configs = SlateLineupConfigModel.load_slate_lineup_configs()

    for slate_lineup_config in slate_lineup_configs:
        match = re.match(r'^Explore (.*?) Topic SlateLineup$', slate_lineup_config.description)
        if match:
            topic_name = match.group(1)
            for experiment in slate_lineup_config.experiments:
                slates = [slate_configs_by_id[slate_id] for slate_id in experiment.slates]

                # Assert that the first two slates are topic slates
                assert topic_name in slates[0].displayName
                assert topic_name in slates[1].displayName

                # Assert that slates are ordered curated, algorithmic.
                assert "Curated" in slates[0].displayName
                assert "Algorithmic" in slates[1].displayName
