from decimal import Decimal

from app.models.metrics.slate_metrics_model import SlateMetricsModel


class TestSlateMetrics:

    def test_dynamodb_row_to_metrics(self):
        row = {
            "clicks": Decimal(0.045687984008122705),
            "created_at": Decimal(1610404066),
            "expires_at": Decimal(1644359266),
            "impressions": Decimal(2.207612237118199),
            "mod_item": "topic/default",
        }

        metrics = SlateMetricsModel.parse_obj(row)
        assert metrics.clicks == 0.045687984008122705
        assert metrics.impressions == 2.207612237118199
        assert metrics.mod_item == "topic/default"
