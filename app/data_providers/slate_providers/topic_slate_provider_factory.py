from app.data_providers.slate_providers.topic_slate_provider import TopicSlateProvider
from app.models.topic import TopicModel


class TopicSlateProviderFactory:

    def __init__(self, *args, **kwargs):
        self.slate_provider_args = args
        self.slate_provider_kwargs = kwargs

    def __getitem__(self, topic: TopicModel) -> TopicSlateProvider:
        """
        :param topic:
        :return: A TopicSlateProvider for the given topic
        """
        return TopicSlateProvider(topic=topic, *self.slate_provider_args, **self.slate_provider_kwargs)
