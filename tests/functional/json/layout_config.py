from app.models.layout_experiment import LayoutExperimentModel
from app.models.slate_config import SlateConfigModel
from app.models.layout_config import LayoutConfigModel


def test_layout_config():
    """
    Test that all slates referenced in the layout config exist.
    """
    SlateConfigModel.SLATE_CONFIGS_BY_ID = {s.id: s for s in SlateConfigModel.load_slate_configs()}
    LayoutConfigModel.LAYOUT_CONFIGS = LayoutConfigModel.load_layout_configs()

    for layout_config in LayoutConfigModel.LAYOUT_CONFIGS:
        for experiment in layout_config.experiments:
            for slate in experiment.slates:
                if not LayoutExperimentModel.slate_id_exists(slate):
                    raise ValueError(f'slate {layout_config.id}|{experiment.description}|{slate} was not found')
