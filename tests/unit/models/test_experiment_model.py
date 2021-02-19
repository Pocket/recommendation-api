import json
import unittest

from app.models.experiment import ExperimentModel
from app.models.slate_experiment import SlateExperimentModel


class TestExperimentModel(unittest.TestCase):
    # test generating ids

    def test_generate_experiment_id(self):
        ex_dict = {
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

        ex_id = ExperimentModel.generate_experiment_id(ex_dict)
        ex_id_again = ExperimentModel.generate_experiment_id(ex_dict)

        # make sure we are only getting 7 characters
        self.assertEqual(7, len(ex_id))

        # make sure repeated calls with the same dict result in the same id
        self.assertEqual(ex_id, ex_id_again)

    def test_choose_experiment(self):
        experiments = [
            SlateExperimentModel('1', 'first', [], ['a', 'b', 'c'], 0.1),
            SlateExperimentModel('2', 'second', [], ['d', 'e', 'f'], 0.3),
            SlateExperimentModel('3', 'third', [], ['g', 'h', 'i'], 0.6)
        ]

        choices = []

        # choose 100 times to get a sample size
        for _ in range(100):
            choices.append(ExperimentModel.choose_experiment(experiments))

        # make sure the number of each choice roughly corresponds with the expected weight/frequency
        first = [e.id for e in choices if e.id == '1']
        second = [e.id for e in choices if e.id == '2']
        third = [e.id for e in choices if e.id == '3']

        # as we're dealing with semi-randomness, it's inconsistent to check percentages, but we *should* always be able
        # to count on the frequency order to be predictable (...right?)
        self.assertTrue(len(third) > len(second) > len(first))
