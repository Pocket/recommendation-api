from app.data_providers.slate_providers.slate_provider import SlateProvider


class RecommendedReadsSlateProvider(SlateProvider):

    @property
    def candidate_set_id(self) -> str:
        return '5f0dae93-a5a8-439a-a2e2-5d418c04bc98'

    @property
    def headline(self) -> str:
        return 'Recommended Reads'

    @property
    def subheadline(self) -> str:
        return 'Curated by Pocket'
