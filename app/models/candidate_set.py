import aioboto3
import aiohttp
from aiocache import caches
import logging

from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from pydantic import BaseModel
from typing import List, Dict, Any, Union, Type

from app.config import dynamodb as dynamodb_config, recit as recit_config
import app.cache
from app.models.candidate import Candidate


class CandidateSetModel(BaseModel):
    """
    Models a candidate set.
    """
    candidates: List[Candidate]
    id: str
    created_at: int = None
    version: int

    @staticmethod
    async def verify_candidate_set(cs_id: str) -> bool:
        raise NotImplemented


class DynamoDBCandidateSet(CandidateSetModel):
    @staticmethod
    @xray_recorder.capture_async('models.dynamodb_candidate_set.verify_candidate_set')
    async def verify_candidate_set(cs_id: str) -> bool:
        """
        Ensures the given candidate set exists in the database

        :param cs_id: string id of the candidate set
        :return: boolean
        """
        response = await DynamoDBCandidateSet._query_by_id(cs_id)
        if not response['Items']:
            return False

        return True

    @staticmethod
    @xray_recorder.capture_async('models.dynamodb_candidate_set.get')
    async def get(cs_id: str, user_id: str = None) -> 'DynamoDBCandidateSet':
        """
        Retrieves a candidate set from the database and instantiates a CandidateSetModel

        :param cs_id: string id of the candidate set
        :return: A CandidateSetModel object
        """
        response = await DynamoDBCandidateSet._cached_query_by_id(cs_id)
        if not response['Items']:
            raise KeyError(f'candidate set id {cs_id} was not found in the database')

        return DynamoDBCandidateSet.parse_obj(response['Items'][0])

    @staticmethod
    @xray_recorder.capture_async('models.dynamodb_candidate_set._cached_query_by_id')
    async def _cached_query_by_id(cs_id: str) -> Dict[str, Any]:
        """
        Wrap the _query_by_id function in a cache.
        A nicer solution would be to use the aiocache decorator, but it raises a "different loop" error,
        because the decorator is called before FastAPI starts.
        :param cs_id: Candidate Set id
        :return: Candidate Set dict
        """
        cache = caches.get(app.cache.candidate_set_alias)

        key = f'candidate_set:{cs_id}'
        value = await cache.get(key)
        if value is not None:
            return value

        result = await DynamoDBCandidateSet._query_by_id(cs_id)

        await cache.set(key, result, ttl=app.config.elasticache['candidate_set_ttl'])
        return result

    @staticmethod
    @xray_recorder.capture_async('models.dynamodb_candidate_set._query_by_id')
    async def _query_by_id(cs_id: str) -> Dict[str, Any]:
        """
        Retrieves a candidate set from the database

        :param cs_id: string id of the candidate set
        :return: dictionary database response
        """
        session = aioboto3.Session()
        async with session.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['candidate_sets']['table'])
            key_condition = Key('id').eq(cs_id)
            response = await table.query(KeyConditionExpression=key_condition)

        return response
