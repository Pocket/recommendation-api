import aioboto3
from aiocache import caches

from boto3.dynamodb.conditions import Key
from pydantic import BaseModel
from typing import List, Dict, Any, Type

from app.config import dynamodb as dynamodb_config
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


def candidate_set_factory(candidate_set_id: str) -> Type[DynamoDBCandidateSet]:
    """Given a `candidate_set_id`, return the class that can fetch those candidates."""
    return DynamoDBCandidateSet
