import os
import unittest

from app.models.layout_config import LayoutConfigModel
from app.config import ROOT_DIR


class TestLayoutConfigModel(unittest.TestCase):
    def test_load_valid_slates(self):
        layout_configs = LayoutConfigModel.load_layout_configs(os.path.join(ROOT_DIR, 'tests/assets/json/layout_configs.json'))

        # make sure both layouts in the test file were loaded
        self.assertEqual(3, len(layout_configs))

        # make sure each layout's experiments were also loaded
        # (this is some wild list comprehension syntax - gets all experiments in all layouts)
        experiments = [ex for lc in layout_configs for ex in lc.experiments]
        self.assertEqual(4, len(experiments))
