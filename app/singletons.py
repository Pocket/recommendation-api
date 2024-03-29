from typing import Optional

import aioboto3
from opentelemetry import trace

from app.config import TRANSLATIONS_DIR
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.feature_group.feature_group_client import FeatureGroupClient
from app.recommenders.item2item import Item2ItemRecommender

from app.data_providers.translation import TranslationProvider
from app.data_providers.user_impression_cap_provider import UserImpressionCapProvider

container: Optional['DiContainer'] = None  # place_type: Optional[DiContainer]


class DiContainer:
    def __init__(self):
        self.item2item_recommender = Item2ItemRecommender()
        self.aioboto3_session = aioboto3.Session()
        self.feature_group_client = FeatureGroupClient(aioboto3_session=self.aioboto3_session)
        self.translation_provider = TranslationProvider(translations_dir=TRANSLATIONS_DIR)
        self.corpus_feature_group_client = CorpusFeatureGroupClient(aioboto3_session=self.aioboto3_session)
        self.user_impression_cap_provider = UserImpressionCapProvider(aioboto3_session=self.aioboto3_session)
        self.corpus_engagement_provider = CorpusEngagementProvider(feature_group_client=self.feature_group_client)

        self.tracer = trace.get_tracer(__name__)

    @staticmethod
    def init():
        global container
        container = DiContainer()

    @staticmethod
    def get() -> 'DiContainer':
        return container
