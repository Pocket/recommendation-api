from typing import Tuple

import unittest
import boto3
import json
from aiocache import caches
from app.cache import initialize_caches, candidate_set_alias, clickdata_alias
from app.config import dynamodb as dynamodb_config, ROOT_DIR
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
from aws_xray_sdk import global_sdk_config


class TestDynamoDBBase(unittest.IsolatedAsyncioTestCase):
    TABLE_NAMES: Tuple[str] = ('recommendation_api_metadata', 'recommendation_api_candidates',
                               'recommendation_api_clickdata', 'recommendation_api_candidate_sets')
    dynamodb: DynamoDBServiceResource
    jsonRoot = ROOT_DIR + '.docker/localstack/dynamodb/'
    metadataTable: DynamoDBServiceResource.Table
    candidateTable: DynamoDBServiceResource.Table
    clickdataTable: DynamoDBServiceResource.Table
    candidateSetTable: DynamoDBServiceResource.Table

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
        for alias in (candidate_set_alias, clickdata_alias):
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
        self.metadataTable = self.create_recommendation_api_metadata_table()
        self.candidateTable = self.create_recommendation_api_candidates_table()
        self.clickdataTable = self.create_recommendation_api_clickdata_table()
        self.candidateSetTable = self.create_recommendation_api_candidate_sets_table()

    def create_table(self, table_schema) -> DynamoDBServiceResource.Table:
        with open(table_schema) as f:
            table_schema_json = json.load(f)

        table = self.dynamodb.create_table(**table_schema_json)
        table.meta.client.get_waiter('table_exists').wait(TableName=table.name)
        assert table.table_status == 'ACTIVE'

        return table

    def create_slate_lineup_config(self):
        self.slate_lineup_config = [
            {
                "id": "dc010ef1-1f34-473a-a4b5-4cc155e18a4a",
                "description": "Explore Technology Topic SlateLineup",
                "experiments": [
                    {
                        "description": "Explore Topic SlateLineup",
                        "rankers": [],
                        "slates": [
                            "e0d7063a-9421-4148-b548-446e9fbc8566",
                            "fa61096a-b681-4251-b299-2fda06c49ebf"
                        ]
                    }
                ]
            }
        ]

    def create_slate_config(self):
        self.slate_config = [
            {
                "id": "fa61096a-b681-4251-b299-2fda06c49ebf",
                "displayName": "Algorithmic Technology Slate",
                "description": "Popular with Pocket readers  Stories from across the web",
                "experiments": [
                    {
                        "description": "algorithmic technology items",
                        "candidateSets": [
                            "46ec119b-2705-4631-8cc2-69092b95b26a"
                        ],
                        "rankers": [
                            "top30",
                            "thompson-sampling",
                            "pubspread"
                        ]
                    }
                ]
            },
            {
                "id": "e0d7063a-9421-4148-b548-446e9fbc8566",
                "displayName": "Curated Technology Slate",
                "description": "Curated by our editors Stories to fuel your mind",
                "experiments": [
                    {
                        "description": "curated technology items",
                        "candidateSets": [
                            "e78cc946-c042-4607-abb1-b25f759df059"
                        ],
                        "rankers": [
                            "top30",
                            "thompson-sampling",
                            "pubspread"
                        ]
                    }
                ]
            },
        ]

    def create_recommendation_api_metadata_table(self) -> DynamoDBServiceResource.Table:
        return self.create_table(self.jsonRoot + 'recommendation_api_metadata.json')

    def create_recommendation_api_candidates_table(self) -> DynamoDBServiceResource.Table:
        return self.create_table(self.jsonRoot + 'recommendation_api_candidates.json')

    def create_recommendation_api_clickdata_table(self) -> DynamoDBServiceResource.Table:
        return self.create_table(self.jsonRoot + 'recommendation_api_clickdata.json')

    def create_recommendation_api_candidate_sets_table(self) -> DynamoDBServiceResource.Table:
        return self.create_table(self.jsonRoot + 'recommendation_api_candidate_sets.json')
