import random

import pytest

from app.data_providers.slate_providers.new_tab_slate_provider import NewTabSlateProvider
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel
from tests.mocks.corpus_clients import CORPUS_API_CLIENT_FIXTURE_ITEM_COUNT
from tests.assets.topics import all_topic_fixtures


@pytest.fixture
def new_tab_slate_provider(corpus_api_client, corpus_engagement_provider):
    return NewTabSlateProvider(
        corpus_api_client=corpus_api_client,
        corpus_engagement_provider=corpus_engagement_provider,
        recommendation_surface_id=RecommendationSurfaceId.NEW_TAB_EN_US,
        locale=LocaleModel.en_US
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
    return [CorpusItemModel(id=str(i), topic=random.choice(all_topic_fixtures).corpus_topic_id) for i in range(10)]


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

    async def test_rank_corpus_items_with_engagement_failure(
            self, new_tab_slate_provider_with_engagement_failure, corpus_items_10, caplog, aiocache_functions_fixture):
        ranked_items = await new_tab_slate_provider_with_engagement_failure.rank_corpus_items(items=corpus_items_10)

        # Recommendations should be returned (without Thompson sampling), and an error should be logged.
        assert len(corpus_items_10) == len(ranked_items)
        assert any(r.levelname == 'ERROR' for r in caplog.records)
