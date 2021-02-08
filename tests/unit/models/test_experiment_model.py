import json
import unittest

from app.models.experiment import ExperimentModel


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
