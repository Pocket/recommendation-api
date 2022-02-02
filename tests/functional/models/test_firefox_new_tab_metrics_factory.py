import json
import os
import pytest
from functools import partial
from unittest.mock import MagicMock, AsyncMock

from aws_xray_sdk import global_sdk_config
from botocore.exceptions import BotoCoreError

pytest.importorskip("aioboto3")

import app.config
from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory


class FeatureStoreClient:
    def __init__(self, **kwargs):
        pass
    async def get_record(self, **kwargs):
        pass


@pytest.mark.asyncio
class TestFirefoxNewTabMetricsFactory:

    SLATE_ID = '0737b00e-a21e-4875-a4c7-3e14926d4acf'
    feature_group_name: str

    def setup(self):
        global_sdk_config.set_sdk_enabled(False)
        self._firefox_new_tab_engagement_fixture = self._read_json_asset('firefox_new_tab_engagement.json')
        self.feature_group_name = FirefoxNewTabMetricsFactory.get_feature_group_name()

    async def _get_mocked_feature_store_client(self, monkeypatch):
        # Mock boto3. Localstack currently does not support Feature Group, so we need to mock it ourselves.
        client = MagicMock()  # AsyncMock(FeatureStoreClient)
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
        RecordIdentifierValueAsString = kwargs['RecordIdentifierValueAsString']
        FeatureGroupName = kwargs['FeatureGroupName']

        if FeatureGroupName != self.feature_group_name:
            # In reality FeatureStore raises a ClientError, but the BotoCoreError is easier to construct for testing.
            raise BotoCoreError()

        return self._firefox_new_tab_engagement_fixture.get(RecordIdentifierValueAsString, {})

    async def test_get_existing_records(self, monkeypatch):
        """
        Test the case where the queried records exist in the Feature Group.
        """
        client = await self._get_mocked_feature_store_client(monkeypatch)
        content_ids = [str(i) for i in range(10)]

        new_tab_engagement = await FirefoxNewTabMetricsFactory().get(
            slate_id=self.SLATE_ID,
            content_ids=content_ids,
        )

        # Check that the return value is a dict with Firefox metric models.
        assert set(new_tab_engagement.keys()) == set(content_ids)
        for content_id in content_ids:
            engagement = new_tab_engagement[content_id]
            assert engagement.id == f'{content_id}/{self.SLATE_ID}'
            assert engagement.slate_id == self.SLATE_ID
            assert engagement.trailing_15_minute_impressions >= 100  # All fixtures have at least 100 impressions

        # Get the client that was created in the 'with' statement
        with_client = await client().__aenter__()
        assert with_client.get_record.call_count == len(content_ids)
        # Assert that get_record was called with the right arguments for each content_id
        for content_id in content_ids:
            with_client.get_record.assert_any_call(
                FeatureGroupName=FirefoxNewTabMetricsFactory.get_feature_group_name(),
                RecordIdentifierValueAsString=f'{content_id}/{self.SLATE_ID}',
                FeatureNames=FirefoxNewTabMetricsFactory._FEATURE_NAMES,
            )

    async def test_get_non_existing_records(self, monkeypatch):
        """
        Test that None is returned when querying a record that does not exist.
        """
        client = await self._get_mocked_feature_store_client(monkeypatch)
        # The fixture data does not have a record with id == -1
        queried_content_ids = [str(i) for i in range(-1, 2)]

        new_tab_engagement = await FirefoxNewTabMetricsFactory().get(
            slate_id=self.SLATE_ID,
            content_ids=queried_content_ids,
        )

        existing_content_ids = [content_id for content_id in queried_content_ids if int(content_id) >= 0]
        # Check that only the existing content ids are returned.
        assert set(new_tab_engagement.keys()) == set(existing_content_ids)
        # Metrics for existing content ids should be returned successfully.
        for content_id in existing_content_ids:
            engagement = new_tab_engagement[content_id]
            assert engagement.id == f'{content_id}/{self.SLATE_ID}'
            assert engagement.slate_id == self.SLATE_ID
            assert engagement.trailing_15_minute_impressions >= 100  # All fixtures have at least 100 impressions

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
            await FirefoxNewTabMetricsFactory().get(
                slate_id=self.SLATE_ID,
                content_ids=content_ids,
            )
