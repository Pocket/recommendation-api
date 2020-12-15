from tests.functional.test_dynamodb_base import dynamodb_mock, create_explore_topics_candidates_table
from aws_lambda.tests.lambda_test_data import event, metaflow_data
from aws_lambda import index


def test_handler(dynamodb_mock):
    table = create_explore_topics_candidates_table(dynamodb_mock)
    index.handler(event)
    response = table.scan()
    test_1 = {
        'topic_id-type': '1|curated',
        'candidates': [{'item_id': 1, 'feed_id': 1}]
    }.items() <= response['Items'][0].items()
    test_2 = {
        'topic_id-type': '2|curated',
        'candidates': [{'item_id': 2, 'feed_id': 2}]
    }.items() <= response['Items'][1].items()

    assert test_1 and test_2

# import boto3
# from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
# from tests.functional.test_dynamodb_base import TestDynamoDBBase
# from aws_lambda.config.index import secrets, metaflow
# from pytest_mock import mock
# from aws_lambda.tests.lambda_test_data import event, metaflow_data
# from moto import mock_dynamodb2, mock_secretsmanager
# import pytest
#
# @mock.patch('aws_lambda.index.get_metaflow_data', return_value=metaflow_data)
# @mock_dynamodb2
# @mock_secretsmanager
# class TestLambda(TestDynamoDBBase):
#     table: DynamoDBServiceResource.Table
#
#     @classmethod
#     def setup_class(cls):
#         import aws_lambda
#         aws_lambda.config.index.dynamodb['endpoint_url'] = None
#         cls.dynamodb = boto3.resource('dynamodb', endpoint_url=None)
#
#     @classmethod
#     def teardown_class(cls):
#         cls.dynamodb = None
#
#     def setup_method(self, method):
#         self.table = self.create_explore_topics_candidates_table()
#         self.metaflow_service_url = metaflow.get('service_url')
#         self.metaflow_tag = metaflow.get('tag')
#
#     def teardown_method(self, method):
#         self.table.delete()
#         metaflow['service_url'] = self.metaflow_service_url
#         metaflow['tag'] = self.metaflow_tag
#
#     def test_handler(self, mocker):
#         import aws_lambda
#         aws_lambda.index.handler(event)
#         response = self.table.scan()
#         test_1 = {
#                      'topic_id-type': '1|curated',
#                      'candidates': [{'item_id': 1, 'feed_id': 1}]
#                  }.items() <= response['Items'][0].items()
#         test_2 = {
#                      'topic_id-type': '2|curated',
#                      'candidates': [{'item_id': 2, 'feed_id': 2}]
#                  }.items() <= response['Items'][1].items()
#
#         assert test_1 and test_2
#
#     def test_get_flow_name(self, mocker):
#         import aws_lambda
#         assert aws_lambda.index.get_flow_name(event) == 'CuratedCandidatesFlow'
#
#     def test_get_run_id(self, mocker):
#         import aws_lambda
#         assert aws_lambda.index.get_run_id(
#             event) == 'd3f71c11-26d3-bbbc-6a7f-4efafc51f9d2_283eaaf0-5b60-f4fb-8cf7-9e629d1f9de1'
#
#     def test_get_service_url(self, mocker):
#         metaflow['service_url'] = 'http://test'
#         import aws_lambda
#         assert aws_lambda.index.get_service_url() == 'http://test'
#
#     def test_get_tag(self, mocker):
#         metaflow['tag'] = 'test'
#         import aws_lambda
#         assert aws_lambda.index.get_tag() == 'test'
