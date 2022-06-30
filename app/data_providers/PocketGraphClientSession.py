from dataclasses import dataclass

from aiohttp import ClientSession

from app.config import ENV, ENV_PROD, VERSION


@dataclass
class PocketGraphConfig:
    PROD_ENDPOINT_URL = 'https://client-api.getpocket.com'
    DEV_ENDPOINT_URL = 'https://client-api.getpocket.dev'
    ENDPOINT_URL = PROD_ENDPOINT_URL if ENV == ENV_PROD else DEV_ENDPOINT_URL

    CLIENT_NAME = 'recommendations-api'
    CLIENT_VERSION = VERSION


class PocketGraphClientSession(ClientSession):
    """
    This is an aiohttp.ClientSession initialized for connecting to Pocket's Apollo Federated GraphQL server.

    Example usage:
        ```python
        session = PocketGraphClientSession(config=PocketGraphConfig())
        query = 'query Collections { getCollections { collections { title } } }'
        async with session.post(url='/', json={'query': query}) as resp:
            response_json = await resp.json()
        ```
    """

    def __init__(self, config: PocketGraphConfig) -> None:
        super().__init__(
            base_url=config.ENDPOINT_URL,
            headers={
                'apollographql-client-name': config.CLIENT_NAME,
                'apollographql-client-version': config.CLIENT_VERSION,
            }
        )
