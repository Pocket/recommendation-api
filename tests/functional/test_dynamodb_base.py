import unittest
import boto3
import json
from app.config import dynamodb as dynamodb_config, ROOT_DIR
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource


class TestDynamoDBBase(unittest.TestCase):
    dynamodb: DynamoDBServiceResource
    jsonRoot = ROOT_DIR + '.docker/localstack/dynamodb/'

    def setup_method(self, method):
        self.dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])

    def teardown_method(self, method):
        self.dynamodb = None

    def create_table(self, table_schema) -> DynamoDBServiceResource.Table:
        with open(table_schema) as f:
            table_schema_json = json.load(f)

        table = self.dynamodb.create_table(**table_schema_json)
        table.meta.client.get_waiter('table_exists').wait(TableName=table.name)
        assert table.table_status == 'ACTIVE'

        return table

    def create_explore_topics_metadata_table(self) -> DynamoDBServiceResource.Table:
        return self.create_table(self.jsonRoot + 'explore_topics_metadata.json')

    def create_explore_topics_candidates_table(self) -> DynamoDBServiceResource.Table:
        return self.create_table(self.jsonRoot + 'explore_topics_candidates.json')
