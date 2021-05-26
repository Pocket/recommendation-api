import json
import os
import unittest

import aiohttp
import responses
import requests.exceptions

import app.config
from app.models.personalized_topics import PersonalizedTopics


class TestClickdataModel(unittest.IsolatedAsyncioTestCase):

    async def _read_json_asset(self, filename: str):
        with open(os.path.join(app.config.ROOT_DIR, 'tests/assets/json/', filename)) as f:
            return json.load(f)

    async def test_parse_obj(self):
        fixture = await self._read_json_asset("recit_full_user_profile.json")
        personalized_topics = PersonalizedTopics.parse_from_response(fixture)

        assert len(personalized_topics.curator_topics) == 16
        assert personalized_topics.curator_topics[0].curator_topic_label == 'Technology'

    @responses.activate
    async def test_get(self):
        user_id = '123'
        url = f'{app.config.recit["endpoint_url"]}/v1/user_profile/{user_id}?predict_topics=true'
        fixture = await self._read_json_asset("recit_full_user_profile.json")
        responses.add(responses.GET, url, status=200, json=fixture)

        personalized_topics = await PersonalizedTopics.get(user_id)
        assert len(personalized_topics.curator_topics) == 16

    @responses.activate
    async def test_get_404(self):
        user_id = '123'
        url = f'{app.config.recit["endpoint_url"]}/v1/user_profile/{user_id}?predict_topics=true'
        responses.add(responses.GET, url, status=404)

        personalized_topics = await PersonalizedTopics.get(user_id)
        assert len(personalized_topics.curator_topics) == 0

    @responses.activate
    async def test_get_500(self):
        user_id = '123'
        url = f'{app.config.recit["endpoint_url"]}/v1/user_profile/{user_id}?predict_topics=true'
        responses.add(responses.GET, url, status=500)

        with self.assertRaises(Exception):
            await PersonalizedTopics.get(user_id)
