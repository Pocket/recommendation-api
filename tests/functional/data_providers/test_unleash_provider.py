from app.data_providers.PocketGraphClientSession import PocketGraphClientSession, PocketGraphConfig
from app.data_providers.unleash_provider import UnleashProvider, UnleashConfig
from app.models.unleash_assignment import UnleashAssignmentModel
from app.models.user import User

from tests.mocks.pocket_graph import *
from tests.mocks.user import user_1


async def test_get_assignments(pocket_graph_server: TestServer, user_1: User):
    pocket_graph_config = PocketGraphConfig()
    pocket_graph_config.ENDPOINT_URL = f'http://{pocket_graph_server.host}:{pocket_graph_server.port}'

    unleash_config = UnleashConfig()

    async with PocketGraphClientSession(config=pocket_graph_config) as pocket_graph_client_session:
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
        'sessionId': user_1.hashed_guid
    }

    # pocket_graph_server returns data from `tests/assets/json/unleash_assignments.json`
    assert unleash_assignments == [UnleashAssignmentModel(assigned=True, name='test.getstarted', variant='v0')]

