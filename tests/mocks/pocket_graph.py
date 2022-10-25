import json
import os

import aiohttp
import pytest_asyncio
from aiohttp.test_utils import TestServer

from app.config import ROOT_DIR


@pytest_asyncio.fixture
async def pocket_graph_server(aiohttp_server) -> TestServer:
    async def mock_graphql_query(request):
        if 'requests' not in request.app:
            request.app['requests'] = []
        request.app['requests'].append(request)
        # Calling read() here ensures the request content is available in the test method.
        await request.read()

        with open(os.path.join(ROOT_DIR, 'tests/assets/json/unleash_assignments.json')) as fp:
            unleash_assignments = json.load(fp)
            return aiohttp.web.json_response(unleash_assignments)

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
