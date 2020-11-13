from moto import mock_dynamodb2, mock_secretsmanager
import boto3
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
from tests.functional.test_dynamodb_base import TestDynamoDBBase
import aws_lambda
from aws_lambda.config.index import secrets
from pytest_mock import mock
from tests.functional.aws_lambda.lambda_test_data import event, metaflow_data


@mock_dynamodb2
@mock_secretsmanager
@mock.patch('aws_lambda.index.get_metaflow_data', return_value=metaflow_data)
class TestLambda(TestDynamoDBBase):
    table: DynamoDBServiceResource.Table

    @classmethod
    def setup_class(cls):
        aws_lambda.config.index.dynamodb['endpoint_url'] = None
        cls.dynamodb = boto3.resource('dynamodb')
        cls.secrets_manager = boto3.client('secretsmanager')

    @classmethod
    def teardown_class(cls):
        cls.dynamodb = None

    def setup_method(self, method):
        self.table = self.create_explore_topics_candidates_table()
        self.create_test_secret()

    def teardown_method(self, method):
        self.table.delete()
        self.delete_test_secret()

    def test_handler(self, mocker):
        aws_lambda.index.handler(event)
        response = self.table.scan()
        test_1 = {
                     'topic_id-type': '1|curated',
                     'candidates': [{'item_id': 1, 'feed_id': 1}]
                 }.items() <= response['Items'][0].items()
        test_2 = {
                     'topic_id-type': '2|curated',
                     'candidates': [{'item_id': 2, 'feed_id': 2}]
                 }.items() <= response['Items'][1].items()

        assert test_1 and test_2

    def test_get_flow_name(self, mocker):
        assert aws_lambda.index.get_flow_name(event) == 'CuratedCandidatesFlow'

    def test_get_run_id(self, mocker):
        assert aws_lambda.index.get_run_id(
            event) == 'd3f71c11-26d3-bbbc-6a7f-4efafc51f9d2_283eaaf0-5b60-f4fb-8cf7-9e629d1f9de1'

    def test_get_service_url(self, mocker):
        assert aws_lambda.index.get_service_url() == 'http://test'

    def test_get_tag(self, mocker):
        assert aws_lambda.index.get_tag() == 'test'

    def create_test_secret(self):
        self.secrets_manager.create_secret(
            Name=secrets['metaflow'],
            SecretString='{"METAFLOW_SERVICE_INTERNAL_URL": "http://test", "METAFLOW_DEPLOY_TAG": "test"}'
        )

    def delete_test_secret(self):
        self.secrets_manager.delete_secret(SecretId=secrets['metaflow'], ForceDeleteWithoutRecovery=True)
