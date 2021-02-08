from typing import List
import random

from app.models.topic_recommendations import TopicRecommendationsModel, TopicRecommendationsModelUtils
from app.models.recommendation import RecommendationModel


class TestRecommendationsModelUtils:
    @staticmethod
    def generate_recommendations(item_ids: List[int]) -> List[RecommendationModel]:
        recs = []
        for item_id in item_ids:
            rec = RecommendationModel()
            rec.item_id = item_id
            rec.feed_id = random.randint(0, 101)
            rec.feed_item_id = random.randint(0, 101)
            rec.rec_src = 'bowling'
            recs.append(rec)

        return recs

    def setup_class(self):
        self.curated = TestRecommendationsModelUtils.generate_recommendations([1, 2, 3, 4, 5])

    # dedupe tests
    # ------------------------------------

    def test_no_dupes(self):
        algorithmic = TestRecommendationsModelUtils.generate_recommendations([6, 7, 8, 9])
        topic_recs = TopicRecommendationsModel()
        topic_recs.curated_recommendations = self.curated
        topic_recs.algorithmic_recommendations = algorithmic
        result = TopicRecommendationsModelUtils.dedupe(topic_recs)
        algorithmic_result_ids = [x.item_id for x in result.algorithmic_recommendations]

        assert algorithmic_result_ids == [6, 7, 8, 9]

    def test_dedupes_single_item(self):
        algorithmic = TestRecommendationsModelUtils.generate_recommendations([1, 6, 7, 8, 9])
        topic_recs = TopicRecommendationsModel()
        topic_recs.curated_recommendations = self.curated
        topic_recs.algorithmic_recommendations = algorithmic
        result = TopicRecommendationsModelUtils.dedupe(topic_recs)
        algorithmic_result_ids = [res.item_id for res in result.algorithmic_recommendations]

        assert algorithmic_result_ids == [6, 7, 8, 9]

    def test_dedupes_multiple_items(self):
        algorithmic = TestRecommendationsModelUtils.generate_recommendations([1, 2, 6, 7, 8])
        topic_recs = TopicRecommendationsModel()
        topic_recs.curated_recommendations = self.curated
        topic_recs.algorithmic_recommendations = algorithmic
        result = TopicRecommendationsModelUtils.dedupe(topic_recs)
        algorithmic_result_ids = [res.item_id for res in result.algorithmic_recommendations]
        # Ensures that filter in dedupe does not break the list type of algorithmic_recommendations
        assert len(result.algorithmic_recommendations) == 3
        assert algorithmic_result_ids == [6, 7, 8]

    def test_curated_recs_untouched(self):
        algorithmic = TestRecommendationsModelUtils.generate_recommendations([1, 6, 7, 8, 9])
        topic_recs = TopicRecommendationsModel()
        topic_recs.curated_recommendations = self.curated
        topic_recs.algorithmic_recommendations = algorithmic
        result = TopicRecommendationsModelUtils.dedupe(topic_recs)
        curated_result_ids = [res.item_id for res in result.curated_recommendations]

        assert curated_result_ids == [x.item_id for x in self.curated]

    # limit_results tests
    # ------------------------------------

    def test_limits_array(self):
        algorithmic = TestRecommendationsModelUtils.generate_recommendations([1, 6, 7, 8, 9])
        topic_recs = TopicRecommendationsModel()
        topic_recs.curated_recommendations = self.curated
        topic_recs.algorithmic_recommendations = algorithmic
        result = TopicRecommendationsModelUtils.limit_results(topic_recs, curated_count=2, algorithmic_count=3)

        assert len(result.algorithmic_recommendations) == 3
        assert len(result.curated_recommendations) == 2

    def test_limits_array_when_less(self):
        algorithmic = TestRecommendationsModelUtils.generate_recommendations([1, 6, 7, 8, 9])
        topic_recs = TopicRecommendationsModel()
        topic_recs.curated_recommendations = self.curated
        topic_recs.algorithmic_recommendations = algorithmic
        result = TopicRecommendationsModelUtils.limit_results(topic_recs, curated_count=20, algorithmic_count=30)

        assert len(result.algorithmic_recommendations) == 5
        assert len(result.curated_recommendations) == 5
