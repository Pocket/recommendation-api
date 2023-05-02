import random
import string

import pytest

from app.data_providers.slate_providers.new_tab_slate_provider import NewTabSlateProvider, PUBLISHER_SPREAD_DISTANCE
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel
from tests.mocks.corpus_clients import CORPUS_API_CLIENT_FIXTURE_ITEM_COUNT
from tests.assets.topics import all_topic_fixtures


@pytest.fixture
def new_tab_slate_provider(corpus_api_client, corpus_engagement_provider, translation_provider):
    return NewTabSlateProvider(
        corpus_api_client=corpus_api_client,
        corpus_engagement_provider=corpus_engagement_provider,
        recommendation_surface_id=RecommendationSurfaceId.NEW_TAB_EN_US,
        locale=LocaleModel.en_US,
        translation_provider=translation_provider,
    )


@pytest.fixture
def new_tab_slate_provider_with_engagement_failure(new_tab_slate_provider, failing_corpus_engagement_provider):
    new_tab_slate_provider.corpus_engagement_provider = failing_corpus_engagement_provider
    return new_tab_slate_provider


@pytest.fixture
def new_tab_slate_provider_without_scheduled_date(new_tab_slate_provider, corpus_api_client_without_scheduled_date):
    new_tab_slate_provider.corpus_api_client = corpus_api_client_without_scheduled_date
    return new_tab_slate_provider


@pytest.fixture
def corpus_items_10():
    return [
        CorpusItemModel(
            id=str(i),
            topic=random.choice(all_topic_fixtures).corpus_topic_id,
            publisher=f'Publisher {random.choice(string.ascii_uppercase)}'
        ) for i in range(10)
    ]


@pytest.mark.asyncio
class TestNewTabSlateProvider:

    async def test_get_slate(self, new_tab_slate_provider, corpus_items_10, caplog, aiocache_functions_fixture):
        slate = await new_tab_slate_provider.get_slate()

        assert CORPUS_API_CLIENT_FIXTURE_ITEM_COUNT == len(slate.recommendations)
        assert not any(r.levelname == 'ERROR' for r in caplog.records)

    async def test_get_slate_without_scheduled_date(
            self, new_tab_slate_provider_without_scheduled_date, corpus_items_10, caplog, aiocache_functions_fixture):
        slate = await new_tab_slate_provider_without_scheduled_date.get_slate()

        assert CORPUS_API_CLIENT_FIXTURE_ITEM_COUNT == len(slate.recommendations)
        errors = [r for r in caplog.records if r.levelname == 'ERROR']
        assert len(errors) > 0
        assert 'scheduled_date' in errors[0].message

    async def test_rank_corpus_items(self, new_tab_slate_provider, corpus_items_10, caplog, aiocache_functions_fixture):
        ranked_items = await new_tab_slate_provider.rank_corpus_items(items=corpus_items_10)

        assert len(corpus_items_10) == len(ranked_items)
        assert not any(r.levelname == 'ERROR' for r in caplog.records)

    @pytest.mark.parametrize('repeat', range(10))  # Thompson sampling is non-deterministic, so repeat the test.
    async def test_publisher_spread(
            self, new_tab_slate_provider_without_scheduled_date, corpus_items_10, aiocache_functions_fixture, repeat):
        # Introduce one duplicate publisher 'Publisher 0'
        for i, corpus_item in enumerate(corpus_items_10):
            corpus_item.publisher = 'Duplicate Publisher' if i < 2 else f'Publisher {i}'

        ranked_items = await new_tab_slate_provider_without_scheduled_date.rank_corpus_items(items=corpus_items_10)

        assert len(corpus_items_10) == len(ranked_items)
        indices = [i for i, corpus_item in enumerate(ranked_items) if corpus_item.publisher == 'Duplicate Publisher']
        # 'Duplicate Publisher' is expected to be ranked at the bottom or at least a certain distance apart.
        # This is because the publisher spreading won't rank recs higher because they have a duplicate publisher.
        assert indices[1] == len(ranked_items) - 1 or indices[1] - indices[0] >= PUBLISHER_SPREAD_DISTANCE

    async def test_rank_corpus_items_with_engagement_failure(
            self, new_tab_slate_provider_with_engagement_failure, corpus_items_10, caplog, aiocache_functions_fixture):
        ranked_items = await new_tab_slate_provider_with_engagement_failure.rank_corpus_items(items=corpus_items_10)

        # Recommendations should be returned (without Thompson sampling), and an error should be logged.
        assert len(corpus_items_10) == len(ranked_items)
        assert any(r.levelname == 'ERROR' for r in caplog.records)
