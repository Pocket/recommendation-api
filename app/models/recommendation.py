import aioboto3

from asyncio import gather

import logging
from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from enum import Enum
from pydantic import BaseModel

from app.config import dynamodb as dynamodb_config
# Needs to exist for pydantic to resolve the model field "item: ItemModel" in the RecommendationModel
from app.graphql.item import Item
from app.models.candidate_set import candidate_set_factory
from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory
from app.models.metrics.recommendation_metrics_factory import RecommendationMetricsFactory
from app.models.item import ItemModel
from app.models.slate_experiment import SlateExperimentModel
from app.models.user_impressed_list import UserImpressedList
from app.rankers import get_ranker, POCKET_THOMPSON_SAMPLING_RANKERS, FIREFOX_THOMPSON_SAMPLING_RANKERS, \
    PERSONALIZED_IMPRESSION_RANKERS


class RecommendationType(Enum):
    """
    Defines the possible types of recommendations.
    """
    COLLECTION = 'collection'
    CURATED = 'curated'
    ALGORITHMIC = 'algorithmic'


class RecommendationModel(BaseModel):
    """
    A recommendation models a single article. The properties here are the bare minimum necessary to represent an
    article. The `item` property contains all article details, e.g. title, excerpt, image, etc.
    """
    id: str = None
    feed_item_id: str = None
    feed_id: int = None
    item_id: str
    item: ItemModel
    rec_src: str = 'RecommendationAPI'
    publisher: str = None

    @staticmethod
    def candidate_dict_to_recommendation(candidate: dict):
        """
        Instantiate and populate a RecommendationModel object.
        :param candidate: a dictionary returned from dynamo db
        :return: RecommendationModel instance
        """
        recommendation = RecommendationModel(
            feed_id=candidate.get('feed_id'),
            publisher=candidate.get('publisher'),
            item_id=candidate.get('item_id'),
            item=ItemModel(item_id=candidate.get('item_id'))
        )
        recommendation.id = recommendation.rec_src + '/' + recommendation.item.item_id
        recommendation.feed_item_id = recommendation.id
        return recommendation

    @staticmethod
    async def get_recommendations_from_experiment(
            slate_id: str, experiment: SlateExperimentModel, user_id: str) -> ['RecommendationModel']:
        """
        Retrieves a list of RecommendationModel objects for on the given slate experiment.
        :param slate_id: The id of the slate to which this experiment belongs
        :param experiment: a SlateExperimentModel instance
        :param user_id: ID of the user to generate recommendations for
        :return: a list of RecommendationModel instances
        """
        # for each candidate set id, get the candidate set record from the db
        candidate_sets = await gather(
            *(candidate_set_factory(cs_id).get(cs_id, user_id) for cs_id in experiment.candidate_sets))

        recommendations = []
        # get the recommendations
        for candidate_set in candidate_sets:
            for candidate in candidate_set.candidates:
                recommendations.append(RecommendationModel.candidate_dict_to_recommendation(candidate.dict()))

        # apply rankers from the slate experiment on the candidate set's candidates
        for ranker in experiment.rankers:
            ranker_kwargs = {}
            if ranker in POCKET_THOMPSON_SAMPLING_RANKERS:
                # Thompson sampling requires click/impression data
                ranker_kwargs = {
                    'metrics': await RecommendationMetricsFactory(dynamodb_config["endpoint_url"]).get(
                        slate_id,
                        [recommendation.item.item_id for recommendation in recommendations])
                }
            elif ranker in FIREFOX_THOMPSON_SAMPLING_RANKERS:
                # firefox Thompson sampling requires click/impression data from it's own data source
                ranker_kwargs = {
                    'metrics': await FirefoxNewTabMetricsFactory().get([rec.id for rec in recommendations])
                }
            elif ranker in PERSONALIZED_IMPRESSION_RANKERS:
                # impression filtering requires personalized impressed item lists from it's own data source
                ranker_kwargs = {
                    'user_impressed_list': await UserImpressedList().get(user_id)
                }
            recommendations = get_ranker(ranker)(recommendations, **ranker_kwargs)

        return recommendations
