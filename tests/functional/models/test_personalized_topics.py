import json
import os
import unittest

from aioresponses import aioresponses

import app.config
from app.models.personalized_topic_list import PersonalizedTopicList
from app.exceptions.personalization_error import PersonalizationError


class TestPersonalizedTopics(unittest.IsolatedAsyncioTestCase):

    async def _read_json_asset(self, filename: str):
        with open(os.path.join(app.config.ROOT_DIR, 'tests/assets/json/', filename)) as f:
            return json.load(f)

    async def test_parse_obj(self):
        fixture = await self._read_json_asset("recit_full_user_profile.json")
        personalized_topics = PersonalizedTopicList.parse_recit_response("1234", fixture)

        assert len(personalized_topics.curator_topics) == 16
        assert personalized_topics.curator_topics[0].curator_topic_label == 'Technology'

    @aioresponses()
    async def test_get(self, mocked):
        user_id = '123'
        url = f'{app.config.recit["endpoint_url"]}/v1/user_profile/{user_id}?predict_topics=true'
        fixture = await self._read_json_asset("recit_full_user_profile.json")

        mocked.get(url, status=200, payload=fixture)

        personalized_topics = await PersonalizedTopicList.get(user_id)
        assert len(personalized_topics.curator_topics) == 16

    async def test_get_none_user_id(self):
        # Assert PersonalizedTopicList.get raises PersonalizationError when user_id is None
        with self.assertRaises(PersonalizationError) as context:
            await PersonalizedTopicList.get(user_id=None)

    @aioresponses()
    async def test_get_404(self, mocked):
        user_id = '123'
        url = f'{app.config.recit["endpoint_url"]}/v1/user_profile/{user_id}?predict_topics=true'

        mocked.get(url, status=404)

        # Assert PersonalizedTopicList.get raises PersonalizationError when recit responds with a 404 status
        with self.assertRaises(PersonalizationError) as context:
            await PersonalizedTopicList.get(user_id)

    @aioresponses()
    async def test_get_500(self, mocked):
        user_id = '123'
        url = f'{app.config.recit["endpoint_url"]}/v1/user_profile/{user_id}?predict_topics=true'

        mocked.get(url, status=500)

        with self.assertRaises(Exception):
            await PersonalizedTopicList.get(user_id)
