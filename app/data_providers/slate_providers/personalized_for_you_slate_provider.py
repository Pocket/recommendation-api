from typing import List, Dict

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.link import LinkModel
from app.models.recommendation_reason_model import RecommendationReasonModel
from app.models.recommendation_reason_type import RecommendationReasonType
from app.models.topic import TopicModel
from app.rankers.algorithms import rank_by_preferred_topics


class PersonalizedForYouSlateProvider:

    _EN_RECOMMENDED_CANDIDATE_SET_ID = '2066c835-a940-45ec-b1f7-267457d9e0a2'

    def __init__(self, corpus_feature_group_client: CorpusFeatureGroupClient):
        self.corpus_feature_group_client = corpus_feature_group_client

    async def get_slate(self, preferred_topics: List[TopicModel], recommendation_count: int) -> CorpusSlateModel:
        items = await self.corpus_feature_group_client.fetch(self._EN_RECOMMENDED_CANDIDATE_SET_ID)
        items = rank_by_preferred_topics(items, preferred_topics, recommendation_count)

        preferred_topic_by_id: Dict[str, TopicModel] = {t.corpus_topic_id: t for t in preferred_topics}

        return CorpusSlateModel(
            headline='Recommended For You',
            subheadline='Curated for your interests',
            recommendation_reason_type=RecommendationReasonType.PREFERRED_TOPICS,
            recommendations=[
                CorpusRecommendationModel(
                    corpus_item=item,
                    reason=RecommendationReasonModel(
                        name=preferred_topic_by_id[item.topic].name,
                        type=RecommendationReasonType.PREFERRED_TOPICS,
                    ) if item.topic in preferred_topic_by_id else None,  # Only put reason on items with preferred topic
                ) for item in items
            ],
        )
