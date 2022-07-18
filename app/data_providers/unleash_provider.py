from abc import ABC, abstractmethod
from typing import List, Optional

from aws_xray_sdk.core import xray_recorder

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession
from app.config import ENV, ENV_PROD
from app.models.ab_test_assignment import AbTestAssignmentModel
from app.models.user import User
from app.models.user_session_ids import UserSessionIds


class AbTestProvidable(ABC):
    """
    Abstract class to determine to which A/B tests the user is assigned, and which variant the user should receive.
    """

    async def get_assignment(self, name: str, user_session_ids: UserSessionIds) -> Optional[AbTestAssignmentModel]:
        """
        Get a single A/B test assignment by name
        :param name:
        :param user_session_ids:
        :return: A/B test assignment for the given name, or None if the experiment does not exist.
        """
        assignments = await self.get_assignments(names=[name], user_session_ids=user_session_ids)
        if assignments:
            return assignments[0]
        else:
            return None

    @abstractmethod
    async def get_assignments(self, names: List[str], user_session_ids: UserSessionIds) -> List[AbTestAssignmentModel]:
        """
        Get A/B test assignments with given experiment names for a user.
        :param names: Assignment names
        :param user_session_ids: User and session ids in hashed and integer representation.
        :return: A/B test assignments for the given names. If no experiment exists for any given name, it will be
        missing from the return value.
        """
        return NotImplemented


class UnleashConfig:
    APP_NAME = 'recommendation-api'
    ENVIRONMENT = 'prod' if ENV == ENV_PROD else 'alpha'  # Must be prod, beta, or alpha (see UnleashEnvironment)


class UnleashError(Exception):
    pass


class UnleashProvider(AbTestProvidable):
    """
    Implements getting A/B test assignments from Unleash

    Currently, the only supported Unleash strategies are 'Gradual rollout' and 'UserIDs', because we do not pass
    any additional context to unleash beyond the `hashed_user_id` and `hashed_guid`. Pocket has created several custom
    Unleash strategies that use additional context. For example the 'accountAge' strategy requires
    `context.properties.accountCreatedAt` to be set. When required context for a strategy is not provided, then
    AbTestAssignmentModel.assigned field will be `False`, meaning the user is ineligible for the experiment.
    We should take care to only use assignments for which the required context is passed in.
    @see https://github.com/Pocket/feature-flags/tree/main/src/unleashClient/strategy
    """

    def __init__(self, pocket_graph_client_session: PocketGraphClientSession, unleash_config: UnleashConfig):
        self.pocket_graph_client_session = pocket_graph_client_session
        self.unleash_config = unleash_config

    @xray_recorder.capture_async('data_providers.UnleashProvider.get_assignments')
    async def get_assignments(self, names: List[str], user: User) -> List[AbTestAssignmentModel]:
        """
        Returns Unleash assignments with certain assignment names.
        :param names:
        :param user:
        :return:
        """

        # Currently FeatureFlags only has a query for all assignments:
        # https://github.com/Pocket/feature-flags/blob/main/schema.graphql#L25
        all_assignments = await self._get_all_assignments(user=user)

        return [assignment for assignment in all_assignments if assignment.name in names]

    async def _get_all_assignments(self, user: User) -> List[AbTestAssignmentModel]:
        """
        Get all Unleash assignments for the given user/session.
        :param user:
        :return:
        """
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
                # @see https://studio.apollographql.com/graph/pocket-client-api/schema/reference/inputs/UnleashContext
                'context': {
                    'appName': self.unleash_config.APP_NAME,
                    'environment': self.unleash_config.ENVIRONMENT,
                    'userId': user.hashed_user_id,
                    'sessionId': user.hashed_guid,
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
