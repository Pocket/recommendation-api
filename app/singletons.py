from typing import Optional

import aioboto3
from opentelemetry import trace

from app import config
from app.config import TRANSLATIONS_DIR
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.feature_group.feature_group_client import FeatureGroupClient
from app.recommenders.item2item import Item2ItemRecommender

from app.data_providers.model_loading import S3Loader, LocalLoader
from app.data_providers.translation import TranslationProvider
from app.data_providers.user_impression_cap_provider import UserImpressionCapProvider
from app.recommenders.hybrid_cf import HybridCFRecommender

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
        self.model_loader = S3Loader(bucket=config.lightfm['model_bucket']) \
            if config.lightfm['model_loader'] == 's3' else LocalLoader()
        self.hybrid_cf_recommender = HybridCFRecommender(model_loader=self.model_loader)

        self.tracer = trace.get_tracer(__name__)

    @staticmethod
    def init():
        global container
        container = DiContainer()

    @staticmethod
    def get() -> 'DiContainer':
        return container
