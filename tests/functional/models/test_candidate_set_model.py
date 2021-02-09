from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.models.candidate_set import CandidateSetModel


class TestCandidateSetsModel(TestDynamoDBBase):

    async def test_get_latest_curated_candidates_for_topic(self):
        self.candidateSetTable.put_item(Item={
            "id": "asdasd-12sd1asd3-5512",
            "candidates": [
                "asdasd-12sd1asd3-5512",
                "asdasd-12sd1asd3-5513"
            ]
        })

        executed = await CandidateSetModel.verify_candidate_set(cs_id='asdasd-12sd1asd3-5512')
        assert executed == True
