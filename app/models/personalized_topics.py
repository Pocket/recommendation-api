import aiohttp
import logging
from aiocache import caches, decorators
from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List

import app.config
import app.cache


class PersonalizedTopicsEntry(BaseModel):
    curator_topic_label: str = None
    score: float = None

    @staticmethod
    def parse_from_list(tuple: list):
        return PersonalizedTopicsEntry.parse_obj({
            "curator_topic_label": tuple[0],
            "score": tuple[1],
        })


class PersonalizedTopics(BaseModel):
    curator_topics: List[PersonalizedTopicsEntry]

    @staticmethod
    def parse_from_response(response: dict):
        curator_topics = [PersonalizedTopicsEntry.parse_from_list(l) for l in response["curator_topics"]]
        return PersonalizedTopics(curator_topics=curator_topics)

    @staticmethod
    @xray_recorder.capture_async('algorithms.get_personalized_topics')
    async def get(user_id: str) -> 'PersonalizedTopics':
        """
        A request including the user_id is issued to RecIt which returns a list of ranked curator topic labels
        personalized to the user_id.  The output will be a list of reordered topic labels based on affinity to items
        in the user's saved list.
        :param user_id: str identifying user
        :return: List with elements [<curatorTopicLabel>, score]
        """
        if not user_id:
            raise ValueError("user_id must be provided for personalized slate lineups")

        # TODO: There should really just be one session shared, not sure how to do this in gunicorn thou
        async with aiohttp.ClientSession() as session:
            url = f'{app.config.recit["endpoint_url"]}/v1/user_profile/{user_id}?predict_topics=true'
            async with session.get(url) as resp:
                personalized_topics = {"curator_topics": []}
                if resp.status == 200:
                    response = await resp.json()
                    return PersonalizedTopics.parse_from_response(response)
                elif resp.status == 404:
                    logging.info(f"RecIt /v1/user_profile does not have a user profile for user id {user_id}")
                    # Return empty list when user does not exist in RecIt.
                    return PersonalizedTopics(curator_topics=[])
                else:
                    # Unexpected response code
                    raise Exception(f"RecIt responded with {resp.status} for {url}")
