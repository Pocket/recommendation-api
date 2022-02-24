import pytest

from app.data_providers.metrics_client import MetricsClient
from app.graphql.corpus_item import CorpusItem
from app.models.metrics.firefox_new_tab_metrics_model import FirefoxNewTabMetricsModel
from app.rankers.algorithms import firefox_thompson_sampling_1day, top5


class MockFirefoxNewtabMetricsFactory():
    mock_impressions = {
        '00000000-0000-0000-0000-000000000000': FirefoxNewTabMetricsModel(
            id='00000000-0000-0000-0000-000000000000',
            unloaded_at='2022-02-07T16:15:30Z',
            scheduled_surface_item_id='4a105732-6dcc-4bfa-a92e-8bb0e5616e89',
            slate_experiment_id='13055e0',
            url='https://example.com/00000000-0000-0000-0000-000000000000',
            slate_id='f99178fb-6bd0-4fa1-8109-cda181b697f6',
            trailing_1_day_opens=0,
            trailing_1_day_impressions=100000
        )
    }

    async def get(self, recommendation_ids):
        return self.mock_impressions

@pytest.mark.asyncio
async def test_get_engagement_metrics__firefox_thompson_sampling():
    mock_metrics_factory = MockFirefoxNewtabMetricsFactory()
    metrics = await MetricsClient(firefox_newtab_metrics_factory=mock_metrics_factory).get_engagement_metrics(
        [CorpusItem(id="example-corpus-item-id")],
        firefox_thompson_sampling_1day
    )
    assert metrics.get('metrics') == mock_metrics_factory.mock_impressions

@pytest.mark.asyncio
async def test_get_engagement_metrics__anything_besides_firefox_thompson_sampling():
    mock_metrics_factory = MockFirefoxNewtabMetricsFactory()
    metrics = await MetricsClient(firefox_newtab_metrics_factory=mock_metrics_factory).get_engagement_metrics(
        [CorpusItem(id="example-corpus-item-id")],
        top5
    )
    assert metrics == {}
