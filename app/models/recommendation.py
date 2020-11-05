from pydantic import BaseModel
import boto3
from app.config import dynamodb as dynamodb_config


class RecommendationModel(BaseModel):
    feed_item_id: str = None
    item_id: str = None
    feed_id: int = None
    rec_src: str = 'ExploreTopics'

    @staticmethod
    def dynamodb_candidate_to_recommendation(candidate: dict):
        recommendation = RecommendationModel()
        recommendation.item_id = str(candidate['item_id'])
        recommendation.feed_item_id = recommendation.rec_src + '/' + recommendation.item_id
        if 'feed_id' in candidate:
            recommendation.feed_id = candidate['feed_id']
        return recommendation

    @staticmethod
    def get_curated_recommendations(topic: str):
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
        table = dynamodb.Table(dynamodb_config['explore_topics_candidates_table'])
        response = table.scan()
        #      response = table.query

        return list(map(RecommendationModel.dynamodb_candidate_to_recommendation, response['Items'][0]['candidates']))

    @staticmethod
    def get_algorithmic_recommendations(topic: str):
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
        table = dynamodb.Table(dynamodb_config['explore_topics_candidates_table'])
        response = table.scan()
        #      response = table.query

        return list(map(RecommendationModel.dynamodb_candidate_to_recommendation, response['Items'][0]['candidates']))
