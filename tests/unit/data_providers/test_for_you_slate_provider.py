import os
from unittest.mock import MagicMock

import pytest

from app.config import ROOT_DIR
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.corpus_engagement_provider import CorpusEngagementProvider
from app.data_providers.slate_providers.for_you_slate_provider import ForYouSlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.recommendation_reason_type import RecommendationReasonType
from tests.assets.topics import business_topic, all_topic_fixtures
from tests.mocks.feature_store_mock import FeatureStoreMock


@pytest.mark.asyncio
class TestForYouSlateProvider:

    def setup(self):
        self.feature_store_mock = FeatureStoreMock(
            feature_group_name=CorpusFeatureGroupClient.get_feature_group_name(),
            records_json_path=os.path.join(ROOT_DIR, 'tests/assets/json/corpus_candidate_sets.json')
        )

        self.engagement_provider = MagicMock(CorpusEngagementProvider)
        self.engagement_provider.get.return_value = dict()

        self.corpus_feature_group_client = CorpusFeatureGroupClient(aioboto3_session=self.feature_store_mock.aioboto3)
        self.slate_provider = ForYouSlateProvider(
            corpus_feature_group_client=self.corpus_feature_group_client,
            corpus_engagement_provider=self.engagement_provider,
            recommendation_surface_id=RecommendationSurfaceId.HOME,
        )

    async def test_rank_corpus_items_single_preferred_topic(self):
        items = [CorpusItemModel(id=str(i), topic=all_topic_fixtures[i % 2].corpus_topic_id) for i in range(10)]
        preferred_topics = [all_topic_fixtures[0]]
        preferred_topic_items = [r for r in items if any(r.topic == p.corpus_topic_id for p in preferred_topics)]

        ranked_items = await self.slate_provider.rank_corpus_items(
            items=items, preferred_topics=preferred_topics, user_impression_capped_list=[])

        assert len(items) == len(ranked_items)
        # Assert recs with preferred topic are ranked first.
        assert set(r.id for r in ranked_items[:len(preferred_topic_items)]) == set(r.id for r in preferred_topic_items)

    async def test_rank_corpus_items_multiple_preferred_topics(self):
        items = [CorpusItemModel(id=str(i), topic=all_topic_fixtures[i % 5].corpus_topic_id) for i in range(20)]
        preferred_topics = [all_topic_fixtures[0], all_topic_fixtures[2], all_topic_fixtures[-1]]
        preferred_topic_items = [r for r in items if any(r.topic == p.corpus_topic_id for p in preferred_topics)]

        ranked_items = await self.slate_provider.rank_corpus_items(
            items=items, preferred_topics=preferred_topics, user_impression_capped_list=[])

        assert len(items) == len(ranked_items)
        # Assert recs with preferred topic are ranked first.
        assert set(r.id for r in ranked_items[:len(preferred_topic_items)]) == set(r.id for r in preferred_topic_items)
        # Assert topics are spread
        assert ranked_items[0].topic != ranked_items[1].topic
        assert ranked_items[1].topic != ranked_items[2].topic

    async def test_rank_corpus_items_topic_preferences_impression_capped(self):
        items = [CorpusItemModel(id=str(i), topic=all_topic_fixtures[i % 5].corpus_topic_id) for i in range(20)]
        preferred_topics = [all_topic_fixtures[0], all_topic_fixtures[2], all_topic_fixtures[-1]]
        preferred_corpus_topic_ids = {p.corpus_topic_id for p in preferred_topics}
        preferred_topic_items = [r for r in items if any(r.topic == p.corpus_topic_id for p in preferred_topics)]
        impression_capped_items = preferred_topic_items[:4]

        ranked_items = await self.slate_provider.rank_corpus_items(
            items=items, preferred_topics=preferred_topics, user_impression_capped_list=impression_capped_items)

        assert len(items) == len(ranked_items)
        # Assert that the first items are not impression capped, have preferred topics, and have topic spreading.
        n_preferred_topic_items_not_impression_capped = len(preferred_topic_items) - len(impression_capped_items)
        for i in range(n_preferred_topic_items_not_impression_capped):
            assert ranked_items[i] not in impression_capped_items
            assert ranked_items[i].topic in preferred_corpus_topic_ids
            assert ranked_items[i].topic != ranked_items[i + 1].topic

    async def test_get_slate_without_topic_preferences(self):
        slate = await self.slate_provider.get_slate(preferred_topics=[], user_impression_capped_list=[])

        assert 447 == len(slate.recommendations)  # Number of recommendations matches corpus_candidate_sets.json
        assert all(r.reason is None for r in slate.recommendations)

    async def test_get_slate_with_topic_preferences(self):
        slate = await self.slate_provider.get_slate(preferred_topics=[business_topic], user_impression_capped_list=[])

        assert 447 == len(slate.recommendations)  # Number of recommendations matches corpus_candidate_sets.json

        recs_with_reason = [r for r in slate.recommendations if r.reason is not None]
        assert 21 == len(recs_with_reason)  # Number of Business items in corpus_candidate_sets.json
        assert all(r.reason.name == 'Business' for r in recs_with_reason)
        assert all(r.reason.type == RecommendationReasonType.PREFERRED_TOPICS for r in recs_with_reason)

    async def test_thompson_sampling(self):
        items = [CorpusItemModel(id=str(i), topic=all_topic_fixtures[i % 2].corpus_topic_id) for i in range(10)]
        preferred_topics = [all_topic_fixtures[0]]
        preferred_topic_items = [r for r in items if any(r.topic == p.corpus_topic_id for p in preferred_topics)]

        top_ranked_item_ids = set()
        n = 20  # With 5 preferred topic items the probability that the same item ranks on top is 1/5^19 = 10^-14
        for _ in range(n):
            ranked_items = await self.slate_provider.rank_corpus_items(
                items=items,
                enable_thompson_sampling=True,
                preferred_topics=preferred_topics,
                user_impression_capped_list=[]
            )

            top_ranked_item_ids.add(ranked_items[0].id)
            assert len(items) == len(ranked_items)
            # Assert recs with preferred topic are ranked first
            assert set(r.id for r in ranked_items[:len(preferred_topic_items)]) == set(r.id for r in preferred_topic_items)

        # Assert that the same item is not always ranked at the top.
        assert len(top_ranked_item_ids) > 1
