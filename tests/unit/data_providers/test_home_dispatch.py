import uuid
from typing import List
from unittest.mock import MagicMock

import pytest

from app.config import POCKET_HOME_V3_FEATURE_FLAG
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.dispatch import HomeDispatch
from app.data_providers.slate_providers.author_faves_slate_provider import AuthorFavesSlateProvider
from app.data_providers.slate_providers.collection_slate_provider import CollectionSlateProvider
from app.data_providers.slate_providers.for_you_slate_provider import ForYouSlateProvider
from app.data_providers.slate_providers.life_hacks_slate_provider import LifeHacksSlateProvider
from app.data_providers.slate_providers.pocket_hits_slate_provider import PocketHitsSlateProvider
from app.data_providers.slate_providers.pockety_worthy_provider import PocketWorthyProvider
from app.data_providers.slate_providers.recommended_reads_slate_provider import RecommendedReadsSlateProvider
from app.data_providers.slate_providers.top_saved_slate_provider import TopSavedSlateProvider
from app.data_providers.slate_providers.topic_slate_provider_factory import TopicSlateProviderFactory
from app.data_providers.snowplow.config import create_snowplow_tracker, SnowplowConfig
from app.data_providers.snowplow.snowplow_corpus_recommendations_tracker import SnowplowCorpusRecommendationsTracker
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.unleash_provider import UnleashProvider
from app.data_providers.user_impression_cap_provider import UserImpressionCapProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.models.api_client import ApiClient
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.localemodel import LocaleModel
from app.models.request_user import RequestUser
from app.models.unleash_assignment import UnleashAssignmentModel
from tests.assets.topics import technology_topic, entertainment_topic, self_improvement_topic


def _generate_slate(corpus_item_ids: List[str], headline='Foo Bar') -> CorpusSlateModel:
    return CorpusSlateModel(
        headline=headline,
        configuration_id=str(uuid.uuid4()),
        recommendations=[CorpusRecommendationModel(corpus_item=CorpusItemModel(id=id)) for id in corpus_item_ids]
    )


class MockSlateProvider:

    def __init__(self, slate):
        self.slate = slate

    async def get_slate(self):
        return self.slate


@pytest.mark.asyncio
class TestHomeDispatch:

    def setup(self):
        self.request_user = RequestUser(
            user_id=1,
            hashed_user_id='1-hashed',
        )

        self.corpus_client = MagicMock(CorpusFeatureGroupClient)
        self.preferences_provider = MagicMock(UserRecommendationPreferencesProvider)
        self.unleash_provider = MagicMock(UnleashProvider)

        self.home_dispatch = HomeDispatch(
            corpus_client=self.corpus_client,
            preferences_provider=self.preferences_provider,
            user_impression_cap_provider=MagicMock(UserImpressionCapProvider),
            topic_provider=MagicMock(TopicProvider),
            for_you_slate_provider=MagicMock(ForYouSlateProvider),
            recommended_reads_slate_provider=MagicMock(RecommendedReadsSlateProvider),
            topic_slate_providers=MagicMock(TopicSlateProviderFactory),
            collection_slate_provider=MagicMock(CollectionSlateProvider),
            pocket_hits_slate_provider=MagicMock(PocketHitsSlateProvider),
            life_hacks_slate_provider=MagicMock(LifeHacksSlateProvider),
            unleash_provider=self.unleash_provider,
            snowplow=SnowplowCorpusRecommendationsTracker(
                tracker=create_snowplow_tracker(), snowplow_config=SnowplowConfig()),
            pocket_worthy_provider=MagicMock(PocketWorthyProvider),
            top_saved_provider=MagicMock(TopSavedSlateProvider),
            author_faves_provider=MagicMock(AuthorFavesSlateProvider),
        )

    async def test_dedupe_and_limit(self):
        """
        Test that corpus recommendations are deduplicated across slates in the Home lineup.
        """
        self.unleash_provider.get_assignment.return_value = UnleashAssignmentModel(assigned=False, name=POCKET_HOME_V3_FEATURE_FLAG)
        self.preferences_provider.fetch.return_value = None
        self.home_dispatch.recommended_reads_slate_provider.get_slate.return_value = _generate_slate(
            ['Tech2', 'Ent4'], headline='Collections')
        self.home_dispatch.pocket_hits_slate_provider.get_slate.return_value = _generate_slate(
            ['PH1', 'PH2', 'PH3'], headline='Pocket Hits')
        self.home_dispatch.collection_slate_provider.get_slate.return_value = _generate_slate(
            ['Tech1', 'Ent2', 'Self1'], headline='Collections')
        self.home_dispatch.life_hacks_slate_provider.get_slate.return_value = _generate_slate(
            ['LifeHack1', 'LifeHack2'], headline='Life Hacks')
        self.home_dispatch.topic_provider.get_topics.return_value = [
            technology_topic, entertainment_topic, self_improvement_topic
        ]
        self.home_dispatch.topic_slate_providers.__getitem__.side_effect = [
            MockSlateProvider(_generate_slate(['Tech1', 'Tech2', 'Tech3', 'Tech4'], headline='Technology')),
            MockSlateProvider(_generate_slate(['Ent1', 'Ent2', 'Ent3'], headline='Entertainment')),
            MockSlateProvider(_generate_slate(['Self1'], headline='Self-improvement')),
        ]

        lineup = await self.home_dispatch.get_slate_lineup(
            user=self.request_user, locale=LocaleModel.en_US, recommendation_count=2,
            api_client=ApiClient(
                consumer_key='web-client-consumer-key',
                api_id='94110',
                application_name='Pocket web-client',
                is_native=True,
                is_trusted=True,
            ))

        assert [
                   ['Tech2', 'Ent4'],
                   ['PH1', 'PH2'],
                   ['Tech1', 'Ent2'],
                   ['LifeHack1', 'LifeHack2'],
                   ['Tech3', 'Tech4'],
                   ['Ent1', 'Ent3'],  # 'Ent2' is removed because it occurs in the Collection slate.
                   ['Self1'],  # 'Self1' is not removed because it's outside the top 2 of the Collection slate.
               ] == [[rec.corpus_item.id for rec in slate.recommendations] for slate in lineup.slates]
