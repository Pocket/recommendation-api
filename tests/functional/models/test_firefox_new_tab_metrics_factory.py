import pytest
from unittest.mock import MagicMock

pytest.importorskip("aioboto3")

from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory

@pytest.mark.asyncio
class TestFirefoxNewTabMetricsFactory:

    async def test_get(self):
        new_tab_engagement = await FirefoxNewTabMetricsFactory().get(
            slate_id='0737b00e-a21e-4875-a4c7-3e14926d4acf',
            content_ids=[str(i) for i in range(50)]
        )

        print(new_tab_engagement)

    async def test_get_2(self, monkeypatch):
        # Mock boto3. Localstack currently does not support Feature Group, so we need to mock it ourselves.
        client = MagicMock()
        aioboto3 = MagicMock(client=client)
        monkeypatch.setattr("app.models.metrics.firefox_new_tab_metrics_factory.aioboto3", aioboto3)

        new_tab_engagement = await FirefoxNewTabMetricsFactory().get(
            slate_id='0737b00e-a21e-4875-a4c7-3e14926d4acf',
            content_ids=[str(i) for i in range(50)]
        )

        called_method = client.mock_calls[1]
        assert called_method[0] == "().start_execution"
        client().start_execution.assert_called_once_with(
            stateMachineArn="arn", name="name", input="{}"
        )
