from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.slate_providers.topic_slate_provider import TopicSlateProvider
from app.models.topic import TopicModel


class TopicSlateProviderFactory:

    def __init__(self, corpus_feature_group_client: CorpusFeatureGroupClient):
        self.corpus_feature_group_client = corpus_feature_group_client

    def __getitem__(self, topic: TopicModel) -> TopicSlateProvider:
        """
        :param topic:
        :return: A TopicSlateProvider for the given topic
        """
        return TopicSlateProvider(corpus_feature_group_client=self.corpus_feature_group_client, topic=topic)
