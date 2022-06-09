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


# All RecIt CandidateSets are prefixed with this
RECIT_PREFIX = "recit-personalized"

# The keys represent valid names for use in RecsAPI, the corresponding values are the module names for RecIt.
RECIT_MODULES = {'bestof': 'recsapi_bestof', 'syndicated': 'recsapi_syndicated', 'curated': 'recsapi_curated'}
RECIT_LIMIT = 60


class RecItCandidateSet(CandidateSetModel):

    @staticmethod
    def _get_module(cs_id: str) -> str:
        """Return the RecIt module name for a given `cs_id`."""
        _, module = cs_id.split('/')
        return RECIT_MODULES[module]

    @staticmethod
    def _verify_candidate_set(cs_id: str) -> bool:
        """Verify that `cs_id` is composed of `RECIT_PREFIX`/`RECIT_MODULES`"""
        if not cs_id.startswith(RECIT_PREFIX):
            return False
        try:
            RecItCandidateSet._get_module(cs_id)
            return True
        except KeyError:
            return False

    @staticmethod
    async def verify_candidate_set(cs_id: str) -> bool:
        """Async version of _verify_candidate_set"""
        return RecItCandidateSet._verify_candidate_set(cs_id)

    @staticmethod
    @xray_recorder.capture_async('models.recit_candidate_set.get')
    async def get(cs_id: str, user_id: str) -> "RecItCandidateSet":
        """Get a candidateSet personalized for a user from RecIt. This makes a network call to RecIt.
        :param cs_id: string identifying which candidateSet to fetch from RecIt. Format is `RECIT_PREFIX`/`RECIT_MODULES`.
        :param user_id string of the target user_id

        :returns If a profile exists for `user_id`, a candidateSet populated with items pertaining to the users interest.
        If no profile exists an empty candidateSet is returned.

        :raises `ValueError` if `cs_id` is unsupported or `user_id` is missing.
        """
        if not user_id:
            raise ValueError("user_id must be provided for personalized slates")

        if not RecItCandidateSet._verify_candidate_set(cs_id):
            raise ValueError(f"Unsupported cs_id {cs_id}")

        recit_module_name = RecItCandidateSet._get_module(cs_id)

        #TODO: There should really just be one session shared, not sure how to do this in gunicorn thou
        async with aiohttp.ClientSession() as session:
            async with session.getSlate(f'{recit_config["endpoint_url"]}/v1/module/{recit_module_name}/0',
                                        params={"user_id": user_id, "limit": RECIT_LIMIT}) as resp:
                if resp.status == 200:
                    return RecItCandidateSet.parse_recit_response(cs_id, await resp.json())
                else:
                    logging.warning("RecIt error with status (%s): %s", resp.status, resp.content)
                    return RecItCandidateSet(candidates=[], id=cs_id, version=1)

    @staticmethod
    def parse_recit_response(cs_id: str, response: Dict) -> "RecItCandidateSet":
        """Transforms a RecIt response to a CandidateSet. We set publisher to '0' since RecIt doesn't currently return
        publishers."""
        candidates = [Candidate(item_id=r["resolved_id"], publisher="0") for r in response["items"]]
        return RecItCandidateSet(candidates=candidates, id=cs_id, version=1)


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
        cache = caches.getSlate(app.cache.candidate_set_alias)

        key = f'candidate_set:{cs_id}'
        value = await cache.getSlate(key)
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
        async with aioboto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url']) as dynamodb:
            table = await dynamodb.Table(dynamodb_config['candidate_sets']['table'])
            key_condition = Key('id').eq(cs_id)
            response = await table.query(KeyConditionExpression=key_condition)

        return response


def candidate_set_factory(candidate_set_id: str) -> Union[Type[RecItCandidateSet], Type[DynamoDBCandidateSet]]:
    """Given a `candidate_set_id`, return the class that can fetch those candidates."""
    if candidate_set_id.startswith(RECIT_PREFIX):
        return RecItCandidateSet
    else:
        return DynamoDBCandidateSet
