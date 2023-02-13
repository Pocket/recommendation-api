from asyncio import gather

from enum import Enum
from pydantic import BaseModel, Field

from app.config import dynamodb as dynamodb_config
from app.models.candidate_set import candidate_set_factory
from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory
from app.models.metrics.recommendation_metrics_factory import RecommendationMetricsFactory
from app.models.item import ItemModel
from app.models.slate_experiment import SlateExperimentModel
from app.rankers import get_ranker, POCKET_THOMPSON_SAMPLING_RANKERS, FIREFOX_THOMPSON_SAMPLING_RANKERS


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
    id: str = Field(
        description='A generated id from the Data and Learning team that represents the Recommendation')
    feed_item_id: str = Field(
        default=None,
        description='A generated id from the Data and Learning team that represents the Recommendation - Deprecated')
    feed_id: int = Field(
        default=None,
        description='The feed id from mysql that this item was curated from (if it was curated)')
    item_id: str = Field(
        description='The ID of the item this recommendation represents\n'
                    'TODO: Use apollo federation to turn this into an Item type.')
    item: ItemModel = Field(description='The Item that is resolved by apollo federation using the itemId')
    rec_src: str = Field(default='RecommendationAPI', description='The source of the recommendation')
    publisher: str = Field(default=None, description='The publisher of the item')

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
            recommendations = get_ranker(ranker)(recommendations, **ranker_kwargs)

        return recommendations
