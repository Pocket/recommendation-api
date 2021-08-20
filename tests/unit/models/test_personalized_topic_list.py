import unittest

from app.models.personalized_topic_list import PersonalizedTopicList
from app.exceptions.personalization_exceptions import PersonalizationError


class TestPersonalizedTopicList(unittest.IsolatedAsyncioTestCase):

    async def test_personalization_errors(self):

        with self.assertRaises(PersonalizationError) as context:
            await PersonalizedTopicList.get(user_id=None)

        # self.assertTrue('user_id must be provided' in context.exception)

