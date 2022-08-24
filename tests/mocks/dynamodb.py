import json
import os

import boto3
import pytest
from mypy_boto3_dynamodb import DynamoDBServiceResource

from app.config import ROOT_DIR, dynamodb as dynamodb_config


class DynamoDBFixture:

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])

    def recreate_table(self, table_name: str) -> DynamoDBServiceResource.Table:
        self._delete_table(table_name)
        return self._create_table(table_name)

    def _delete_table(self, table_name: str):
        try:
            table = self.dynamodb.Table(table_name)
            table.delete()
            table.meta.client.get_waiter('table_not_exists').wait(TableName=table.name)
        except self.dynamodb.meta.client.exceptions.ResourceNotFoundException:
            pass

    def _get_schema_path(self, table_name: str) -> str:
        return os.path.join(ROOT_DIR, '.docker/localstack/dynamodb/', f'{table_name}.json')

    def _create_table(self, table_name: str) -> DynamoDBServiceResource.Table:
        with open(self._get_schema_path(table_name)) as f:
            table_schema_json = json.load(f)

        table = self.dynamodb.create_table(**table_schema_json)
        table.meta.client.get_waiter('table_exists').wait(TableName=table.name)
        assert table.table_status == 'ACTIVE'

        return table


@pytest.fixture
def candidate_sets_dynamodb_table() -> DynamoDBServiceResource.Table:
    return DynamoDBFixture().recreate_table('recommendation_api_candidate_sets')
