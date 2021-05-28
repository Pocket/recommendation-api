from decimal import Decimal

from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.models.metrics.recommendation_metrics_model import RecommendationMetricsModel


class TestClickdataModel(TestDynamoDBBase):

    async def test_get_metrics_by_item(self):
        await self._put_clickdata_fixtures()

        metrics = await RecommendationMetricsModel().get("1234-ABCD", ["666666", "333333"])
        assert len(metrics) == 3
        assert "default" in metrics
        assert "666666" in metrics
        assert "333333" in metrics
        assert "999999" not in metrics

    async def test_get_cached_metrics_by_item(self):
        await self._put_clickdata_fixtures()

        # Get and cache metrics.
        # - 666666, 333333, and "default" all exist in the database
        # - 111111 doesn't exist, but will be created later
        # - foobar doesn't exist, and will not be created
        metrics = await RecommendationMetricsModel().get("1234-ABCD", ["111111", "666666", "333333", "foobar"])
        assert len(metrics) == 3
        assert metrics["default"].clicks == 200
        assert metrics["333333"].clicks == 33
        assert metrics["666666"].clicks == 66
        assert "foobar" not in metrics
        # "111111" does not exist yet, and is therefore not returned
        assert "111111" not in metrics

        # Change clicks from 66 to 67 for "1234-ABCD/666666"
        self.recommendationMetricsTable.update_item(
            Key={"mod_item": "1234-ABCD/666666"},
            UpdateExpression="set clicks=:c, impressions=:i",
            ExpressionAttributeValues={':c': Decimal(67), ':i': Decimal(1000)})

        # Insert a new item, that wasn't there before.
        self.recommendationMetricsTable.put_item(Item={
            "mod_item": "1234-ABCD/111111",
            "clicks": "1",
            "impressions": "5",
            "created_at": "0",
            "expires_at": "0"
        })

        # The click value in the database has changed. Assert that we're getting the same click value from cache.
        metrics = await RecommendationMetricsModel().get("1234-ABCD", ["111111", "666666", "333333"])
        assert len(metrics) == 3
        assert metrics["default"].clicks == 200
        assert metrics["333333"].clicks == 33
        assert metrics["666666"].clicks == 66
        assert "foobar" not in metrics
        # "111111" exists in the database, but not in the cache.
        assert "111111" not in metrics

        await super().clear_caches()

        # The cache has been cleared. Assert that we're getting the new click values from the database.
        metrics = await RecommendationMetricsModel().get("1234-ABCD", ["111111", "666666", "333333"])
        assert len(metrics) == 4
        assert metrics["default"].clicks == 200
        assert metrics["333333"].clicks == 33
        assert metrics["666666"].clicks == 67
        assert "foobar" not in metrics
        assert metrics["111111"].clicks == 1

    async def _put_clickdata_fixtures(self):
        self.recommendationMetricsTable.put_item(Item={
            "mod_item": "1234-ABCD/default",  # TODO: Should this be /1234-ABCD? The doc only mention rollups per item.
            "clicks": "200",
            "impressions": "5000",
            "created_at": "0",
            "expires_at": "0"
        })

        self.recommendationMetricsTable.put_item(Item={
            "mod_item": "999999/1234-ABCD",
            "clicks": "99",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        self.recommendationMetricsTable.put_item(Item={
            "mod_item": "666666/1234-ABCD",
            "clicks": "66",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        self.recommendationMetricsTable.put_item(Item={
            "mod_item": "333333/1234-ABCD",
            "clicks": "33",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })
