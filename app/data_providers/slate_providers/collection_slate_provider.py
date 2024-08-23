from typing import Optional, List

from app.data_providers.slate_providers.slate_provider import HomeSlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.link import LinkModel
from app.models.localemodel import LocaleModel
from app.rankers.algorithms import thompson_sampling, rank_by_impression_caps


class CollectionSlateProvider(HomeSlateProvider):

    @property
    def candidate_set_id(self) -> str:
        if self.locale == LocaleModel.de_DE:
            return 'ce0e010b-d73d-45e2-a4cd-4abbff74d168'
        else:
            # Default to en-US for the rest of the world
            return '92af3dae-25c9-46c3-bf05-18082aacc7e1'

    @property
    def more_link(self) -> Optional[LinkModel]:
        return LinkModel(
            text=self.home_translations['CollectionsSlateProvider.more_link_text'],
            url='https://getpocket.com/collections')

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
                default_alpha_prior=18,   # beta * P95 item CTR for this slate (1.5%)
                default_beta_prior=1200)  # 20% of average daily item impressions for this slate

        if user_impression_capped_list is not None:
            items = rank_by_impression_caps(items, user_impression_capped_list)

        return items
