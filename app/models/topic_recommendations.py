from pydantic import BaseModel
from typing import List
from app.models.recommendation import RecommendationModel, RecommendationType


class TopicRecommendationsModel(BaseModel):
    curated_recommendations: List[RecommendationModel] = []
    algorithmic_recommendations: List[RecommendationModel] = []

    @staticmethod
    def get_recommendations(slug: str, algorithmic_count: int, curated_count: int) -> ['TopicRecommendationsModel']:
        topic_recommendations = TopicRecommendationsModel()
        topic_recommendations.algorithmic_recommendations = RecommendationModel.get_recommendations(
            slug=slug,
            recommendation_type=RecommendationType.ALGORITHMIC,
        )
        topic_recommendations.curated_recommendations = RecommendationModel.get_recommendations(
            slug=slug,
            recommendation_type=RecommendationType.CURATED
        )

        # dedupe items in the algorithmic recommendations
        topic_recommendations = TopicRecommendationsModelUtils.dedupe(topic_recommendations)

        # lets limit the result set to what was requested.
        topic_recommendations = TopicRecommendationsModelUtils.limit_results(topic_recommendations,
                                                                             algorithmic_count,
                                                                             curated_count)

        # TODO: Publisher spread module
        return topic_recommendations


class TopicRecommendationsModelUtils:
    @staticmethod
    def dedupe(topic_recs_model: TopicRecommendationsModel) -> TopicRecommendationsModel:
        # are there dupes?
        curated_item_ids = {x.item_id for x in topic_recs_model.curated_recommendations}
        algorithmic_item_ids = {x.item_id for x in topic_recs_model.algorithmic_recommendations}

        dupes = set(curated_item_ids) & set(algorithmic_item_ids)

        if dupes:
            # if there are dupes, remove the duplicates from the algorithmic recs
            topic_recs_model.algorithmic_recommendations = filter(lambda rec: rec.item_id not in curated_item_ids,
                                                                  topic_recs_model.algorithmic_recommendations)

        return topic_recs_model

    @staticmethod
    def limit_results(topic_recommendations: TopicRecommendationsModel,
                      algorithmic_count: int,
                      curated_count: int
                      ) -> TopicRecommendationsModel:
        # The requester wants us to limit our results, so lets truncate the arrays
        topic_recommendations.algorithmic_recommendations = topic_recommendations.algorithmic_recommendations[
                                                            0: algorithmic_count]
        topic_recommendations.curated_recommendations = topic_recommendations.curated_recommendations[
                                                        0: curated_count]

        return topic_recommendations
