from typing import List, Optional

from aws_xray_sdk.core import xray_recorder

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession
from app.config import ENV, ENV_PROD
from app.models.unleash_assignment import UnleashAssignmentModel
from app.models.request_user import RequestUser


class UnleashConfig:
    APP_NAME = 'recommendation-api'
    ENVIRONMENT = 'prod' if ENV == ENV_PROD else 'alpha'  # Must be prod, beta, or alpha (see UnleashEnvironment)


class UnleashError(Exception):
    pass


class UnleashProvider:
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

    async def get_assignment(self, name: str, user: RequestUser) -> Optional[UnleashAssignmentModel]:
        """
        :param name: name of the assignment
        :param user:
        :return: UnleashAssignmentModel if the user is assigned else None.
        """
        assignments = await self.get_assignments([name], user=user)
        return assignments[0] if assignments else None

    async def get_assignments(self, names: List[str], user: RequestUser) -> List[UnleashAssignmentModel]:
        """
        Returns Unleash assignments with certain assignment names that the user is assigned to.
        :param names:
        :param user:
        :return:
        """

        # Currently FeatureFlags only has a query for all assignments:
        # https://github.com/Pocket/feature-flags/blob/main/schema.graphql#L25
        all_assignments = await self._get_all_assignments(user=user)

        return [assignment for assignment in all_assignments if assignment.name in names and assignment.assigned]

    @xray_recorder.capture_async('data_providers.UnleashProvider._get_all_assignments')
    async def _get_all_assignments(self, user: RequestUser) -> List[UnleashAssignmentModel]:
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

        async with self.pocket_graph_client_session.post(url='/', json=body, raise_for_status=True) as resp:
            response_json = await resp.json()
            assignments_data = response_json['data']['unleashAssignments']['assignments']
            return [UnleashAssignmentModel.parse_obj(assignment) for assignment in assignments_data]
