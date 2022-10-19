import os
import pytest

from aws_xray_sdk import global_sdk_config

import app.config
from app.data_providers.user_impression_cap_provider import UserImpressionCapProvider
from app.models.user_ids import UserIds
from tests.mocks.feature_store_mock import FeatureStoreMock


@pytest.mark.asyncio  # This pytest-asyncio decorator allows us to use an async side_effect
class TestUserImpressionCapProvider:

    HASHED_USER_ID = 'aaaaaaaaaaaaaaa123'

    def setup(self):
        global_sdk_config.set_sdk_enabled(False)

        self.feature_store_mock = FeatureStoreMock(
            feature_group_name=UserImpressionCapProvider.get_feature_group_name(),
            records_json_path=os.path.join(app.config.ROOT_DIR, 'tests/assets/json/user_impressions_v2.json')
        )

        # This is the client that's under test.
        self.client = UserImpressionCapProvider(aioboto3_session=self.feature_store_mock.aioboto3)

    async def test_get_existing_records(self):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        corpus_items = await self.client.get(
            user_ids=UserIds(hashed_user_id=self.HASHED_USER_ID)
        )

        # Assert corpus_items reflect the user_impressions_v2.json fixture data.
        assert len(corpus_items) == 2
        assert corpus_items[0].id == '1697212b-1065-4e60-839d-c399882a0977'
        assert corpus_items[1].id == '357e1f96-617e-4ece-aa21-a9cc74a457a2'

    async def test_get_non_existing_record(self):
        corpus_items = await self.client.get(user_ids=UserIds(hashed_user_id='i-do-not-exist'))

        assert [] == corpus_items
