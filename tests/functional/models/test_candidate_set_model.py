from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.models.candidate_set import DynamoDBCandidateSet
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

        executed = await DynamoDBCandidateSet.verify_candidate_set(cs_id='asdasd-12sd1asd3-5512')
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

        candidate_set = await DynamoDBCandidateSet.get(cs_id='asdasd-12sd1asd3-5512')
        assert candidate_set.id == 'asdasd-12sd1asd3-5512'
        assert len(candidate_set.candidates) == 1
        candidate = candidate_set.candidates[0]
        assert candidate.item_id == 3208490410

    async def test_get_cached_candidate_set(self):
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

        # Get and cache the candidate set.
        candidate_set = await DynamoDBCandidateSet.get(cs_id='asdasd-12sd1asd3-5512')
        assert candidate_set.version == 1
        assert candidate_set.candidates[0].item_id == 3208490410

        # Change version from 1 to 2.
        self.candidateSetTable.update_item(
            Key={'id': 'asdasd-12sd1asd3-5512'},
            UpdateExpression="set version=:v",
            ExpressionAttributeValues={':v': 2})

        # Assert version has not changed, because we're getting the candidate set from cache.
        candidate_set = await DynamoDBCandidateSet.get(cs_id='asdasd-12sd1asd3-5512')
        assert candidate_set.version == 1
        assert candidate_set.candidates[0].item_id == 3208490410

        await super().clear_caches()

        # Assert version changed, because the cache has been cleared.
        candidate_set = await DynamoDBCandidateSet.get(cs_id='asdasd-12sd1asd3-5512')
        assert candidate_set.version == 2
        assert candidate_set.candidates[0].item_id == 3208490410
