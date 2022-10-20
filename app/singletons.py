import aioboto3

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_impression_cap_provider import UserImpressionCapProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider

aioboto3_session = aioboto3.Session()
corpus_client = CorpusFeatureGroupClient(aioboto3_session=aioboto3_session)
topic_provider = TopicProvider(aioboto3_session=aioboto3_session)
user_recommendation_preferences_provider = UserRecommendationPreferencesProvider(
    aioboto3_session=aioboto3_session,
    topic_provider=topic_provider
)
user_impression_cap_provider = UserImpressionCapProvider(aioboto3_session=aioboto3_session)
