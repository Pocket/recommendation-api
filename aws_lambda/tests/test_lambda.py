import json
import os

from pytest_mock import MockerFixture
import pytest
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
import boto3
from moto import mock_dynamodb2

from aws_lambda.tests.fixtures.lambda_test_data import event, metaflow_data
from aws_lambda import index
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


def create_metadata_table(dynamodb) -> DynamoDBServiceResource.Table:
    json_path = os.path.join(DYNAMODB_LOCALSTACK_DIR, 'recommendation_api_metadata.json')
    return create_table(dynamodb, json_path)


def create_candidates_table(dynamodb) -> DynamoDBServiceResource.Table:
    json_path = os.path.join(DYNAMODB_LOCALSTACK_DIR, 'recommendation_api_candidates.json')
    return create_table(dynamodb, json_path)


def mock_get_metaflow_data(mocker: MockerFixture):
    mocker.patch('aws_lambda.index.get_metaflow_data', return_value=metaflow_data)


def test_handler(mocker: MockerFixture, mock_dynamodb_resource):
    mock_get_metaflow_data(mocker)
    table = create_candidates_table(mock_dynamodb_resource)

    index.handler(event)
    response = table.scan()

    assert {
        'topic_id-type': '1|curated',
        'candidates': [{'item_id': 1, 'feed_id': 1}]
    }.items() <= response['Items'][0].items()

    assert {
        'topic_id-type': '2|curated',
        'candidates': [{'item_id': 2, 'feed_id': 2}]
    }.items() <= response['Items'][1].items()


def test_get_flow_name():
    assert index.get_flow_name(event) == 'CuratedCandidatesFlow'


def test_get_run_id():
    assert index.get_run_id(event) == 'd3f71c11-26d3-bbbc-6a7f-4efafc51f9d2_283eaaf0-5b60-f4fb-8cf7-9e629d1f9de1'


def test_get_tag(mocker: MockerFixture):
    mocker.patch.dict(index.metaflow, {'tag': 'test-tag'})
    assert index.get_tag() == 'test-tag'


def test_get_service_url(mocker: MockerFixture):
    mocker.patch.dict(index.metaflow, {'service_url': 'http://test'})
    assert index.get_service_url() == 'http://test'
