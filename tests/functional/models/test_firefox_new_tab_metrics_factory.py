import json
import os
import pytest
from functools import partial
from unittest.mock import MagicMock

from aws_xray_sdk import global_sdk_config
from botocore.exceptions import BotoCoreError

import app.config
from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory


@pytest.mark.asyncio  # This pytest-asyncio decorator allows us to use an async side_effect
class TestFirefoxNewTabMetricsFactory:

    SLATE_ID = 'f99178fb-6bd0-4fa1-8109-cda181b697f6'  # Matches the slate_id in firefox_new_tab_engagement.json
    feature_group_name: str = FirefoxNewTabMetricsFactory.get_feature_group_name()

    def setup(self):
        global_sdk_config.set_sdk_enabled(False)
        records = self._read_json_asset('firefox_new_tab_engagement.json')
        # Map id to record (use record[0] assuming that ID is the first feature in the above json fixture)
        self._firefox_new_tab_engagement_record_by_id = {record[0]['ValueAsString']: record for record in records}

    async def _get_mocked_feature_store_client(self, monkeypatch):
        # Mock boto3. Localstack currently does not support Feature Group, so we need to mock it ourselves.
        client = MagicMock()
        aioboto3 = MagicMock(client=client)
        monkeypatch.setattr("app.models.metrics.firefox_new_tab_metrics_factory.aioboto3", aioboto3)
        # Mock return values for 'get_record' calls.
        # Use partial pass in 'self' so it can access attributes loaded during setup.
        client.return_value.__aenter__.return_value.get_record.side_effect = \
            partial(self._feature_store_get_record_stub, self)
        return client

    def _read_json_asset(self, filename: str):
        with open(os.path.join(app.config.ROOT_DIR, 'tests/assets/json/', filename)) as f:
            return json.load(f)

    def _feature_store_get_record_stub(self, *args, **kwargs):
        """
        This function simulates the FeatureStore get_record operation.
        :param args:
        :param kwargs: get_record arguments
        :return: simplified version of get_record return value: only the record is returned (not any request metadata)
        """
        record_identifier_value_as_string = kwargs['RecordIdentifierValueAsString']
        feature_group_name = kwargs['FeatureGroupName']
        feature_names = kwargs['FeatureNames']

        if feature_group_name != self.feature_group_name:
            # Raise an exception if the feature group is not found.
            # In reality FeatureStore raises a ClientError, but the BotoCoreError is easier to construct for testing.
            raise BotoCoreError()

        full_record = self._firefox_new_tab_engagement_record_by_id.get(record_identifier_value_as_string, {})
        # Only return requested features to check that a valid model can be constructed from the requested features.
        filtered_record = [feature for feature in full_record if feature['FeatureName'] in feature_names]
        return {'Record': filtered_record}

    async def test_get_existing_records(self, monkeypatch):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        client = await self._get_mocked_feature_store_client(monkeypatch)
        recommendation_ids = [f"00000000-0000-0000-0000-00000000000{i}" for i in range(10)]

        new_tab_engagement = await FirefoxNewTabMetricsFactory().get(recommendation_ids=recommendation_ids)

        # Check that the return value is a dict with Firefox metric models.
        assert set(new_tab_engagement.keys()) == set(recommendation_ids)
        # Get the client that was created in the 'with' statement
        with_client = await client().__aenter__()
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
        client = await self._get_mocked_feature_store_client(monkeypatch)
        # The fixture data does not have a record with id == -1
        existing_recommendation_ids = [f"00000000-0000-0000-0000-00000000000{i}" for i in range(0, 2)]
        queried_recommendation_ids = list(existing_recommendation_ids) + ['non-existing-uuid']

        new_tab_engagement = await FirefoxNewTabMetricsFactory().get(recommendation_ids=queried_recommendation_ids)

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
        client = await self._get_mocked_feature_store_client(monkeypatch)
        content_ids = [str(i) for i in range(2)]
        FirefoxNewTabMetricsFactory._FEATURE_GROUP_VERSION = 123  # This version does not exist.

        # Assert that the exception bubbles up when the feature group does not exist.
        # In reality FeatureStore raises a ClientError, but the BotoCoreError is easier to construct for testing.
        with pytest.raises(BotoCoreError):
            await FirefoxNewTabMetricsFactory().get(recommendation_ids=content_ids)
