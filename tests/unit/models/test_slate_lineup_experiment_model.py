import json
import unittest

from app.models.slate_lineup_experiment import SlateLineupExperimentModel


class TestSlateLineupExperimentModel(unittest.TestCase):
    # test instantiation

    def test_no_weight(self):
        ex = SlateLineupExperimentModel(experiment_id='c3h5n3o9', description='d', slates=['a'], rankers=['top15'])
        self.assertEqual(ex.weight, SlateLineupExperimentModel.DEFAULT_WEIGHT)

    def test_no_slates(self):
        with self.assertRaises(ValueError) as context:
            SlateLineupExperimentModel(experiment_id='c3h5n3o9', description='desc', slates=[], rankers=['top15'])

        self.assertTrue('no slates provided for experiment' in str(context.exception))

    def test_no_rankers(self):
        lem = SlateLineupExperimentModel(experiment_id='c3h5n3o9', description='desc', slates=['a', 'b'], rankers=[],
                                    weight=0)

        self.assertEqual(len(lem.rankers), 0)

    def test_invalid_ranker(self):
        with self.assertRaises(KeyError) as context:
            SlateLineupExperimentModel(experiment_id='c3h5n3o9', description='desc', slates=['a', 'b'],
                            rankers=['invalid'], weight=0)

        self.assertTrue('invalid is not a valid ranker' in str(context.exception))

    def test_valid_instantiation(self):
        ex_id = 'c3h5n3o9'
        desc = 'd'
        slates = ['a', 'b']
        rs = ['top15', 'pubspread']
        w = 0.2

        experiment = SlateLineupExperimentModel(experiment_id=ex_id, description=desc, slates=slates, rankers=rs, weight=w)

        self.assertEqual(experiment.id, ex_id)
        self.assertEqual(experiment.description, desc)
        self.assertEqual(experiment.slates, slates)
        self.assertEqual(experiment.rankers, rs)
        self.assertEqual(experiment.weight, w)

    # test loading from json

    def test_load_from_json_without_weight(self):
        json_str = """
            {
               "description": "TS window 30",
               "slates": [
                 "39d0dc54-f6f8-4f13-bea4-4320b3bd8217",
                 "df8a86c1-8b40-48bf-b85d-c144ed96c3fc"
               ],
               "rankers": [
                 "top30",
                 "thompson-sampling",
                 "pubspread"
               ]
            }
            """
        ex = SlateLineupExperimentModel.load_from_dict(json.loads(json_str))

        self.assertEqual(ex.description, "TS window 30")
        self.assertEqual(ex.weight, SlateLineupExperimentModel.DEFAULT_WEIGHT)
        self.assertEqual(len(ex.slates), 2)
        self.assertEqual(len(ex.rankers), 3)

    def test_load_from_json_with_weight(self):
        json_str = """
                {
               "description": "TS window 15",
               "slates": [
                 "39d0dc54-f6f8-4f13-bea4-4320b3bd8217",
                 "df8a86c1-8b40-48bf-b85d-c144ed96c3fc",
                 "df8a86c1-8b40-48bf-b85d-c144ed96c3fd"
               ],
               "rankers": [
                 "top15",
                 "thompson-sampling"
               ],
               "weight": 0.3
             }
            """
        ex = SlateLineupExperimentModel.load_from_dict(json.loads(json_str))

        self.assertEqual(ex.description, "TS window 15")
        self.assertEqual(ex.weight, 0.3)
        self.assertEqual(len(ex.slates), 3)
        self.assertEqual(len(ex.rankers), 2)
