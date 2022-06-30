from dataclasses import dataclass

from aiohttp import ClientSession

from app.config import ENV, ENV_PROD


@dataclass
class PocketGraphConfig:
    PROD_ENDPOINT_URL = 'https://client-api.getpocket.com'
    DEV_ENDPOINT_URL = 'https://client-api.getpocket.dev'
    ENDPOINT_URL = PROD_ENDPOINT_URL if ENV == ENV_PROD else DEV_ENDPOINT_URL

    APOLLO_CLIENT_NAME = 'recommendations-api'
    APOLLO_CLIENT_VERSION = 1


class PocketGraphClientSession(ClientSession):
    """
    This class subclasses ClientSession and initializes it for connecting to Pocket's Apollo Federated GraphQL server.
    """

    def __init__(self, config: PocketGraphConfig) -> None:
        super().__init__(
            base_url=config.ENDPOINT_URL,
            headers={
                'apollographql-client-name': config.APOLLO_CLIENT_NAME,
                'apollographql-client-version': str(config.APOLLO_CLIENT_VERSION),
            }
        )
