import os
import unittest

from app.models.slate_config import SlateConfigModel
from app.config import ROOT_DIR


class TestSlateConfigModel(unittest.TestCase):
    def test_load_valid_slates(self):
        slate_configs = SlateConfigModel.load_slate_configs(os.path.join(ROOT_DIR, 'tests/assets/json/slate_configs.json'))

        # make sure both slates in the test file were loaded
        self.assertEqual(2, len(slate_configs))

        # make sure each slate's experiments were also loaded
        # (this is some wild list comprehension syntax - gets all experiments in all slates)
        experiments = [ex for s in slate_configs for ex in s.experiments]
        self.assertEqual(4, len(experiments))

    def test_load_invalid_slate(self):
        with self.assertRaises(ValueError):
            SlateConfigModel.load_slate_configs(os.path.join(ROOT_DIR, 'tests/assets/json/invalid_slate_configs.json'))
