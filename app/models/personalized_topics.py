import aiohttp
import logging
from aiocache import caches, decorators
from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List, Dict

import app.config
import app.cache


class PersonalizedTopicElement(BaseModel):
    curator_topic_label: str
    score: float

class PersonalizedTopicList(BaseModel):
    curator_topics: List[PersonalizedTopicElement]
    user_id: str = None


    @staticmethod
    @xray_recorder.capture_async('models.personalized_topic_list.get')
    async def get(user_id: str) -> 'PersonalizedTopicList':
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
            async with session.get(f'{app.config.recit["endpoint_url"]}/v1/user_profile/{user_id}?predict_topics=true',
                                   params={"user_id": user_id}) as resp:
                if resp.status == 200:
                    j1 = await resp.json()
                    return PersonalizedTopicList.parse_recit_response(user_id, j1)
                else:
                    logging.warning("RecIt error with status (%s): %s", resp.status, resp.content)
                    return []


    @staticmethod
    def parse_recit_response(user_id: str, response: Dict, usr) -> "PersonalizedTopicList":
        """Transforms a RecIt response to a PersonalizedTopicList."""
        # this list should be ordered by score descending and order must be preserved for ranking
        personalized_topics = [PersonalizedTopicElement(curator_topic_label=x[0], score=x[1])
                               for x in response["curator_topics"]]
        return PersonalizedTopicList(curator_topics=personalized_topics, user_id=user_id)
