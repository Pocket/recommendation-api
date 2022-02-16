from app.data_providers.curation_api_client import CurationAPIClient
from app.data_providers.slate_provider import SlateProvider


class Dispatch:
    def __init__(
            self,
            api_client: CurationAPIClient = CurationAPIClient,
            slate_provider: SlateProvider = SlateProvider
    ):
        self.api_client = api_client
        self.slate_provider = slate_provider

    def get_ranked_items(self, corpus_id, user_id):
        pass

    
