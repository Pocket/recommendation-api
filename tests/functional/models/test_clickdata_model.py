from decimal import Decimal

from tests.functional.test_dynamodb_base import TestDynamoDBBase


class TestClickdataModel(TestDynamoDBBase):

    async def _put_clickdata_fixtures(self):
        self.clickdataTable.put_item(Item={
            "mod_item": "home/default",
            "clicks": "200",
            "impressions": "5000",
            "created_at": "0",
            "expires_at": "0"
        })

        self.clickdataTable.put_item(Item={
            "mod_item": "home/999999",
            "clicks": "99",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        self.clickdataTable.put_item(Item={
            "mod_item": "home/666666",
            "clicks": "66",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        self.clickdataTable.put_item(Item={
            "mod_item": "home/333333",
            "clicks": "33",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })
