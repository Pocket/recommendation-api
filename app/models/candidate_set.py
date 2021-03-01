import aioboto3

from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from pydantic import BaseModel
from typing import List, Dict, Any

from app.config import dynamodb as dynamodb_config


class CandidateSetModel(BaseModel):
    """
    Models a candidate set.
    """
    candidates: List[Dict[str, Any]]
    id: str
    created_at: int = None
    version: int

    @staticmethod
    @xray_recorder.capture_async('model_candidate_set_verify_candidate_set')
    async def verify_candidate_set(cs_id: str) -> bool:
        """
        Ensures the given candidate set exists in the database

        :param cs_id: string id of the candidate set
        :return: boolean
        """
        response = await CandidateSetModel.__query_by_id(cs_id)
        if not response['Items']:
            return False

        return True

    @staticmethod
    @xray_recorder.capture_async('model_candidate_set_get')
    async def get(cs_id: str) -> 'CandidateSetModel':
        """
        Retrieves a candidate set from the database and instantiates a CandidateSetModel

        :param cs_id: string id of the candidate set
        :return: A CandidateSetModel object
        """
        response = await CandidateSetModel.__query_by_id(cs_id)
        if not response['Items']:
            raise KeyError(f'candidate set id {cs_id} was not found in the database')

        return CandidateSetModel.parse_obj(response['Items'][0])

    @staticmethod
    async def __query_by_id(cs_id):
        """
        Retrieves a candidate set from the database

        :param cs_id: string id of the candidate set
        :return: dictionary database response
        """
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['recommendation_api_candidate_sets_table'])
            key_condition = Key('id').eq(cs_id)
            response = await table.query(KeyConditionExpression=key_condition)

        return response


