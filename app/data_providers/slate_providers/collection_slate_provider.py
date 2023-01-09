import logging
from typing import Optional, List

from app.data_providers.slate_providers.slate_provider import SlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.link import LinkModel
from app.models.localemodel import LocaleModel
from app.rankers.algorithms import thompson_sampling


class CollectionSlateProvider(SlateProvider):

    @property
    def candidate_set_id(self) -> str:
        return '92af3dae-25c9-46c3-bf05-18082aacc7e1'

    @property
    def more_link(self) -> Optional[LinkModel]:
        base_url = 'https://getpocket.com'

        if self.locale == LocaleModel.en_US:
            url = f'{base_url}/collections'
        elif self.locale == LocaleModel.de_DE:
            # TODO: Ask Web team how we should generalize this. /de-DE/collections currently points to English content.
            url = f'{base_url}/de/collections'
        else:
            logging.warning(f'Unsupported locale for collections {self.locale.value}')
            return None

        return LinkModel(text=self.home_translations['CollectionsSlateProvider.more_link_text'], url=url)

    async def rank_corpus_items(
            self,
            items: List[CorpusItemModel],
            *args,
            **kwargs,
    ) -> List[CorpusItemModel]:
        """
        :param items: Candidate corpus items
        :return: Ranks items based on Thompson sampling if enable_thompson_sampling is True.
        """
        if kwargs.get('enable_thompson_sampling'):
            metrics = await self.corpus_engagement_provider.get(
                self.recommendation_surface_id, self.configuration_id, items)

            items = thompson_sampling(
                recs=items,
                metrics=metrics,
                trailing_period=14,  # With a low impression volume, a longer period should help find the best stories
                default_alpha_prior=18,   # beta * P95 item CTR for this slate (1.5%)
                default_beta_prior=1200)  # 20% of average daily item impressions for this slate

        return items
