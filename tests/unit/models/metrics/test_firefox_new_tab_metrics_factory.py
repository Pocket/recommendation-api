from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory


class TestFirefoxNewTabMetricsFactory:

    def test_dynamodb_row_to_metrics(self):
        record = [
            {
                "FeatureName": "ID",
                "ValueAsString": "00000000-0000-0000-0000-000000000000"
            },
            {
                "FeatureName": "UNLOADED_AT",
                "ValueAsString": "2022-02-07T16:15:30Z"
            },
            {
                "FeatureName": "SCHEDULED_SURFACE_ITEM_ID",
                "ValueAsString": "4a105732-6dcc-4bfa-a92e-8bb0e5616e89"
            },
            {
                "FeatureName": "SLATE_EXPERIMENT_ID",
                "ValueAsString": "13055e0"
            },
            {
                "FeatureName": "URL",
                "ValueAsString": "https://example.com/00000000-0000-0000-0000-000000000000"
            },
            {
                "FeatureName": "SLATE_ID",
                "ValueAsString": "f99178fb-6bd0-4fa1-8109-cda181b697f6"
            },
            {
                "FeatureName": "TRAILING_1_DAY_OPENS",
                "ValueAsString": "0"
            },
            {
                "FeatureName": "TRAILING_1_DAY_IMPRESSIONS",
                "ValueAsString": "100000"
            }
        ]

        metrics = FirefoxNewTabMetricsFactory().parse_from_record(record)
        assert metrics.trailing_1_day_opens == 0
        assert metrics.trailing_1_day_impressions == 100000
        assert metrics.id == "00000000-0000-0000-0000-000000000000"
