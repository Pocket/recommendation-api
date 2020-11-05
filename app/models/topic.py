from pydantic import BaseModel
import boto3
from app.config import dynamodb as dynamodb_config


class TopicModel(BaseModel):
    display_name: str
    slug: str
    query: str
    curator_label: str
    is_displayed: bool
    is_promoted: bool
    social_title: str = None
    social_description: str = None
    social_image: str = None

    @staticmethod
    def get_all():
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
        table = dynamodb.Table(dynamodb_config['explore_topics_metadata_table'])
        response = table.scan()
        return response['Items']
