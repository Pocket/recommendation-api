import random

import pytest

from app.data_providers.slate_providers.new_tab_slate_provider import NewTabSlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel
from tests.assets.topics import all_topic_fixtures


@pytest.fixture
def new_tab_slate_provider(corpus_feature_group_client, corpus_engagement_provider, translation_provider):
    return NewTabSlateProvider(
        corpus_feature_group_client=corpus_feature_group_client,
        corpus_engagement_provider=corpus_engagement_provider,
        recommendation_surface_id=RecommendationSurfaceId.NEW_TAB_EN_US,
        locale=LocaleModel.en_US,
        translation_provider=translation_provider,
    )


@pytest.fixture
def new_tab_slate_provider_with_engagement_failure(new_tab_slate_provider, failing_corpus_engagement_provider):
    new_tab_slate_provider.corpus_engagement_provider = failing_corpus_engagement_provider
    return new_tab_slate_provider


@pytest.mark.asyncio
class TestNewTabSlateProvider:

    async def test_rank_corpus_items(self, new_tab_slate_provider, caplog, aiocache_functions_fixture):
        items = [CorpusItemModel(id=str(i), topic=random.choice(all_topic_fixtures).corpus_topic_id) for i in range(10)]

        ranked_items = await new_tab_slate_provider.rank_corpus_items(items=items)

        assert len(items) == len(ranked_items)
        assert not any(r.levelname == 'ERROR' for r in caplog.records)

    async def test_rank_corpus_items_with_engagement_failure(
            self, new_tab_slate_provider_with_engagement_failure, caplog, aiocache_functions_fixture):
        items = [CorpusItemModel(id=str(i), topic=random.choice(all_topic_fixtures).corpus_topic_id) for i in range(10)]

        ranked_items = await new_tab_slate_provider_with_engagement_failure.rank_corpus_items(items=items)

        # Recommendations should be returned (without Thompson sampling), and an error should be logged.
        assert len(items) == len(ranked_items)
        assert any(r.levelname == 'ERROR' for r in caplog.records)