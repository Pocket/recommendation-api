from copy import deepcopy
import json
import os

import pytest
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
import boto3
from moto import mock_dynamodb2

from aws_lambda.tests.fixtures.lambda_sqs_event import event, body, body2
from aws_lambda.tests.fixtures.lambda_sqs_event_without_id import event_without_id
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

    assert body.items() <= response['Items'][0].items()
    assert body2.items() <= response['Items'][1].items()


def test_handler_validates_id(mock_dynamodb_resource):
    create_candidate_sets_table(mock_dynamodb_resource)

    with pytest.raises(AssertionError):
        sqs_handler.handler(event_without_id)


def test_get_dynamodb_item_validation():
    # Missing id raises AssertionError
    with pytest.raises(AssertionError):
        test_case = deepcopy(body)
        del test_case['id']
        sqs_handler.get_dynamodb_item(test_case)

    # id = None raises AssertionError
    with pytest.raises(AssertionError):
        test_case = deepcopy(body)
        test_case['id'] = None
        sqs_handler.get_dynamodb_item(test_case)

    # Missing candidates raises AssertionError
    with pytest.raises(AssertionError):
        test_case = deepcopy(body)
        del test_case['candidates']
        sqs_handler.get_dynamodb_item(test_case)

    # If candidates is not a list, it raises AssertionError
    with pytest.raises(AssertionError):
        test_case = deepcopy(body)
        test_case['candidates'] = {'foo': 'bar'}
        sqs_handler.get_dynamodb_item(test_case)

    # If a candidate is missing an item_id, it raises AssertionError
    with pytest.raises(AssertionError):
        test_case = deepcopy(body)
        del test_case['candidates'][0]['item_id']
        sqs_handler.get_dynamodb_item(test_case)

    # If a candidate has a publisher that is not a string, it raises AssertionError
    with pytest.raises(AssertionError):
        test_case = deepcopy(body)
        test_case['candidates'][0]['publisher'] = 1234
        sqs_handler.get_dynamodb_item(test_case)
