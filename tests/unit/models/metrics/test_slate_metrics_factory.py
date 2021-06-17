from decimal import Decimal

from app.models.metrics.slate_metrics_factory import SlateMetricsFactory


class TestSlateMetrics:

    def test_dynamodb_row_to_metrics(self):
        row = {
            "created_at": Decimal(1610404066),
            "expires_at": Decimal(1644359266),
            "trailing_28_day_opens": Decimal(0.045687984008122705),
            "trailing_28_day_impressions": Decimal(2.207612237118199),
            "trailing_14_day_opens": Decimal(0.045684008122705),
            "trailing_14_day_impressions": Decimal(3.207612237118199),
            "trailing_7_day_opens": Decimal(0.077745684008122705),
            "trailing_7_day_impressions": Decimal(4.207612237118199),
            "trailing_1_day_opens": Decimal(0.086664008122705),
            "trailing_1_day_impressions": Decimal(5.207612237118199),
            "slates_pk": "slate-id-123/lineup-id-123",
        }

        metrics = SlateMetricsFactory().parse_from_record(row)
        assert metrics.trailing_28_day_opens == 0.045687984008122705
        assert metrics.trailing_28_day_impressions == 2.207612237118199
        assert metrics.id == "slate-id-123/lineup-id-123"
