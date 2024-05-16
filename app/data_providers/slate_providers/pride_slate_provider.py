from typing import List

from app.data_providers.slate_providers.slate_provider import HomeSlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.localemodel import LocaleModel
from app.rankers.algorithms import thompson_sampling, rank_by_impression_caps


class PrideSlateProvider(HomeSlateProvider):

    @property
    def candidate_set_id(self) -> str:
        if self.locale == LocaleModel.de_DE:
            return '8c4f7d7e-f0e0-4c99-9ebb-c889b78dfd66'
        else:
            # fall back to en
            return '33cd5817-cbc4-4d01-b9be-7dbcf4e26d2e'

    async def rank_corpus_items(
            self,
            items: List[CorpusItemModel],
            user_impression_capped_list: List[CorpusItemModel] = None,
            *args,
            **kwargs,
    ) -> List[CorpusItemModel]:
        """
        :param items: Candidate corpus items
        :return: Ranks items based on Thompson sampling.
        """
        if kwargs.get('enable_thompson_sampling_with_seed'):
            metrics = await self.corpus_engagement_provider.get(
                self.recommendation_surface_id, self.configuration_id, items)

            items = thompson_sampling(
                recs=items,
                metrics=metrics,
                random_state=kwargs['enable_thompson_sampling_with_seed'],
                trailing_period=7,  # With few new items/day and relatively many impressions, a low period is sufficient
                default_alpha_prior=12,   # beta * P95 item CTR for this slate (0.7%)
                default_beta_prior=1700)  # 5% of average daily item impressions for this slate

        if user_impression_capped_list is not None:
            items = rank_by_impression_caps(items, user_impression_capped_list)

        return items