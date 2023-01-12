from app.data_providers.slate_providers.slate_provider import SlateProvider


class LifeHacksSlateProvider(SlateProvider):

    @property
    def candidate_set_id(self) -> str:
        return 'da9cb7a1-3a34-4211-b918-73819a5586c8'
