from typing import Tuple

import unittest
import boto3
import json
from app.config import dynamodb as dynamodb_config, ROOT_DIR
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource


class TestDynamoDBBase(unittest.IsolatedAsyncioTestCase):
    TABLE_NAMES: Tuple[str] = ('explore_topics_metadata', 'explore_topics_candidates')
    dynamodb: DynamoDBServiceResource
    jsonRoot = ROOT_DIR + '.docker/localstack/dynamodb/'
    metadataTable: DynamoDBServiceResource.Table
    candidateTable: DynamoDBServiceResource.Table

    def setup_method(self, method):
        self.dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
        self.delete_tables()
        self.create_tables()

    def teardown_method(self, method):
        self.delete_tables()

    def delete_tables(self):
        for table_name in TestDynamoDBBase.TABLE_NAMES:
            self.delete_table(table_name)

    def delete_table(self, table_name):
        try:
            table = self.dynamodb.Table(table_name)
            table.delete()
            table.meta.client.get_waiter('table_not_exists').wait(TableName=table.name)
        except self.dynamodb.meta.client.exceptions.ResourceNotFoundException:
            pass

    def create_tables(self):
        self.metadataTable = self.create_explore_topics_metadata_table()
        self.candidateTable = self.create_explore_topics_candidates_table()

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
