import unittest
import json
import os
from app.models.candidate_set import RecItCandidateSet
from app.config import ROOT_DIR

class TestCandidateSetModel(unittest.TestCase):
    def test_recit_parse(self):
        with open(os.path.join(ROOT_DIR, "tests/assets/json/recit_response.json")) as f:
            recit_json = json.load(f)
        candidate_set = RecItCandidateSet.parse_recit_response("test-id", recit_json)
        self.assertEqual(len(candidate_set.candidates), len(recit_json['items']))
        self.assertEqual(candidate_set.candidates[0].item_id, recit_json['items'][0]["resolved_id"])

    def test_recit_validate_id(self):
        self.assertTrue(RecItCandidateSet._verify_candidate_set("recit-personalized/bestof"))
        self.assertFalse(RecItCandidateSet._verify_candidate_set("recit-personalized/not-a-real-module"))
        self.assertFalse(RecItCandidateSet._verify_candidate_set("wrackit-personalized/bestof"))
