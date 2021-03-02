from app.models.slate_lineup_experiment import SlateLineupExperimentModel
from app.models.slate_config import SlateConfigModel
from app.models.slate_lineup_config import SlateLineupConfigModel


def test_slate_lineup_config():
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
