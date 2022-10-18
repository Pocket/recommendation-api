from typing import Optional

from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.models.link import LinkModel


class CollectionSlateProvider(SlateProvider):

    @property
    def candidate_set_id(self) -> str:
        return '92af3dae-25c9-46c3-bf05-18082aacc7e1'

    @property
    def headline(self) -> str:
        return 'Popular Collections'

    @property
    def subheadline(self) -> str:
        return 'Curated guides to the best reads on the web'

    @property
    def more_link(self) -> Optional[LinkModel]:
        return LinkModel(text='Explore more Collections', url='https://getpocket.com/collections')
