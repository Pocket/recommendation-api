from pydantic import BaseModel
from typing import List
from app.models.recommendation import RecommendationModel, RecommendationType


class TopicRecommendationsModel(BaseModel):
    curated_recommendations: List[RecommendationModel] = []
    algorithmic_recommendations: List[RecommendationModel] = []

    @staticmethod
    def get_recommendations(slug: str) -> ['TopicRecommendationsModel']:
        topic_recommendations = TopicRecommendationsModel()
        topic_recommendations.algorithmic_recommendations = RecommendationModel.get_recommendations(
            slug=slug,
            recommendation_type=RecommendationType.ALGORITHMIC
        )
        topic_recommendations.curated_recommendations = RecommendationModel.get_recommendations(
            slug=slug,
            recommendation_type=RecommendationType.CURATED
        )

        # dedupe items in the algorithmic recommendations
        topic_recommendations = TopicRecommendationsModelUtils.dedupe(topic_recommendations)

        # TODO: Publisher spread module
        return topic_recommendations


class TopicRecommendationsModelUtils:
    @staticmethod
    def dedupe(topic_recs_model: TopicRecommendationsModel) -> ['TopicRecommendationsModel']:
        # are there dupes?
        curated_item_ids = {x.item_id for x in topic_recs_model.curated_recommendations}
        algorithmic_item_ids = {x.item_id for x in topic_recs_model.algorithmic_recommendations}

        dupes = set(curated_item_ids) & set(algorithmic_item_ids)

        if dupes:
            # if there are dupes, remove the duplicates from the algorithmic recs
            topic_recs_model.algorithmic_recommendations = filter(lambda rec: rec.item_id not in curated_item_ids,
                                                                  topic_recs_model.algorithmic_recommendations)

        return topic_recs_model
