import json
from functools import partial
from typing import Dict, List
from unittest.mock import MagicMock

from botocore.exceptions import BotoCoreError


class FeatureStoreMock:
    """
    Mock boto3 featurestore client. Localstack currently does not support Feature Group, so we need to mock it ourselves.
    """

    def __init__(self, feature_group_name: str, records_json_path: str):
        self.feature_group_name = feature_group_name

        with open(records_json_path) as f:
            records = json.load(f)
        self.records_by_id = {self._get_id_from_record(record): record for record in records}

        self.client = MagicMock()
        self.aioboto3 = MagicMock(client=self.client)

        # Mock return values for 'get_record' calls.
        # Use partial pass in 'self' so it can access attributes loaded during setup.
        self.client.return_value.__aenter__.return_value.get_record.side_effect = partial(self._get_record_stub, self)

    def _get_id_from_record(self, record: List[Dict]) -> str:
        """
        :param record: List of dicts with FeatureName and ValueAsString.
        :return: record identifier value
        """
        # Assume that the record identifier is the first feature in the record.
        return record[0]['ValueAsString']

    def _get_record_stub(self, *args, **kwargs):
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

        if record_identifier_value_as_string not in self.records_by_id:
            # FeatureStore returns a 200 response without a record if the identifier is not found.
            return {}

        full_record = self.records_by_id[record_identifier_value_as_string]
        # Only return requested features to check that a valid model can be constructed from the requested features.
        filtered_record = [feature for feature in full_record if feature['FeatureName'] in feature_names]
        return {'Record': filtered_record}