import logging

import aioboto3
from aiocache import caches

from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from pydantic import BaseModel
from typing import List, Dict, Any

from app.config import dynamodb as dynamodb_config
import app.cache
from app.models.candidate import Candidate


class CandidateSetModel(BaseModel):
    candidates: List[Candidate]
    id: str
    created_at: int = None
    version: int

    @staticmethod
    @xray_recorder.capture_async('model_candidate_set_verify_candidate_set')
    async def verify_candidate_set(cs_id: str) -> bool:
        response = await CandidateSetModel._query_by_id(cs_id)
        if not response['Items']:
            return False

        return True


    @staticmethod
    @xray_recorder.capture_async('models.candidate_set._query_by_id')
    async def get(cs_id: str) -> 'CandidateSetModel':
        response = await CandidateSetModel._cached_query_by_id(cs_id)
        if not response['Items']:
            raise KeyError(f'candidate set id {cs_id} was not found in the database')

        candidate_set = response['Items'][0]
        instance = CandidateSetModel.parse_obj(candidate_set)

        return instance

    @staticmethod
    @xray_recorder.capture_async('models.candidate_set.get')
    async def _cached_query_by_id(cs_id: str) -> Dict[str, Any]:
        """
        Wrap the _query_by_id function in a cache.
        A nicer solution would be to use the aiocache decorator, but it raises a "different loop" error,
        because the decorator is called before FastAPI starts.
        :param cs_id: Candidate Set id
        :return: Candidate Set model
        """
        cache = caches.get(app.cache.candidate_set_alias)

        key = f'candidate_set:{cs_id}'
        value = await cache.get(key)
        if value is not None:
            return value

        result = await CandidateSetModel._query_by_id(cs_id)

        await cache.set(key, result)
        return result

    @staticmethod
    @xray_recorder.capture_async('models.candidate_set._query_by_id')
    async def _query_by_id(cs_id: str) -> Dict[str, Any]:
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['recommendation_api_candidate_sets_table'])
            key_condition = Key('id').eq(cs_id)
            response = await table.query(KeyConditionExpression=key_condition)
        return response
