from decimal import Decimal

from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.models.clickdata.recommendation_clickdata_model import RecommendationClickdataModel


class TestClickdataModel(TestDynamoDBBase):

    async def test_get_clickdata_by_item(self):
        await self._put_clickdata_fixtures()

        clickdata = await RecommendationClickdataModel().get("1234-ABCD", ["666666", "333333"])
        assert len(clickdata) == 3
        assert "default" in clickdata
        assert "666666" in clickdata
        assert "333333" in clickdata
        assert "999999" not in clickdata

    async def test_get_cached_clickdata_by_item(self):
        await self._put_clickdata_fixtures()

        # Get and cache clickdata.
        # - 666666, 333333, and "default" all exist in the database
        # - 111111 doesn't exist, but will be created later
        # - foobar doesn't exist, and will not be created
        clickdata = await RecommendationClickdataModel().get("1234-ABCD", ["111111", "666666", "333333", "foobar"])
        assert len(clickdata) == 3
        assert clickdata["default"].clicks == 200
        assert clickdata["333333"].clicks == 33
        assert clickdata["666666"].clicks == 66
        assert "foobar" not in clickdata
        # "111111" does not exist yet, and is therefore not returned
        assert "111111" not in clickdata

        # Change clicks from 66 to 67 for "1234-ABCD/666666"
        self.clickdataTable.update_item(
            Key={"mod_item": "1234-ABCD/666666"},
            UpdateExpression="set clicks=:c, impressions=:i",
            ExpressionAttributeValues={':c': Decimal(67), ':i': Decimal(1000)})

        # Insert a new item, that wasn't there before.
        self.clickdataTable.put_item(Item={
            "mod_item": "1234-ABCD/111111",
            "clicks": "1",
            "impressions": "5",
            "created_at": "0",
            "expires_at": "0"
        })

        # The clickvalue in the database has changed. Assert that we're getting the same click value from cache.
        clickdata = await RecommendationClickdataModel().get("1234-ABCD", ["111111", "666666", "333333"])
        assert len(clickdata) == 3
        assert clickdata["default"].clicks == 200
        assert clickdata["333333"].clicks == 33
        assert clickdata["666666"].clicks == 66
        assert "foobar" not in clickdata
        # "111111" exists in the database, but not in the cache.
        assert "111111" not in clickdata

        await super().clear_caches()

        # The cache has been cleared. Assert that we're getting the new click values from the database.
        clickdata = await RecommendationClickdataModel().get("1234-ABCD", ["111111", "666666", "333333"])
        assert len(clickdata) == 4
        assert clickdata["default"].clicks == 200
        assert clickdata["333333"].clicks == 33
        assert clickdata["666666"].clicks == 67
        assert "foobar" not in clickdata
        assert clickdata["111111"].clicks == 1

    async def _put_clickdata_fixtures(self):
        self.clickdataTable.put_item(Item={
            "mod_item": "1234-ABCD/default",
            "clicks": "200",
            "impressions": "5000",
            "created_at": "0",
            "expires_at": "0"
        })

        self.clickdataTable.put_item(Item={
            "mod_item": "1234-ABCD/999999",
            "clicks": "99",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        self.clickdataTable.put_item(Item={
            "mod_item": "1234-ABCD/666666",
            "clicks": "66",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        self.clickdataTable.put_item(Item={
            "mod_item": "1234-ABCD/333333",
            "clicks": "33",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })
