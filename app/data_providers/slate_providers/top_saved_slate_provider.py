import random
from typing import List, Optional

from app.config import POCKET_HOME_V3_FEATURE_FLAG
from app.data_providers.slate_providers.candidate_sets import get_topic_candidate_set_id
from app.data_providers.slate_providers.slate_provider import HomeSlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.link import LinkModel
from app.models.localemodel import LocaleModel
from app.models.topic import TopicModel
from app.rankers.algorithms import thompson_sampling, rank_by_impression_caps


class TopSavedSlateProvider(HomeSlateProvider):

    @property
    def candidate_set_id(self) -> str:
        return "ce4553e1-608d-4bd1-b652-5beeecb72195"

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
