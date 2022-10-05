from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import uuid5, UUID

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.link import LinkModel


class SlateProvider(ABC):

    def __init__(self, corpus_feature_group_client: CorpusFeatureGroupClient):
        self.corpus_feature_group_client = corpus_feature_group_client

    @property
    @abstractmethod
    def candidate_set_id(self) -> str:
        """
        :return: UUID candidate set identifier, which identifies the corpus items that serve as the input for this slate
        """
        return NotImplemented

    @property
    @abstractmethod
    def headline(self) -> str:
        """
        :return: Slate headline
        """
        return NotImplemented

    @property
    def subheadline(self) -> Optional[str]:
        """
        :return: Slate headline
        """
        return None

    @property
    def more_link(self) -> Optional[LinkModel]:
        """
        :return: Slate headline
        """
        return None

    async def get_candidate_corpus_items(self) -> List[CorpusItemModel]:
        """
        :return: The CorpusItems from the candidate set, without any rankers or filters applied.
        """
        return await self.corpus_feature_group_client.fetch(self.candidate_set_id)

    async def get_recommendations(self, recommendation_count: int) -> List[CorpusRecommendationModel]:
        """
        :param recommendation_count: The desired number of recommendations. Fewer or more than this may be returned.
        :return: The list of corpus items that can be recommended is by default the same as the candidate set.
        """
        items = await self.get_candidate_corpus_items()
        return [CorpusRecommendationModel(corpus_item=item) for item in items]

    async def get_slate(self, recommendation_count: int) -> CorpusSlateModel:
        """
        :param recommendation_count: The desired number of recommendations. Fewer or more than this may be returned.
        It's good to return ~2x more recommendations to account for any duplicates that are removed at a later stage.
        Fewer may be returned if insufficient content is available.
        :return: A Corpus Slate that can be recommended
        """
        return CorpusSlateModel(
            configuration_id=self.configuration_id,
            headline=self.headline,
            subheadline=self.subheadline,
            recommendations=await self.get_recommendations(recommendation_count=recommendation_count),
            more_link=self.more_link
        )

    @property
    def provider_name(self) -> str:
        """
        :return: Name for the slate provider, representing the ranking/filtering algorithms that are applied.
        """
        return self.__class__.__name__

    @property
    def configuration_id(self) -> str:
        """
        :return: UUID slate's configuration id, identifying the context and type of content that this slate provides.
        """
        return str(uuid5(UUID(self.candidate_set_id), self.provider_name))
