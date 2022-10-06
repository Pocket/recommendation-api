import aiohttp
import pytest
from aio_snowplow_tracker import Tracker, Emitter
from aiohttp.test_utils import TestServer


@pytest.fixture
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


@pytest.fixture
async def failing_snowplow_server(aiohttp_server) -> TestServer:
    async def failing_response(request):
        return aiohttp.web.Response(body=b'Simulating an internal server error', status=501)

    app = aiohttp.web.Application()
    app.router.add_get('/i', failing_response)
    app.router.add_post('/com.snowplowanalytics.snowplow/tp2', failing_response)
    return await aiohttp_server(app)


@pytest.fixture
async def snowplow_tracker(snowplow_server) -> Tracker:
    emitter = Emitter((await snowplow_server).host, protocol='http', port=snowplow_server.port)
    return Tracker([emitter])


@pytest.fixture
async def snowplow_tracker_with_server_failure(failing_snowplow_server) -> Tracker:
    emitter = Emitter(failing_snowplow_server.host, protocol='http', port=failing_snowplow_server.port)
    return Tracker([emitter])
