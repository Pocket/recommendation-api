import aioboto3

from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from pydantic import BaseModel
from typing import List

from app.config import dynamodb as dynamodb_config
from app.models.recommendation import RecommendationModel


class CandidateSetModel(BaseModel):
    candidates: List[RecommendationModel]
    id: str = None
    created_at: int = None
    version: int = None

    @staticmethod
    @xray_recorder.capture_async('model_recommendations_get_recommendations')
    async def verify_candidate_set(cs_id: str) -> bool:
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['recommendation_api_candidate_sets_table'])
            key_condition = Key('id').eq(cs_id)
            response = await table.query(IndexName='id', Limit=1, KeyConditionExpression=key_condition,
                                         ScanIndexForward=False)
        if not response['Items']:
            return False

        return True
