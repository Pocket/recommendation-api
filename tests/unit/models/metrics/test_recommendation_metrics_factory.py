from decimal import Decimal

from app.models.metrics.recommendation_metrics_factory import RecommendationMetricsFactory


class TestRecommendationMetrics:

    def test_dynamodb_row_to_metrics(self):
        row = {
            "trailing_28_day_opens": Decimal(0.045687984008122705),
            "created_at": Decimal(1610404066),
            "expires_at": Decimal(1644359266),
            "trailing_28_day_impressions": Decimal(2.207612237118199),
            "trailing_14_day_opens": Decimal(0.087984008122705),
            "trailing_14_day_impressions": Decimal(2.045687984008122705),
            "trailing_7_day_opens": Decimal(0.084008122705),
            "trailing_7_day_impressions": Decimal(3.045687984008122705),
            "trailing_1_day_opens": Decimal(0.088884008122705),
            "trailing_1_day_impressions": Decimal(5.045687984008122705),
            "recommendations_pk": "item-id-123/slate-id-123",
        }

        metrics = RecommendationMetricsFactory().parse_from_record(row)
        assert metrics.trailing_28_day_opens == 0.045687984008122705
        assert metrics.trailing_28_day_impressions == 2.207612237118199
        assert metrics.id == "item-id-123/slate-id-123"
