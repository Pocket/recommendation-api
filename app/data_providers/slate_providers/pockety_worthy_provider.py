from app.data_providers.slate_providers.slate_provider import HomeSlateProvider


class PocketWorthyProvider(HomeSlateProvider):

    @property
    def candidate_set_id(self) -> str:
        return '0e0a8663-a2c1-430e-9b8c-3a5b6d9eda11'
