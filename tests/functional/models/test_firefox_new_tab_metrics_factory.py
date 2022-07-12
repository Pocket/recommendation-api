import json
import os
import pytest
from functools import partial
from unittest.mock import MagicMock

from aws_xray_sdk import global_sdk_config
from botocore.exceptions import BotoCoreError

import app.config
from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory
from tests.mocks.feature_store_mock import FeatureStoreMock


@pytest.mark.asyncio  # This pytest-asyncio decorator allows us to use an async side_effect
class TestFirefoxNewTabMetricsFactory:

    SLATE_ID = 'f99178fb-6bd0-4fa1-8109-cda181b697f6'  # Matches the slate_id in firefox_new_tab_engagement.json
    feature_group_name: str = FirefoxNewTabMetricsFactory.get_feature_group_name()

    async def test_get_existing_records(self, monkeypatch):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        feature_store_mock = self._get_feature_store_mock()
        metrics_client = FirefoxNewTabMetricsFactory(aioboto3_session=feature_store_mock.aioboto3)
        recommendation_ids = [f"00000000-0000-0000-0000-00000000000{i}" for i in range(10)]

        new_tab_engagement = await metrics_client.get(recommendation_ids=recommendation_ids)

        # Check that the return value is a dict with Firefox metric models.
        assert set(new_tab_engagement.keys()) == set(recommendation_ids)
        # Get the client that was created in the 'with' statement
        with_client = await feature_store_mock.client().__aenter__()
        assert with_client.get_record.call_count == len(recommendation_ids)

        for recommendation_id in recommendation_ids:
            engagement = new_tab_engagement[recommendation_id]
            assert engagement.id == recommendation_id
            assert engagement.slate_id == self.SLATE_ID
            assert engagement.trailing_1_day_impressions == 100000  # All fixtures records have 100,000 impressions

            # Assert that get_record was called with the right arguments for each recommendation_id
            with_client.get_record.assert_any_call(
                FeatureGroupName=FirefoxNewTabMetricsFactory.get_feature_group_name(),
                RecordIdentifierValueAsString=recommendation_id,
                FeatureNames=FirefoxNewTabMetricsFactory._FEATURE_NAMES,
            )

    async def test_get_non_existing_records(self, monkeypatch):
        """
        Test that None is returned when querying a record that does not exist.
        """
        metrics_client = FirefoxNewTabMetricsFactory(aioboto3_session=self._get_feature_store_mock().aioboto3)

        # The fixture data does not have a record with id == -1
        existing_recommendation_ids = [f"00000000-0000-0000-0000-00000000000{i}" for i in range(0, 2)]
        queried_recommendation_ids = list(existing_recommendation_ids) + ['non-existing-uuid']

        new_tab_engagement = await metrics_client.get(recommendation_ids=queried_recommendation_ids)

        # Check that only the existing content ids are returned.
        assert set(new_tab_engagement.keys()) == set(existing_recommendation_ids)
        # Metrics for existing content ids should be returned successfully.
        for recommendation_id in existing_recommendation_ids:
            engagement = new_tab_engagement[recommendation_id]
            assert engagement.id == recommendation_id
            assert engagement.slate_id == self.SLATE_ID
            assert engagement.trailing_1_day_impressions >= 100  # All fixtures have at least 100 impressions

    async def test_get_non_existing_feature_group(self, monkeypatch):
        """
        Test that querying a non-existing feature group raises an exception.
        """
        metrics_client = FirefoxNewTabMetricsFactory(
            aioboto3_session=self._get_feature_store_mock(
                # Simulate a mismatch between the existing store and the one referenced in FirefoxNewTabMetricsFactory.
                feature_group_name='new-version123'
            ).aioboto3
        )
        content_ids = [str(i) for i in range(2)]

        # Assert that the exception bubbles up when the feature group does not exist.
        # In reality FeatureStore raises a ClientError, but the BotoCoreError is easier to construct for testing.
        with pytest.raises(BotoCoreError):
            await metrics_client.get(recommendation_ids=content_ids)

    def _get_feature_store_mock(self, feature_group_name=None):
        if feature_group_name is None:
            feature_group_name = FirefoxNewTabMetricsFactory.get_feature_group_name()

        return FeatureStoreMock(
            feature_group_name=feature_group_name,
            records_json_path=os.path.join(app.config.ROOT_DIR, 'tests/assets/json/firefox_new_tab_engagement.json')
        )
