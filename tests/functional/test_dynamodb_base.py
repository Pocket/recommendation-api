from moto import mock_dynamodb2
import os
import unittest
import boto3
import json
from app.config import dynamodb as dynamodb_config, ROOT_DIR
import pytest
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource


DYNAMODB_LOCALSTACK_DIR = os.path.join(ROOT_DIR, '.docker/localstack/dynamodb/')


@pytest.fixture(scope='function')
def dynamodb_mock():
    with mock_dynamodb2():
        yield boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])


def create_table(dynamodb, table_schema) -> DynamoDBServiceResource.Table:
    with open(table_schema) as f:
        table_schema_json = json.load(f)

    table = dynamodb.create_table(**table_schema_json)
    table.meta.client.get_waiter('table_exists').wait(TableName=table.name)
    assert table.table_status == 'ACTIVE'

    return table


def create_explore_topics_metadata_table(dynamodb) -> DynamoDBServiceResource.Table:
    json_path = os.path.join(DYNAMODB_LOCALSTACK_DIR, 'explore_topics_metadata.json')
    return create_table(dynamodb, json_path)


def create_explore_topics_candidates_table(dynamodb) -> DynamoDBServiceResource.Table:
    json_path = os.path.join(DYNAMODB_LOCALSTACK_DIR, 'explore_topics_candidates.json')
    return create_table(dynamodb, json_path)

#
# class TestDynamoDBBase(unittest.IsolatedAsyncioTestCase):
#     dynamodb: DynamoDBServiceResource
#     jsonRoot = ROOT_DIR + '.docker/localstack/dynamodb/'
#     #
#     # def setup_method(self, method):
#     #     self.dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
#
#     def teardown_method(self, method):
#         self.dynamodb = None
#
#     def create_table(self, table_schema) -> DynamoDBServiceResource.Table:
#         with open(table_schema) as f:
#             table_schema_json = json.load(f)
#
#         table = self.dynamodb.create_table(**table_schema_json)
#         table.meta.client.get_waiter('table_exists').wait(TableName=table.name)
#         assert table.table_status == 'ACTIVE'
#
#         return table
#
#     def create_explore_topics_metadata_table(self) -> DynamoDBServiceResource.Table:
#         return self.create_table(self.jsonRoot + 'explore_topics_metadata.json')
#
#     def create_explore_topics_candidates_table(self) -> DynamoDBServiceResource.Table:
#         return self.create_table(self.jsonRoot + 'explore_topics_candidates.json')
