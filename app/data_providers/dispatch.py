from app.data_providers.curation_api_client import CurationAPIClient
from app.data_providers.slate_provider import SlateProvider


class Dispatch:
    def __init__(
            self,
            api_client: CurationAPIClient,
            slate_provider: SlateProvider
    ):
        self.api_client = api_client
        self.slate_provider = slate_provider

    
