import aioboto3

from asyncio import gather
from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from enum import Enum
from pydantic import BaseModel

from app.config import dynamodb as dynamodb_config
# Needs to exist for pydantic to resolve the model field "item: ItemModel" in the RecommendationModel
from app.graphql.item import Item
from app.models.candidate_set import CandidateSetModel
from app.models.clickdata import ClickdataModel, RecommendationModules
from app.models.item import ItemModel
from app.models.slate_experiment import SlateExperimentModel
from app.rankers import get_ranker


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
    feed_item_id: str = None
    feed_id: int = None
    item_id: str
    item: ItemModel
    rec_src: str = 'RecommendationAPI'
    publisher: str = None

    @staticmethod
    def candidate_to_recommendation(candidate: dict):
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
        recommendation.feed_item_id = recommendation.rec_src + '/' + recommendation.item.item_id
        return recommendation

    @staticmethod
    @xray_recorder.capture_async('model_recommendations_get_recommendations')
    async def get_recommendations(topic_id: str, recommendation_type: RecommendationType) -> ['RecommendationModel']:
        """
        Retrieves recommendations for the given `topic_id` of the given type from dynamo db.
        :param topic_id: id of the topic we want recommendations for
        :param recommendation_type: the type of recommendations we want, e.g. algorithmic, curated
        :return: list of RecommendationModel objects
        """
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['recommendation_api_candidates_table'])
            key_condition = Key('topic_id-type').eq(topic_id + '|' + recommendation_type.value)
            response = await table.query(IndexName='topic_id-type', Limit=1, KeyConditionExpression=key_condition,
                                         ScanIndexForward=False)
        if not response['Items']:
            return []
        # assume 'candidates' below contains publisher
        return list(map(RecommendationModel.candidate_to_recommendation, response['Items'][0]['candidates']))

    @staticmethod
    async def get_recommendations_from_experiment(experiment: SlateExperimentModel) -> ['RecommendationModel']:
        """
        Retrieves a list of RecommendationModel objects for on the given slate experiment.
        :param experiment: a SlateExperimentModel instance
        :return: a list of RecommendationModel instances
        """
        candidate_sets = []
        # for each candidate set id, get the candidate set record from the db
        for candidate_set_id in experiment.candidate_sets:
            candidate_sets.append(CandidateSetModel.get(candidate_set_id))
        candidate_sets = await gather(*candidate_sets)

        recommendations = []
        # get the recommendations
        for candidate_set in candidate_sets:
            for candidate in candidate_set.candidates:
                recommendations.append(RecommendationModel.candidate_to_recommendation(candidate))

        # apply rankers from the slate experiment on the candidate set's candidates
        for ranker in experiment.rankers:
            if ranker == 'thompson-sampling':
                # thompson sampling takes two specific arguments so it needs to be handled differently
                recommendations = await RecommendationModel.__thompson_sample(recommendations)
                continue
            recommendations = get_ranker(ranker)(recommendations)

        return recommendations

    @staticmethod
    async def __thompson_sample(recommendations: ['RecommendationModel']) -> ['RecommendationModel']:
        """
        Special processing for handling the thompson sampling ranker. Retrieves click data for the items being ranked
        and uses that for thompson sampling algorithm.
        :param recommendations: a list of RecommendationModel instances
        :return: a list of RecommendationModel instances
        """
        item_ids = [recommendation.item.item_id for recommendation in recommendations]
        try:
            click_data = await ClickdataModel.get_clickdata(RecommendationModules.TOPIC, item_ids)
        except ValueError:
            rec_item_ids = ','.join(item_ids)
            print(f'click data not found for candidates with item ids: {rec_item_ids}')
            click_data = {}
        return get_ranker('thompson-sampling')(recommendations, click_data)
