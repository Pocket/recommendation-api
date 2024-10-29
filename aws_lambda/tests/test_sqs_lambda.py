from copy import deepcopy
import json
import math
import os
import time

import pytest
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
import boto3
from moto import mock_aws

from aws_lambda.tests.fixtures.lambda_sqs_event import event, body, body2
from aws_lambda.tests.fixtures.lambda_sqs_event_without_id import event_without_id
from aws_lambda import sqs_handler
from app.config import ROOT_DIR


DYNAMODB_LOCALSTACK_DIR = os.path.join(ROOT_DIR, '.docker/localstack/dynamodb/')


@pytest.fixture(scope='function')
def mock_dynamodb_resource():
    with mock_aws():
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

    # Assert created_at is set to now. (+/- 10 second tolerance to ensure test runs reliably.)
    # pytest.assert doesn't work with Decimals, which is what DynamoDB returns.
    assert math.isclose(response['Items'][0]['created_at'], time.time(), abs_tol=10)
    assert math.isclose(response['Items'][1]['created_at'], time.time(), abs_tol=10)


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

    # version not being integer raises AssertionError
    with pytest.raises(AssertionError):
        test_case = deepcopy(body)
        test_case['version'] = '1'
        sqs_handler.get_dynamodb_item(test_case)

    # If expires_at is not set, it raises AssertionError
    with pytest.raises(AssertionError):
        test_case = deepcopy(body)
        del test_case['expires_at']
        sqs_handler.get_dynamodb_item(test_case)

    # If expires_at is not an int, it raises AssertionError
    with pytest.raises(AssertionError):
        test_case = deepcopy(body)
        test_case['expires_at'] = str(int(time.time() + 120))  # Unix time as a string
        sqs_handler.get_dynamodb_item(test_case)

    # If expires_at is in the past, it raises AssertionError
    with pytest.raises(AssertionError):
        test_case = deepcopy(body)
        test_case['expires_at'] = time.time() - 1.0  # 1 second in the past
        sqs_handler.get_dynamodb_item(test_case)

    # If expires_at is too low, it raises AssertionError
    with pytest.raises(AssertionError):
        test_case = deepcopy(body)
        test_case['expires_at'] = time.time() + sqs_handler.MINIMUM_EXPIRES_AT_FROM_NOW - 1.0  # 1 second before minimum
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
