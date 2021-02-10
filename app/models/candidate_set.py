import aioboto3

from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from pydantic import BaseModel
from typing import List

from app.config import dynamodb as dynamodb_config
from app.models.recommendation import RecommendationModel


class CandidateSetModel(BaseModel):
    candidates: List[RecommendationModel]
    id: str
    created_at: int = None
    version: int

    @staticmethod
    @xray_recorder.capture_async('model_candidate_set_verify_candidate_set')
    async def verify_candidate_set(cs_id: str) -> bool:
        response = await CandidateSetModel.__query_by_id(cs_id)
        if not response['Items']:
            return False

        return True

    @staticmethod
    @xray_recorder.capture_async('model_candidate_set_get')
    async def get(cs_id: str) -> 'CandidateSetModel':
        response = await CandidateSetModel.__query_by_id(cs_id)
        if not response['Items']:
            raise KeyError(f'candidate set id {cs_id} was not found in the database')

        candidate_set = response['Items'][0]
        instance = CandidateSetModel.parse_obj(candidate_set)
        # We should keep an eye on performance here if/when candidate sets become large
        instance.candidates = list(map(RecommendationModel.parse_obj, candidate_set['candidates']))

        return instance

    @staticmethod
    async def __query_by_id(cs_id):
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['recommendation_api_candidate_sets_table'])
            key_condition = Key('id').eq(cs_id)
            response = await table.query(KeyConditionExpression=key_condition)
        return response


