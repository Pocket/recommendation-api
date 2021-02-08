import os
import unittest

from app.models.slateconfig import SlateConfigModel
from app.config import ROOT_DIR


class TestSlateModel(unittest.TestCase):
    def test_load_valid_slates(self):
        slateconfigs = SlateConfigModel.load_slateconfigs(os.path.join(ROOT_DIR, 'tests/assets/json/slateconfigs.json'))

        # make sure both slates in the test file were loaded
        self.assertEqual(2, len(slateconfigs))

        # make sure each slate's experiments were also loaded
        # (this is some wild list comprehension syntax - gets all experiments in all slates)
        experiments = [ex for s in slateconfigs for ex in s.experiments]
        self.assertEqual(4, len(experiments))
