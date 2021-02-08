import json
import unittest

from app.models.slate_experiment import SlateExperimentModel


class TestSlateExperimentModel(unittest.TestCase):
    # test instantiation

    def test_no_weight(self):
        ex = SlateExperimentModel(experiment_id='c3h5n3o9', description='d', candidate_sets=['a'], rankers=['top15'])
        self.assertEqual(ex.weight, SlateExperimentModel.DEFAULT_WEIGHT)

    def test_no_candidate_sets(self):
        with self.assertRaises(ValueError) as context:
            SlateExperimentModel(experiment_id='c3h5n3o9', description='desc', candidate_sets=[], rankers=['top15'])

        self.assertTrue('no candidate sets provided for experiment' in str(context.exception))

    def test_no_rankers(self):
        with self.assertRaises(ValueError) as context:
            SlateExperimentModel(experiment_id='c3h5n3o9', description='desc', candidate_sets=['a', 'b'], rankers=[],
                                 weight=0)

        self.assertTrue('no rankers provided for experiment' in str(context.exception))

    def test_invalid_ranker(self):
        with self.assertRaises(KeyError) as context:
            SlateExperimentModel(experiment_id='c3h5n3o9', description='desc', candidate_sets=['a', 'b'],
                                 rankers=['invalid'], weight=0)

        self.assertTrue('invalid is not a valid ranker' in str(context.exception))

    def test_valid_instantiation(self):
        ex_id = 'c3h5n3o9'
        desc = 'd'
        cs = ['a', 'b']
        rs = ['top15', 'pubspread']
        w = 0.2

        experiment = SlateExperimentModel(experiment_id=ex_id, description=desc, candidate_sets=cs, rankers=rs, weight=w)

        self.assertEqual(experiment.id, ex_id)
        self.assertEqual(experiment.description, desc)
        self.assertEqual(experiment.candidate_sets, cs)
        self.assertEqual(experiment.rankers, rs)
        self.assertEqual(experiment.weight, w)

    # test loading from json

    def test_load_from_json_without_weight(self):
        json_str = """
            {
               "description": "TS window 30",
               "candidateSets": [
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
        ex = SlateExperimentModel.load_from_dict(json.loads(json_str))

        self.assertEqual(ex.description, "TS window 30")
        self.assertEqual(ex.weight, SlateExperimentModel.DEFAULT_WEIGHT)
        self.assertEqual(len(ex.candidate_sets), 2)
        self.assertEqual(len(ex.rankers), 3)

    def test_load_from_json_with_weight(self):
        json_str = """
                {
               "description": "TS window 15",
               "candidateSets": [
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
        ex = SlateExperimentModel.load_from_dict(json.loads(json_str))

        self.assertEqual(ex.description, "TS window 15")
        self.assertEqual(ex.weight, 0.3)
        self.assertEqual(len(ex.candidate_sets), 3)
        self.assertEqual(len(ex.rankers), 2)
