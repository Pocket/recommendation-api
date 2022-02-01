import unittest

from app.models.metrics.firefox_new_tab_metrics_factory import FirefoxNewTabMetricsFactory


class TestFirefoxNewTabMetricsFactory(unittest.IsolatedAsyncioTestCase):

    async def test_get(self):
        new_tab_engagement = await FirefoxNewTabMetricsFactory().get(
            slate_id='0737b00e-a21e-4875-a4c7-3e14926d4acf',
            content_ids=[str(i) for i in range(50)]
        )

        print(new_tab_engagement)
