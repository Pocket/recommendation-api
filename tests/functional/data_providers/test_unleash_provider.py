import pytest
from aiohttp import ClientError

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession, PocketGraphConfig
from app.data_providers.unleash_provider import UnleashProvider, UnleashConfig
from app.models.unleash_assignment import UnleashAssignmentModel
from app.models.request_user import RequestUser

from tests.mocks.pocket_graph import *
from tests.mocks.user import user_1


def _get_pocket_graph_config(pocket_graph_server: TestServer):
    config = PocketGraphConfig()
    config.ENDPOINT_URL = f'http://{pocket_graph_server.host}:{pocket_graph_server.port}'
    return config


@pytest.mark.asyncio
async def test_get_assignments(pocket_graph_server: TestServer, user_1: RequestUser):
    unleash_config = UnleashConfig()

    async with PocketGraphClientSession(_get_pocket_graph_config(pocket_graph_server)) as pocket_graph_client_session:
        unleash_provider = UnleashProvider(pocket_graph_client_session, unleash_config=unleash_config)
        unleash_assignments = await unleash_provider.get_assignments(['test.getstarted'], user_1)

    # Assert the request to the Pocket Graph has the expected query and variables.
    request = pocket_graph_server.app['requests'][-1]
    request_json = await request.json()
    assert 'unleashAssignments' in request_json['query']
    assert request_json['variables']['context'] == {
        'appName': unleash_config.APP_NAME,
        'environment': unleash_config.ENVIRONMENT,
        'userId': user_1.hashed_user_id,
        'sessionId': user_1.hashed_guid,
        'properties': {'locale': user_1.locale}
    }

    # pocket_graph_server returns data from `tests/assets/json/unleash_assignments.json`
    assert unleash_assignments == [UnleashAssignmentModel(assigned=True, name='test.getstarted', variant='v0')]


@pytest.mark.asyncio
async def test_get_assignments_server_error(failing_pocket_graph_server: TestServer, user_1: RequestUser):
    # Assert that an exception is raised when the Pocket GraphQL server responds with a server error.
    with pytest.raises(ClientError) as exception_info:
        async with PocketGraphClientSession(_get_pocket_graph_config(failing_pocket_graph_server)) as client_session:
            unleash_provider = UnleashProvider(client_session, unleash_config=UnleashConfig())
            await unleash_provider.get_assignments(['test.getstarted'], user_1)

    assert '501' in str(exception_info.value)
