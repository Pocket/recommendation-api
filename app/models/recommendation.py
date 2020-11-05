from pydantic import BaseModel
import boto3
from app.config import dynamodb as dynamodb_config


class Recommendation(BaseModel):
    feed_item_id: str
    item_id: str
    feed_id: int

    @staticmethod
    def get_curated_topic(topic: str):
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
        table = dynamodb.Table(dynamodb_config['explore_topics_candidate_table'])
        response = table.scan()
        return response['Items']

    @staticmethod
    def get_algorithmic_topic(topic: str):
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
        table = dynamodb.Table(dynamodb_config['explore_topics_candidates_table'])
        response = table.scan()
        return response['Items']
