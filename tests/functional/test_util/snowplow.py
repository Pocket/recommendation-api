import asyncio
from urllib.parse import urljoin

import requests

from app.data_providers.snowplow.config import SnowplowConfig


class SnowplowMicroClient:
    """
    Based on https://github.com/Pocket/curated-corpus-api/blob/main/src/test/helpers/snowplow.ts
    """

    def __init__(self, config: SnowplowConfig):
        self.config = config

    def reset_snowplow_events(self):
        return requests.post(self._format_url('/micro/reset')).json()

    def get_event_counts(self):
        return requests.get(self._format_url('/micro/all')).json()

    def get_good_events(self):
        return requests.get(self._format_url('/micro/good')).json()

    def get_bad_snowplow_events(self):
        return requests.get(self._format_url('/micro/bad')).json()

    def get_last_error(self):
        bad_events = self.get_bad_snowplow_events()
        return bad_events[-1]['errors']

    def _format_url(self, url_path):
        return urljoin(f'{self.config.PROTOCOL}://{self.config.ENDPOINT_URL}', url_path)


async def wait_for_snowplow_events(snowplow_micro, max_wait_time: int = 5, n_expected_event: int = 1):
    # Locally the request to Snowplow gets handled in 0.01s, but in CircleCI we need 1 second.
    for i in range(max_wait_time):
        if snowplow_micro.get_event_counts()['total'] >= n_expected_event:
            return
        else:
            await asyncio.sleep(1)
