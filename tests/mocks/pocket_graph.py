import json
import os

import aiohttp.web
import pytest_asyncio
from aiohttp.test_utils import TestServer
from aiohttp.web_request import Request

from app.config import ROOT_DIR
from app.data_providers.PocketGraphClientSession import PocketGraphConfig


@pytest_asyncio.fixture
async def pocket_graph_server(aiohttp_server) -> TestServer:
    async def mock_graphql_query(request: Request):
        if 'requests' not in request.app:
            request.app['request_jsons'] = []

        request_json = await request.json()
        request.app['request_jsons'].append(request_json)

        if 'unleashAssignments' in request_json['query']:
            json_fixture_path = 'tests/assets/json/unleash_assignments.json'
        elif 'scheduledSurface' in request_json['query']:
            json_fixture_path = 'tests/assets/json/scheduled_surface.json'
        else:
            raise NotImplementedError(f"pocket_graph_server does not implement query {request_json['query']}")

        with open(os.path.join(ROOT_DIR, json_fixture_path)) as fp:
            return aiohttp.web.json_response(json.load(fp))

    app = aiohttp.web.Application()
    app.router.add_post('/', mock_graphql_query)
    return await aiohttp_server(app)


@pytest_asyncio.fixture
async def failing_pocket_graph_server(aiohttp_server) -> TestServer:
    async def mock_graphql_query(request):
        return aiohttp.web.Response(body=b'Simulating an internal server error', status=501)

    app = aiohttp.web.Application()
    app.router.add_post('/', mock_graphql_query)
    return await aiohttp_server(app)


def get_pocket_graph_config(pocket_graph_server: TestServer):
    config = PocketGraphConfig()
    config.ENDPOINT_URL = f'http://{pocket_graph_server.host}:{pocket_graph_server.port}'
    return config
