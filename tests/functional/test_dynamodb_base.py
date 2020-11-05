import boto3
import json
from app.config import dynamodb as dynamodb_config


class TestDynamoDBBase:
    def setup_method(self, method):
        self.dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])

    def teardown_method(self, method):
        self.dynamodb = None

    def create_table(self, table_schema):
        with open(table_schema) as f:
            table_schema_json = json.load(f)

        table = self.dynamodb.create_table(**table_schema_json)
        table.meta.client.get_waiter('table_exists').wait(TableName=table.name)
        assert table.table_status == 'ACTIVE'

        return table

    def create_explore_topics_metadata_table(self):
        return self.create_table('.docker/localstack/dynamodb/explore_topics_metadata.json')

    def create_explore_topics_candidates_table(self):
        return self.create_table('.docker/localstack/dynamodb/explore_topics_candidates.json')
