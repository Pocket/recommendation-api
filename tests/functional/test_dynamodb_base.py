import os
from typing import Tuple

import unittest
import boto3
import json
from aiocache import caches
from app.cache import initialize_caches, candidate_set_alias, metrics_alias
from app.config import dynamodb as dynamodb_config, ROOT_DIR
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
from aws_xray_sdk import global_sdk_config


class TestDynamoDBBase(unittest.IsolatedAsyncioTestCase):
    TABLE_NAMES: Tuple[str] = (
        'recommendation_api_metadata',
        'recommendation_api_candidates',
        'recommendation_api_candidate_sets',
        'MODELD-Local-RecMetrics',
        'MODELD-Local-SlateMetrics',
    )
    dynamodb: DynamoDBServiceResource
    jsonRoot = os.path.join(ROOT_DIR, '.docker/localstack/dynamodb/')
    metadata_table: DynamoDBServiceResource.Table
    candidate_table: DynamoDBServiceResource.Table
    recommendation_metrics_table: DynamoDBServiceResource.Table
    candidate_set_table: DynamoDBServiceResource.Table

    async def asyncSetUp(self):
        global_sdk_config.set_sdk_enabled(False)
        self.dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config['endpoint_url'])
        self.delete_tables()
        self.create_tables()

        initialize_caches()

    async def asyncTearDown(self):
        self.delete_tables()
        await self.clear_caches()

    async def clear_caches(self):
        # Clear memcached
        for alias in (candidate_set_alias, metrics_alias):
            cache = caches.get(alias)
            await cache.clear()
            # aiocache doesn't support deleting caches.
            # If we don't delete them, an error is raised "attached to a different loop", because
            # IsolatedAsyncioTestCase creates a new event loop for every test case.
            del caches._caches[alias]

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
        self.metadata_table = self.create_recommendation_api_metadata_table()
        self.candidate_table = self.create_recommendation_api_candidates_table()
        self.recommendation_metrics_table = self.create_recommendation_metrics_table()
        self.slate_metrics_table = self.create_slate_metrics_table()
        self.candidate_set_table = self.create_recommendation_api_candidate_sets_table()

    def create_table(self, table_schema, retry_count=2) -> DynamoDBServiceResource.Table:
        with open(table_schema) as f:
            table_schema_json = json.load(f)

        try:
            table = self.dynamodb.create_table(**table_schema_json)
            table.meta.client.get_waiter('table_exists').wait(TableName=table.name)
            assert table.table_status == 'ACTIVE'
        except self.dynamodb.meta.client.exceptions.ResourceInUseException as e:
            # 'ResourceInUseException' is raised if the table already exists.
            # This happens about half the times on CircleCI, but only the first time that tests are executed.
            # SSH'ing into CircleCI and re-running the tests makes them consistently pass successfully.
            # It's unclear how we can get in this state, because asyncSetUp deletes all tables before creating them.
            if retry_count > 0:
                self.delete_table(table_schema_json['TableName'])
                return self.create_table(table_schema, retry_count=retry_count-1)
            else:
                raise e

        return table

    def create_recommendation_api_metadata_table(self) -> DynamoDBServiceResource.Table:
        return self.create_table(self.jsonRoot + 'recommendation_api_metadata.json')

    def create_recommendation_api_candidates_table(self) -> DynamoDBServiceResource.Table:
        return self.create_table(self.jsonRoot + 'recommendation_api_candidates.json')

    def create_recommendation_metrics_table(self) -> DynamoDBServiceResource.Table:
        return self.create_table(self.jsonRoot + 'MODELD-Local-RecMetrics.json')

    def create_slate_metrics_table(self) -> DynamoDBServiceResource.Table:
        return self.create_table(self.jsonRoot + 'MODELD-Local-SlateMetrics.json')

    def create_recommendation_api_candidate_sets_table(self) -> DynamoDBServiceResource.Table:
        return self.create_table(self.jsonRoot + 'recommendation_api_candidate_sets.json')
