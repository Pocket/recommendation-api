import os
import unittest

from app.models.slate_lineup_config import SlateLineupConfigModel
from app.config import ROOT_DIR


class TestSlateLineupConfigModel(unittest.TestCase):
    def test_load_valid_slates(self):
        slate_lineup_configs = SlateLineupConfigModel.load_slate_lineup_configs(os.path.join(ROOT_DIR, 'tests/assets/json/slate_lineup_configs.json'))

        # make sure both slate_lineups in the test file were loaded
        self.assertEqual(3, len(slate_lineup_configs))

        # make sure each slate_lineup's experiments were also loaded
        # (this is some wild list comprehension syntax - gets all experiments in all slate_lineups)
        experiments = [ex for lc in slate_lineup_configs for ex in lc.experiments]
        self.assertEqual(4, len(experiments))

    def test_invalid_slates(self):
        with self.assertRaises(ValueError):
            SlateLineupConfigModel.load_slate_lineup_configs(os.path.join(ROOT_DIR, 'tests/assets/json/invalid_slate_lineup_configs.json'))
