from typing import List

import pytest
from aws_xray_sdk import global_sdk_config

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.dispatch import SetupMomentDispatch, HomeDispatch
from app.data_providers.slate_providers.collection_slate_provider import CollectionSlateProvider
from app.data_providers.slate_providers.personalized_for_you_slate_provider import ForYouSlateProvider
from app.data_providers.slate_providers.topic_slate_provider import TopicSlateProvider
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.models.corpus_item_model import CorpusItemModel
from unittest.mock import MagicMock

from app.models.corpus_recommendation_model import CorpusRecommendationModel
from app.models.corpus_slate_model import CorpusSlateModel
from app.models.user_ids import UserIds


def _generate_slate(corpus_item_ids: List[str], headline='Foo Bar') -> CorpusSlateModel:
    return CorpusSlateModel(
        headline=headline,
        recommendations=[CorpusRecommendationModel(corpus_item=CorpusItemModel(id=id)) for id in corpus_item_ids]
    )


@pytest.mark.asyncio
class TestHomeDispatch:

    def setup(self):
        global_sdk_config.set_sdk_enabled(False)

        self.user_ids = UserIds(
            user_id=1,
            hashed_user_id='1-hashed',
        )

        self.corpus_client = MagicMock(CorpusFeatureGroupClient)
        self.preferences_provider = MagicMock(UserRecommendationPreferencesProvider)

        self.home_dispatch = HomeDispatch(
            corpus_client=self.corpus_client,
            preferences_provider=self.preferences_provider,
            topic_provider=MagicMock(TopicProvider),
            for_you_slate_provider=MagicMock(ForYouSlateProvider),
            topic_slate_provider=MagicMock(TopicSlateProvider),
            collection_slate_provider=MagicMock(CollectionSlateProvider),
        )

    async def test_dedupe_and_limit(self):
        """
        Test that corpus recommendations are deduplicated across slates in the Home lineup.
        """
        self.preferences_provider.fetch.return_value = None
        self.home_dispatch.collection_slate_provider.get_slate.return_value = _generate_slate(
            ['Tech1', 'Ent2', 'Self1'], headline='Collections')
        self.home_dispatch.topic_slate_provider.get_slates.return_value = [
            _generate_slate(['Tech1', 'Tech2', 'Tech3'], headline='Technology'),
            _generate_slate(['Ent1', 'Ent2', 'Ent3'], headline='Entertainment'),
            _generate_slate(['Self1'], headline='Self-improvement'),
        ]

        lineup = await self.home_dispatch.get_slate_lineup(user=self.user_ids, slate_count=10, recommendation_count=2)

        assert [
            ['Tech1', 'Ent2'],
            ['Tech2', 'Tech3'],
            ['Ent1', 'Ent3'],  # 'Ent2' is removed because it occurs in the Collection slate.
            ['Self1'],  # 'Self1' is not removed because it's outside the top 2 of the Collection slate.
        ] == [[rec.corpus_item.id for rec in slate.recommendations] for slate in lineup.slates]
