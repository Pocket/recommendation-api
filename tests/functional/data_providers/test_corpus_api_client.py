from datetime import datetime

import pytest
from aiohttp.test_utils import TestServer
from freezegun import freeze_time

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession
from app.data_providers.corpus.corpus_api_client import CorpusApiClient
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from tests.mocks.pocket_graph import pocket_graph_server, get_pocket_graph_config


@pytest.mark.asyncio
async def test_fetch(pocket_graph_server: TestServer):
    async with PocketGraphClientSession(get_pocket_graph_config(pocket_graph_server)) as pocket_graph_client_session:
        corpus_api_client = CorpusApiClient(pocket_graph_client_session)
        corpus_items = await corpus_api_client.fetch('NEW_TAB_EN_US')

    assert len(corpus_items) == 48  # matches number of items in tests/assets/json/scheduled_surface.json

    # Assert all corpus_items have expected fields populated.
    assert all(item.url for item in corpus_items)
    assert all(item.topic for item in corpus_items)
    assert all(item.publisher for item in corpus_items)

    # Assert we can get a scheduled_date for all items.
    assert all(corpus_api_client.get_scheduled_date(item.id) for item in corpus_items)


@pytest.mark.asyncio
@freeze_time("2023-08-01 1:00:00", tz_offset=0)  # 1am Aug 1st, 2023 UTC was 9pm July 31st, 2023 EST
@pytest.mark.parametrize(
    ('surface_id', 'today', 'yesterday'),
    [
        (RecommendationSurfaceId.NEW_TAB_EN_US, '2023-07-31', '2023-07-30'),
        (RecommendationSurfaceId.NEW_TAB_EN_GB, '2023-08-01', '2023-07-31'),
        (RecommendationSurfaceId.NEW_TAB_EN_INTL, '2023-08-01', '2023-07-31'),
        (RecommendationSurfaceId.NEW_TAB_DE_DE, '2023-08-01', '2023-07-31'),
        (RecommendationSurfaceId.NEW_TAB_ES_ES, '2023-08-01', '2023-07-31'),
        (RecommendationSurfaceId.NEW_TAB_FR_FR, '2023-08-01', '2023-07-31'),
        (RecommendationSurfaceId.NEW_TAB_IT_IT, '2023-08-01', '2023-07-31'),
    ]
)
async def test_fetch_variables(
        pocket_graph_server: TestServer, surface_id: RecommendationSurfaceId, today: str, yesterday: str):
    async with PocketGraphClientSession(get_pocket_graph_config(pocket_graph_server)) as pocket_graph_client_session:
        corpus_api_client = CorpusApiClient(pocket_graph_client_session)
        await corpus_api_client.fetch(surface_id.value)

    request_json = pocket_graph_server.app['request_jsons'][-1]
    graphql_variables = request_json['variables']

    assert graphql_variables['date_today'] == today
    assert graphql_variables['date_yesterday'] == yesterday


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ('recommendation_surface_id', ),
    [
        (r, ) for r in RecommendationSurfaceId if 'NEW_TAB' in r.value
    ]
)
async def test_get_surface_timezone(recommendation_surface_id: RecommendationSurfaceId, caplog):
    tz = CorpusApiClient.get_surface_timezone(recommendation_surface_id.value)
    datetime.now(tz)

    # No warnings or errors were logged.
    assert not any(r for r in caplog.records if r.levelname in ('WARNING', 'ERROR', 'CRITICAL'))


@pytest.mark.asyncio
async def test_get_surface_timezone_bad_input(caplog):
    tz = CorpusApiClient.get_surface_timezone('foobar')
    # A timezone is returned, even if scheduled surface id is invalid.
    datetime.now(tz)

    # Error was logged
    error_logs = [r for r in caplog.records if r.levelname == 'ERROR']
    assert len(error_logs) == 1
    assert "Failed to get timezone for foobar, so defaulting to UTC" in error_logs[0].message
