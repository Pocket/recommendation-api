from datetime import datetime

from app.data_providers.slate_providers.slate_provider import SlateProvider


class PocketHitsSlateProvider(SlateProvider):

    @property
    def candidate_set_id(self) -> str:
        return '92411893-ebdb-4a43-ad29-aa79e56e2136'

    @property
    def headline(self) -> str:
        return f'{datetime.now().strftime("%A")}’s Pocket Hits'
