from typing import Optional

import aioboto3

from app.config import TRANSLATIONS_DIR
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.feature_group.feature_group_client import FeatureGroupClient
from app.data_providers.item2item import Item2ItemRecommender
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.translation import TranslationProvider
from app.data_providers.user_impression_cap_provider import UserImpressionCapProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider

container: Optional['DiContainer'] = None  # place_type: Optional[DiContainer]


class DiContainer:
    def __init__(self):
        self.item2item_recommender = Item2ItemRecommender()
        self.aioboto3_session = aioboto3.Session()
        self.feature_group_client = FeatureGroupClient(aioboto3_session=self.aioboto3_session)
        self.translation_provider = TranslationProvider(translations_dir=TRANSLATIONS_DIR)
        self.corpus_client = CorpusFeatureGroupClient(aioboto3_session=self.aioboto3_session)
        self.topic_provider = TopicProvider(aioboto3_session=self.aioboto3_session)
        self.user_recommendation_preferences_provider = UserRecommendationPreferencesProvider(
            aioboto3_session=self.aioboto3_session,
            topic_provider=self.topic_provider
        )
        self.user_impression_cap_provider = UserImpressionCapProvider(aioboto3_session=self.aioboto3_session)
        self.corpus_engagement_provider = CorpusEngagementProvider(feature_group_client=self.feature_group_client)

    @staticmethod
    def init():
        global container
        container = DiContainer()

    @staticmethod
    def get() -> 'DiContainer':
        return container
