from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.topic import TopicModel


class PocketHitsSlateProvider:

    _CANDIDATE_SET = '92411893-ebdb-4a43-ad29-aa79e56e2136'

    def __init__(self, corpus_feature_group_client: CorpusFeatureGroupClient):
        self.corpus_feature_group_client = corpus_feature_group_client

    async def get_slate(self, topic: TopicModel, recommendation_count: int) -> CorpusSlateModel:
        items = await self.corpus_feature_group_client.fetch(self._CANDIDATE_SET)

        return CorpusSlateModel(
            headline=topic.name,
            recommendations=[CorpusRecommendationModel(corpus_item=item) for item in items],
        )
