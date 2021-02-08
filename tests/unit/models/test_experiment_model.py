import json
import unittest

from app.models.experiment import Experiment


class TestExperimentInstantiation(unittest.TestCase):
    def test_no_weight(self):
        ex = Experiment(description='d', candidate_sets=['a'], rankers=['top15'])
        self.assertEqual(ex.weight, Experiment.DEFAULT_WEIGHT)

    def test_no_candidate_sets(self):
        with self.assertRaises(ValueError) as context:
            Experiment(description='desc', candidate_sets=[], rankers=[], weight=0)

        self.assertTrue('no candidate sets provided for experiment' in str(context.exception))

    def test_no_rankers(self):
        with self.assertRaises(ValueError) as context:
            Experiment(description='desc', candidate_sets=['a', 'b'], rankers=[], weight=0)

        self.assertTrue('no rankers provided for experiment' in str(context.exception))

    def test_invalid_ranker(self):
        with self.assertRaises(KeyError) as context:
            Experiment(description='desc', candidate_sets=['a', 'b'], rankers=['invalid'], weight=0)

        self.assertTrue('invalid is not a valid ranker' in str(context.exception))

    def test_valid_instantiation(self):
        desc = 'd'
        cs = ['a', 'b']
        rs = ['top15', 'pubspread']
        w = 0.2

        experiment = Experiment(description=desc, candidate_sets=cs, rankers=rs, weight=w)

        self.assertEqual(experiment.description, desc)
        self.assertEqual(experiment.candidate_sets, cs)
        self.assertEqual(experiment.rankers, ['top15', 'pubspread'])
        self.assertEqual(experiment.weight, w)


class TestLoadFromJson(unittest.TestCase):
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
        ex = Experiment.load_from_json(json.loads(json_str))

        self.assertEqual(ex.description, "TS window 30")
        self.assertEqual(ex.weight, Experiment.DEFAULT_WEIGHT)
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
        ex = Experiment.load_from_json(json.loads(json_str))

        self.assertEqual(ex.description, "TS window 15")
        self.assertEqual(ex.weight, 0.3)
        self.assertEqual(len(ex.candidate_sets), 3)
        self.assertEqual(len(ex.rankers), 2)