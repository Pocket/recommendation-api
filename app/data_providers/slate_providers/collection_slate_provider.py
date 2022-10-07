from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.link import LinkModel


class CollectionSlateProvider:

    _CANDIDATE_SET = '92af3dae-25c9-46c3-bf05-18082aacc7e1'

    def __init__(self, corpus_feature_group_client: CorpusFeatureGroupClient):
        self.corpus_feature_group_client = corpus_feature_group_client

    async def get_slate(self) -> CorpusSlateModel:
        items = await self.corpus_feature_group_client.fetch(self._CANDIDATE_SET)

        return CorpusSlateModel(
            headline='Popular Collections',
            subheadline='Curated guides to the best reads on the web',
            recommendations=[CorpusRecommendationModel(corpus_item=item) for item in items],
            more_link=LinkModel(text='Explore More Collections', url='https://getpocket.com/collections')
        )
