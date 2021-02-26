from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.models.candidate_set import CandidateSetModel
from app.models.recommendation import RecommendationModel


class TestCandidateSetsModel(TestDynamoDBBase):
    async def test_verify_candidate_set(self):
        self.candidateSetTable.put_item(Item={
            "id": "asdasd-12sd1asd3-5512",
            "version": 1,
            "created_at": 1612907252,
            "candidates": [
                {
                    "feed_id": 1,
                    "item_id": 3208490410,
                    "publisher": "hbr.org"
                }
            ]
        })

        executed = await CandidateSetModel.verify_candidate_set(cs_id='asdasd-12sd1asd3-5512')
        assert executed == True

    async def test_get_candidate_set(self):
        self.candidateSetTable.put_item(Item={
            "id": "asdasd-12sd1asd3-5512",
            "version": 1,
            "created_at": 1612907252,
            "candidates": [
                {
                    "feed_id": 1,
                    "item_id": 3208490410,
                    "publisher": "hbr.org"
                }
            ]
        })

        candidate_set = await CandidateSetModel.get(cs_id='asdasd-12sd1asd3-5512')
        assert candidate_set.id == 'asdasd-12sd1asd3-5512'
        assert len(candidate_set.candidates) == 1
        candidate = candidate_set.candidates[0]
        assert candidate.item_id == 3208490410
