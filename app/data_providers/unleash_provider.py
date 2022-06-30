from abc import ABC
from typing import Optional, List

from aws_xray_sdk.core import xray_recorder

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession
from app.config import ENV, ENV_PROD
from app.models.unleash_assignment import AbTestAssignmentModel


class AbTestProvidable(ABC):
    """
    Abstract class to get A/B test assignments.
    """
    async def get_assignments(self, user_id: str) -> List[AbTestAssignmentModel]:
        return NotImplemented


class UnleashConfig:
    APP_NAME = 'recommendation-api'
    ENVIRONMENT = 'prod' if ENV == ENV_PROD else 'alpha'  # Must be prod, beta, or alpha (see UnleashEnvironment)


class UnleashError(Exception):
    pass


class UnleashProvider(AbTestProvidable):
    """
    Implements getting A/B test assignments from Unleash
    """

    def __init__(self, pocket_graph_client_session: PocketGraphClientSession, unleash_config: UnleashConfig):
        self.pocket_graph_client_session = pocket_graph_client_session
        self.unleash_config = unleash_config

    @xray_recorder.capture_async('data_providers.UnleashProvider.get_assignments')
    async def get_assignments(self, user_id: str) -> List[AbTestAssignmentModel]:
        query = """
            query UnleashAssignments($context: UnleashContext!) {
              unleashAssignments(context: $context) {
                assignments {
                  assigned
                  name
                  payload
                  variant
                }
              }
            }
            """

        body = {
            'query': query,
            'variables': {
                'context': {
                    'appName': self.unleash_config.APP_NAME,
                    'environment': self.unleash_config.ENVIRONMENT,
                    'userId': user_id,
                    'sessionId': self._get_session_id(user_id),
                }
            }
        }

        async with self.pocket_graph_client_session.post(url='/', json=body) as resp:
            response_json = await resp.json()

            if resp.status == 200:
                assignments_data = response_json['data']['unleashAssignments']['assignments']
                return [AbTestAssignmentModel.parse_obj(assignment) for assignment in assignments_data]
            else:
                raise UnleashError(f"unleashAssignments responded with {resp.status}: {response_json.get('errors')}")

    def _get_session_id(self, user_id: str):
        """
        The session_id is a device specific identifier that will be consistent across sessions,
        typically the encoded {guid} or some session token. RecommendationAPI
        :param user_id:
        :return:
        """

        # TODO: This should be changed to guid.
        return user_id
