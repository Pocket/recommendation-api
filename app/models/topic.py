from pydantic import BaseModel
import boto3
import os


class Topic(BaseModel):
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
        dynamodb = boto3.resource('dynamodb', endpoint_url=os.getenv('AWS_DYNAMODB_ENDPOINT_URL'))
        table = dynamodb.Table('explore_topics_metadata')
        response = table.scan()
        return response['Items']
