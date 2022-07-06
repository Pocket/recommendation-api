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

# export function assertValidSnowplowObjectUpdateEvents(
#   events,
#   triggers: CuratedCorpusItemUpdate['trigger'][],
#   object: CuratedCorpusItemUpdate['object']
# ) {
#   const parsedEvents = events
#     .map(parseSnowplowData)
#     .map((parsedEvent) => parsedEvent.data);
#
#   expect(parsedEvents).to.include.deep.members(
#     triggers.map((trigger) => ({
#       schema: config.snowplow.schemas.objectUpdate,
#       data: { trigger, object },
#     }))
#   );
# }
