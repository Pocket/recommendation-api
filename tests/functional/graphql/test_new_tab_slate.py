import logging
from typing import Dict

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.data_providers.slate_providers.new_tab_slate_provider import MIN_TILE_ID, MAX_TILE_ID
from app.main import app
from tests.functional.test_util.snowplow import wait_for_snowplow_events


def _format_new_tab_query(locale, region, count=50, enable_ranking_by_region=None):
    ranking_by_region_param = ""
    if enable_ranking_by_region is not None:
        ranking_by_region_param = ", enableRankingByRegion: " + str(enable_ranking_by_region).lower()

    return '''
        query {
          newTabSlate(locale: "%(locale)s", region: %(region)s%(ranking_by_region_param)s) {
            recommendations(count: %(count)d) {
              tileId
              corpusItem {
                id
              }
            }
          }
        }
    ''' % {
        'locale': locale,
        'region': f'"{region}"' if region else 'null',
        'ranking_by_region_param': ranking_by_region_param,
        'count': count,
    }


@pytest.fixture
def pocket_graph_request_headers() -> Dict[str, str]:
    return {
        'apiId': '94110',
        'consumerKey': 'fx-client-consumer-key',
        'applicationName': 'Firefox',
        'applicationIsNative': 'true',
        'applicationIsTrusted': 'true',
    }


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "locale,region",
    [
        # Test cases based on the values that firefox-api-proxy can pass through:
        # https://github.com/Pocket/firefox-api-proxy/blob/main/src/generated/openapi/types.ts#L123-L124
        ('en-US', 'US'),
        ('en-GB', 'GB'),
        ('en-IN', 'IN'),
        ('es-ES', 'ES'),
        ('es', 'ES'),  # Firefox uses both 'es' and 'es-ES' format for locale.
        ('es-ES', 'FR'),  # Spanish-language Firefox geographically located in France.
        ('fr-FR', 'FR'),
        ('it-IT', 'IT'),
        ('it-IT', None),  # Region can be null.
    ])
async def test_new_tab_slate(locale, region, snowplow_micro, pocket_graph_request_headers):
    """
    Note that nothing is patched for this test. This means that:
    1. CorpusItems will be fetched from the public production Pocket GraphQL endpoint. This is a stable endpoint that
        is in the critical path for Firefox New Tab, so it is not expected to make this test fail in an unreliable way.
    2. Assuming AWS credentials are unavailable, FeatureGroupClient.batch_get_records will fail and no engagement will
        be available for Thompson sampling. The query should succeed even when access to the feature group is denied.
    """
    async with AsyncClient(app=app, base_url="http://test") as client, LifespanManager(app):
        requested_recommendation_count = 30
        query = _format_new_tab_query(locale=locale, region=region, count=requested_recommendation_count)
        response = await client.post('/', json={'query': query}, headers=pocket_graph_request_headers)
        data = response.json()

        assert not data.get('errors')
        recommendations = data['data']['newTabSlate']['recommendations']

        # Assert that the expected number of slates is being returned.
        assert len(recommendations) == requested_recommendation_count
        # Assert that all tileId are unique integers in range [MIN_TILE_ID, MAX_TILE_ID]
        tile_ids = [r['tileId'] for r in recommendations]
        assert all(MIN_TILE_ID <= tile_id <= MAX_TILE_ID for tile_id in tile_ids)
        assert all(int(tile_id) == tile_id for tile_id in tile_ids)
        assert len(set(tile_ids)) == len(tile_ids)

        await wait_for_snowplow_events(snowplow_micro, n_expected_event=1)
        all_snowplow_events = snowplow_micro.get_event_counts()
        assert all_snowplow_events == {'total': 1, 'good': 1, 'bad': 0}


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "locale,region,enable_ranking_by_region",
    [
        ('en-US', 'US', True),
        ('en-CA', 'CA', True),
        ('en-US', 'US', False),
        ('en-CA', 'CA', False),
    ])
async def test_new_tab_slate_ranked_by_region(
        locale, region, enable_ranking_by_region, snowplow_micro, pocket_graph_request_headers, caplog):
    async with AsyncClient(app=app, base_url="http://test") as client, LifespanManager(app):
        with caplog.at_level(logging.INFO):
            requested_recommendation_count = 30
            query = _format_new_tab_query(
                locale=locale,
                region=region,
                enable_ranking_by_region=enable_ranking_by_region,
                count=requested_recommendation_count)
            response = await client.post('/', json={'query': query}, headers=pocket_graph_request_headers)
            data = response.json()

            assert not data.get('errors')
            recommendations = data['data']['newTabSlate']['recommendations']
            assert len(recommendations) == requested_recommendation_count

            # Assert an info message was logged if and only if enable_ranking_by_region is True
            assert enable_ranking_by_region == any(
                r.levelname == 'INFO' and f'Results will soon be ranked for the {region} region' in r.message
                for r in caplog.records
            ), f'Expected log record not found in {caplog.records}'
