from pydantic import BaseModel
import boto3
from boto3.dynamodb.conditions import Key
from app.config import dynamodb as dynamodb_config
from app.models.topic import TopicModel
from enum import Enum


class RecommendationType(Enum):
    COLLECTION = 'collection'
    CURATED = 'curated'
    ALGORITHMIC = 'algorithmic'


class RecommendationModel(BaseModel):
    feed_item_id: str = None
    item_id: str = None
    feed_id: int = None
    rec_src: str = 'ExploreTopics'
    publisher: str = None

    @staticmethod
    def dynamodb_candidate_to_recommendation(candidate: dict):
        recommendation = RecommendationModel().parse_obj(candidate)
        recommendation.feed_item_id = recommendation.rec_src + '/' + recommendation.item_id
        return recommendation

    @staticmethod
    def get_recommendations(topic_id: str, recommendation_type: RecommendationType) -> ['RecommendationModel']:
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
        table = dynamodb.Table(dynamodb_config['explore_topics_candidates_table'])
        response = table.query(IndexName='topic_id-type', Limit=1,
                               KeyConditionExpression=Key('topic_id-type').eq(
                                   topic_id + '|' + recommendation_type.value),
                               ScanIndexForward=False)
        if not response['Items']:
            return []
        # assume 'candidates' below contains publisher
        return list(map(RecommendationModel.dynamodb_candidate_to_recommendation, response['Items'][0]['candidates']))
