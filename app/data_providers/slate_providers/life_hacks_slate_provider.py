from typing import List

from app.data_providers.slate_providers.slate_provider import HomeSlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.localemodel import LocaleModel
from app.rankers.algorithms import thompson_sampling, rank_by_impression_caps


class LifeHacksSlateProvider(HomeSlateProvider):

    @property
    def candidate_set_id(self) -> str:
        if self.locale == LocaleModel.en_US:
            return 'da9cb7a1-3a34-4211-b918-73819a5586c8'
        elif self.locale == LocaleModel.de_DE:
            return '1b086a7e-7f49-416b-8fd6-254d84001f7c'
        elif self.locale == LocaleModel.en_GB:
            return 'b5179696-4516-4d2f-b42b-b0424e3e4d18'
        elif self.locale == LocaleModel.fr_FR:
            return 'c082fb1f-bec9-45e5-b119-e658cc29366c'
        elif self.locale == LocaleModel.it_IT:
            return '22312367-36a5-4ceb-bce6-7fea7e83759b'
        elif self.locale == LocaleModel.es_ES:
            return 'c62e86b4-8d88-4036-80e3-00394323946f'
        else:
            # default to en-US
            return 'da9cb7a1-3a34-4211-b918-73819a5586c8'

    async def rank_corpus_items(
            self,
            items: List[CorpusItemModel],
            user_impression_capped_list: List[CorpusItemModel] = None,
            *args,
            **kwargs,
    ) -> List[CorpusItemModel]:

        if kwargs.get('enable_thompson_sampling_with_seed'):
            """
            :param items: Candidate corpus items
            :return: Ranks items based on Thompson sampling.
            """
            metrics = await self.corpus_engagement_provider.get(
                self.recommendation_surface_id, self.configuration_id, items)

            items = thompson_sampling(
                recs=items,
                metrics=metrics,
                random_state=kwargs['enable_thompson_sampling_with_seed'],
                trailing_period=14,  # With a low impression volume, a longer period should help find the best stories
                default_alpha_prior=18,   # copied from CollectionSlateProvider
                default_beta_prior=1200)  # copied from CollectionSlateProvider

        if user_impression_capped_list is not None:
            items = rank_by_impression_caps(items, user_impression_capped_list)

        return items