import aioboto3

from app.config import TRANSLATIONS_DIR
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.feature_group.feature_group_client import FeatureGroupClient
from app.data_providers.item2item import Item2ItemRecommender
from app.data_providers.translation import TranslationProvider
from app.data_providers.user_impression_cap_provider import UserImpressionCapProvider

from dependency_injector import containers
from dependency_injector.providers import Factory


class DiContainer:
    def __init__(self):
        self.item2item_recommender = Item2ItemRecommender()
        self.aioboto3_session = aioboto3.Session()
        self.feature_group_client = FeatureGroupClient(aioboto3_session=self.aioboto3_session)
        self.translation_provider = TranslationProvider(translations_dir=TRANSLATIONS_DIR)
        self.corpus_client = CorpusFeatureGroupClient(aioboto3_session=self.aioboto3_session)
        self.user_impression_cap_provider = UserImpressionCapProvider(aioboto3_session=self.aioboto3_session)
        self.corpus_engagement_provider = CorpusEngagementProvider(feature_group_client=self.feature_group_client)

    @staticmethod
    def init():
        global container
        container = DiContainer()

    @staticmethod
    def get() -> 'DiContainer':
        return container


class Container(containers.DeclarativeContainer):
    # Wiring requires the package https://python-dependency-injector.ets-labs.org/wiring.html
    wiring_config = containers.WiringConfiguration(packages=[
        "app.data_providers",
    ])

    item2item_recommender = Factory(Item2ItemRecommender)
    aioboto3_session = Factory(aioboto3.Session)
    feature_group_client = Factory(FeatureGroupClient, aioboto3_session=aioboto3_session)
    translation_provider = Factory(TranslationProvider, translations_dir=TRANSLATIONS_DIR)
    corpus_client = Factory(CorpusFeatureGroupClient, aioboto3_session=aioboto3_session)
    user_impression_cap_provider = Factory(UserImpressionCapProvider, aioboto3_session=aioboto3_session)
    corpus_engagement_provider = Factory(CorpusEngagementProvider, feature_group_client=feature_group_client)
