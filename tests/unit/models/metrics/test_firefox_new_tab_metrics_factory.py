from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory


class TestFirefoxNewTabMetricsFactory:

    def test_dynamodb_row_to_metrics(self):
        record = [
          {
            "FeatureName": "ID",
            "ValueAsString": "0/0737b00e-a21e-4875-a4c7-3e14926d4acf"
          },
          {
            "FeatureName": "UNLOADED_AT",
            "ValueAsString": "2022-01-31T16:15:30Z"
          },
          {
            "FeatureName": "URL",
            "ValueAsString": "https://example.com/0/0737b00e-a21e-4875-a4c7-3e14926d4acf"
          },
          {
            "FeatureName": "SLATE_ID",
            "ValueAsString": "0737b00e-a21e-4875-a4c7-3e14926d4acf"
          },
          {
            "FeatureName": "TRAILING_15_MINUTE_OPENS",
            "ValueAsString": "0"
          },
          {
            "FeatureName": "TRAILING_15_MINUTE_IMPRESSIONS",
            "ValueAsString": "100"
          }
        ]

        metrics = FirefoxNewTabMetricsFactory().parse_from_record(record)
        assert metrics.trailing_15_minute_opens == 0
        assert metrics.trailing_15_minute_impressions == 100
        assert metrics.id == "0/0737b00e-a21e-4875-a4c7-3e14926d4acf"
