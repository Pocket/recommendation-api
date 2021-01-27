import random
from typing import List
from operator import itemgetter
from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.models.clickdata import ClickdataModel, RecommendationModules
from app.models.topic_recommendations import TopicRecommendationsModelUtils
from app.models.recommendation import RecommendationModel

class TestThompsonSampling(TestDynamoDBBase):

    @staticmethod
    def generate_recommendations(item_ids: List[str]) -> List[RecommendationModel]:
        recs = []
        for item_id in item_ids:
            rec = RecommendationModel()
            rec.item_id = item_id
            rec.feed_id = random.randint(0, 101)
            rec.feed_item_id = random.randint(0, 101)
            rec.rec_src = 'test_TS'
            recs.append(rec)

        return recs

    async def test_thompson_sampling(self):
        self.clickdataTable.put_item(Item={
            "mod_item": "home/999999",
            "clicks": "99",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        self.clickdataTable.put_item(Item={
            "mod_item": "home/666666",
            "clicks": "66",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        self.clickdataTable.put_item(Item={
            "mod_item": "home/333333",
            "clicks": "33",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        recs = self.generate_recommendations(["333333", "666666", "999999"])

        # goal of test is to rank by CTR over ntrials
        # order should be 999999, 666666, 333333
        ntrials = 36
        ranks = dict()
        for i in range(ntrials):
            sampled_recs = await TopicRecommendationsModelUtils.thompson_sampling(recs, RecommendationModules.HOME)
            c = 1
            for rec in sampled_recs:
                # compute average positional rank over the trials
                ranks[rec.item_id] = ranks.get(rec.item_id, 0) + (c / ntrials)
                c += 1

        final_ranks = sorted(ranks.items(), key=itemgetter(1))

        assert final_ranks[0][0] == "999999"
        assert final_ranks[1][0] == "666666"
        assert final_ranks[2][0] == "333333"


    async def test_missing_clickdata(self):
        self.clickdataTable.put_item(Item={
            "mod_item": "home/999999",
            "clicks": "99",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        recs = self.generate_recommendations(["333333", "999999"])

        sampled_recs = await TopicRecommendationsModelUtils.thompson_sampling(recs, RecommendationModules.HOME)

        assert len(sampled_recs) == 2

