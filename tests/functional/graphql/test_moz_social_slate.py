from typing import Dict

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.data_providers.slate_providers.new_tab_slate_provider import MIN_TILE_ID, MAX_TILE_ID
from app.main import app
from tests.functional.test_util.snowplow import wait_for_snowplow_events


def _format_moz_social_slate_query(locale, region, count=50):
    return '''
        query {
          mozSocialSlate(locale: "%(locale)s", region: %(region)s) {
            recommendations(count: %(count)d) {
              tileId
              corpusItem {
                id
              }
            }
          }
        }
    ''' % {'locale': locale, 'region': f'"{region}"' if region else 'null', 'count': count}

#TODO Update below key values with proper mozsocial values when known
@pytest.fixture
def pocket_graph_request_headers() -> Dict[str, str]:
    return {
        'apiId': '1234',
        'consumerKey': 'mozsocial-client-consumer-key',
        'applicationName': 'Mozsocial',
        'applicationIsNative': 'true',
        'applicationIsTrusted': 'true',
    }

#TODO: verify which locales the mozsocial client will be requesting
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "locale,region",
    [
        ('en-US', 'US'),
        ('en-GB', 'GB'),
        ('en-IN', 'IN'),
        ('es-ES', 'ES'),
        ('es', 'ES'),
        ('es-ES', 'FR'),
        ('fr-FR', 'FR'),
        ('it-IT', 'IT'),
        ('it-IT', None),
    ])
async def test_moz_social_slate(locale, region, snowplow_micro, pocket_graph_request_headers):
    #TODO add block comment to explain test
    async with AsyncClient(app=app, base_url="http://test") as client, LifespanManager(app):
        requested_recommendation_count = 30
        query = _format_moz_social_slate_query(locale=locale, region=region, count=requested_recommendation_count)
        response = await client.post('/', json={'query': query}, headers=pocket_graph_request_headers)
        data = response.json()

        assert not data.get('errors')
        recommendations = data['data']['mozSocialSlate']['recommendations']

        # Assert that the expected number of recommendations is the same as requested.
        assert len(recommendations) == requested_recommendation_count

        await wait_for_snowplow_events(snowplow_micro, n_expected_event=1)
        all_snowplow_events = snowplow_micro.get_event_counts()
        assert all_snowplow_events == {'total': 1, 'good': 1, 'bad': 0}
