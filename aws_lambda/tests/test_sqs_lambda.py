import json
import os

import pytest
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
import boto3
from moto import mock_dynamodb2

from aws_lambda.tests.fixtures.lambda_sqs_test_data import event
from aws_lambda import sqs_handler
from app.config import ROOT_DIR


DYNAMODB_LOCALSTACK_DIR = os.path.join(ROOT_DIR, '.docker/localstack/dynamodb/')


@pytest.fixture(scope='function')
def mock_dynamodb_resource():
    with mock_dynamodb2():
        yield boto3.resource('dynamodb')


def create_table(dynamodb, table_schema_path) -> DynamoDBServiceResource.Table:
    with open(table_schema_path) as f:
        table_schema_json = json.load(f)

    table = dynamodb.create_table(**table_schema_json)
    table.meta.client.get_waiter('table_exists').wait(TableName=table.name)
    assert table.table_status == 'ACTIVE'

    return table


def create_candidate_sets_table(dynamodb) -> DynamoDBServiceResource.Table:
    json_path = os.path.join(DYNAMODB_LOCALSTACK_DIR, 'recommendation_api_candidate_sets.json')
    return create_table(dynamodb, json_path)


def test_handler(mock_dynamodb_resource):
    table = create_candidate_sets_table(mock_dynamodb_resource)

    sqs_handler.handler(event, context=None)

    response = table.scan()

    assert {
        'id': '1234-5678-ABCD-CEDF',
        'version': 1,
        'created_at': 1612470655,
        'expires_at': 1644006655,
        'candidates': [{"item_id": 3242933715,"publisher": "TheAtlantic", "feed_id":1}]
    }.items() <= response['Items'][0].items()
