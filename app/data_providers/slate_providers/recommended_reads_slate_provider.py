from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel


class RecommendedReadsSlateProvider:

    _CANDIDATE_SET_ID = '5f0dae93-a5a8-439a-a2e2-5d418c04bc98'

    def __init__(self, corpus_feature_group_client: CorpusFeatureGroupClient):
        self.corpus_feature_group_client = corpus_feature_group_client

    async def get_slate(self) -> CorpusSlateModel:
        items = await self.corpus_feature_group_client.fetch(self._CANDIDATE_SET_ID)

        return CorpusSlateModel(
            headline='Recommended Reads',
            subheadline='Curated by Pocket',
            recommendations=[CorpusRecommendationModel(corpus_item=item) for item in items],
        )
