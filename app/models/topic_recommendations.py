import asyncio

from aws_xray_sdk.core import xray_recorder
from pydantic import BaseModel
from typing import List

from app.models.clickdata import ClickdataModel
from app.models.recommendation import RecommendationModel, RecommendationType
from app.models.topic import TopicModel, PageType
from app.rankers.algorithms import spread_publishers, thompson_sampling


class TopicRecommendationsModel(BaseModel):
    """
    A meta class that contains two lists of recommendations - curated and algorithmic. These lists are not guaranteed
    to contain recommendations, e.g. if the requested topic is an editorial collection, no algorithmic recommendations
    will be retrieved.
    """
    curated_recommendations: List[RecommendationModel] = []
    algorithmic_recommendations: List[RecommendationModel] = []


class TopicRecommendationsModelUtils:
    @staticmethod
    @xray_recorder.capture('models_topic_dedupe')
    def dedupe(topic_recs_model: TopicRecommendationsModel) -> TopicRecommendationsModel:
        """
        If a recommendation exists in both the curated and algorithmic lists, removes that recommendation from the
        algorithmic list (favoring the curated list).

        :param topic_recs_model: an object containing collections of curated and algorithmic recommendations
        :return: the same object, with entries in the curated collection removed from the algorithmic collection
        """

        # are there dupes?
        curated_item_ids = {x.item.item_id for x in topic_recs_model.curated_recommendations}
        algorithmic_item_ids = {x.item.item_id for x in topic_recs_model.algorithmic_recommendations}

        dupes = set(curated_item_ids) & set(algorithmic_item_ids)

        if dupes:
            # if there are dupes, remove the duplicates from the algorithmic recs
            topic_recs_model.algorithmic_recommendations = list(
                filter(lambda rec: rec.item.item_id not in curated_item_ids,
                       topic_recs_model.algorithmic_recommendations))

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