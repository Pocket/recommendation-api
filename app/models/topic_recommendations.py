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

        # TODO: Dedupe the items between result sets
        # TODO: Publisher spread module

        return topic_recommendations


