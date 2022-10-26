import aiohttp
import pytest_asyncio
from aio_snowplow_tracker import Tracker, Emitter
from aio_snowplow_tracker.typing import Method
from aiohttp.test_utils import TestServer


@pytest_asyncio.fixture
async def snowplow_server(aiohttp_server) -> TestServer:
    async def track(request):
        if 'requests' not in request.app:
            request.app['requests'] = []
        request.app['requests'].append(request)
        # Calling read() here ensures the request content is available in the test method.
        await request.read()

        return aiohttp.web.Response(body=b'Thanks for the data!')

    app = aiohttp.web.Application()
    app.router.add_get('/i', track)
    app.router.add_post('/com.snowplowanalytics.snowplow/tp2', track)
    return await aiohttp_server(app)


@pytest_asyncio.fixture
async def failing_snowplow_server(aiohttp_server) -> TestServer:
    async def failing_response(request):
        return aiohttp.web.Response(body=b'Simulating an internal server error', status=501)

    app = aiohttp.web.Application()
    app.router.add_get('/i', failing_response)
    app.router.add_post('/com.snowplowanalytics.snowplow/tp2', failing_response)
    return await aiohttp_server(app)


def create_snowplow_tracker(snowplow_server, method: Method = 'post'):
    emitter = Emitter(snowplow_server.host, protocol='http', port=snowplow_server.port, method=method, buffer_size=1)
    return Tracker([emitter])


@pytest_asyncio.fixture
async def snowplow_tracker(snowplow_server) -> Tracker:
    return create_snowplow_tracker(snowplow_server)


@pytest_asyncio.fixture
async def snowplow_tracker_with_server_failure(failing_snowplow_server) -> Tracker:
    emitter = Emitter(failing_snowplow_server.host, protocol='http', port=failing_snowplow_server.port)
    return Tracker([emitter])
