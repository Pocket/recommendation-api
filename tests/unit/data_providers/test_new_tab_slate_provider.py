import random
import string
from datetime import datetime, timezone

import pytest

from app.data_providers.slate_providers.new_tab_slate_provider import NewTabSlateProvider, PUBLISHER_SPREAD_DISTANCE
from app.models.corpus_item_model import CorpusItemModel
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from tests.mocks.corpus_clients import CORPUS_API_CLIENT_FIXTURE_ITEM_COUNT
from tests.assets.topics import all_topic_fixtures, business_topic


@pytest.fixture
def new_tab_slate_provider(corpus_api_client, corpus_engagement_provider):
    return NewTabSlateProvider(
        corpus_api_client=corpus_api_client,
        corpus_engagement_provider=corpus_engagement_provider,
        recommendation_surface_id=RecommendationSurfaceId.NEW_TAB_EN_US,
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
    async def test_rank_by_scheduled_date_rank(
            self, new_tab_slate_provider, corpus_items_10, aiocache_functions_fixture, repeat):
        # Avoid any duplicate publisher in this test.
        for i, corpus_item in enumerate(corpus_items_10):
            corpus_item.publisher = f'Publisher {i}'

        ranked_items = await new_tab_slate_provider.rank_corpus_items(items=corpus_items_10)

        assert len(corpus_items_10) == len(ranked_items)
        # Assert items are ranked by scheduled date in descending order
        last_scheduled_date = None
        for corpus_item in ranked_items:
            scheduled_date = new_tab_slate_provider.corpus_api_client.get_scheduled_date(corpus_item.id)
            if last_scheduled_date is not None:
                assert last_scheduled_date >= scheduled_date
            last_scheduled_date = scheduled_date

    # When making changes to Thompson sampling, run this test 100x the normal repeat value to ensure it reliably passes.
    @pytest.mark.parametrize('repeat', range(10))
    async def test_rank_by_thompson_sampling(
            self, new_tab_slate_provider_without_scheduled_date, corpus_items_10, aiocache_functions_fixture, repeat):
        # Make all publishers unique, to ensure publisher spreading has no effect on the ranking.
        for i, corpus_item in enumerate(corpus_items_10):
            corpus_item.publisher = f'Publisher {i}'

        fixture_item_id_with_high_ctr = '7'

        top_ranked_ids = []
        bottom_ranked_ids = []
        for i in range(50):
            ranked_items = await new_tab_slate_provider_without_scheduled_date.rank_corpus_items(items=corpus_items_10)
            top_ranked_ids.append(ranked_items[0].id)
            bottom_ranked_ids.append(ranked_items[-1].id)

        # The NewTabSlateProvider fixture receives engagement data from corpus_engagement.json, which has a 5% CTR for
        # id=7 with 10,000 impressions. The prior is lower than 5%, so id 7 should be ranked first most often.
        most_frequent_top_ranked_id = max(set(top_ranked_ids), key=top_ranked_ids.count)
        assert most_frequent_top_ranked_id == fixture_item_id_with_high_ctr
        # All other items are ranked by the prior, so the bottom ranked item should vary.
        assert len(set(bottom_ranked_ids)) > 3  # Should be close to 8 with high probability.

    # When making changes to Thompson sampling, run this test 100x the normal repeat value to ensure it reliably passes.
    @pytest.mark.parametrize('repeat', range(10))
    async def test_rank_corpus_items_with_region_metrics(
            self, new_tab_slate_provider_without_scheduled_date, corpus_items_10, aiocache_functions_fixture, repeat):
        # Make all publishers unique to ensure publisher spreading has no effect on the ranking.
        for i, corpus_item in enumerate(corpus_items_10):
            corpus_item.publisher = f'Publisher {i}'

        # corpus_engagement.json has:
        # - 10000 / 100000 = 10% CTR in CA for item_id 6
        # - 5000 / 300000 = 1.7% CTR globally for item 6
        # - 50000 / 1000000 = 5% CTR globally for item_id 7
        fixture_item_id_with_high_global_ctr = '7'
        fixture_item_id_with_high_region_ctr = '6'

        top_ranked_ids = []
        bottom_ranked_ids = []
        n_iterations = 50
        for i in range(n_iterations):
            ranked_items = await new_tab_slate_provider_without_scheduled_date.rank_corpus_items(
                items=corpus_items_10,
                enable_ranking_by_region=True,
                region='CA'
            )
            top_ranked_ids.append(ranked_items[0].id)
            bottom_ranked_ids.append(ranked_items[-1].id)

        # Count the occurrences of the top ranked item
        high_ctr_global_item_top_count = top_ranked_ids.count(fixture_item_id_with_high_global_ctr)
        high_ctr_region_item_top_count = top_ranked_ids.count(fixture_item_id_with_high_region_ctr)

        assert high_ctr_region_item_top_count > high_ctr_global_item_top_count
        # The item with 10% CTR in the region should end up on top 50% of the time with high probability.
        assert high_ctr_region_item_top_count > n_iterations / 2
        # All other items are ranked by the prior, so the bottom ranked item should vary.
        assert len(set(bottom_ranked_ids)) > 3  # Should be close to 8 with high probability.

    @pytest.mark.parametrize('repeat', range(10))  # Thompson sampling is non-deterministic, so repeat the test.
    async def test_rank_by_publisher_spread(
            self, new_tab_slate_provider, corpus_items_10, aiocache_functions_fixture, repeat):
        # Introduce one duplicate publisher
        for i, corpus_item in enumerate(corpus_items_10):
            corpus_item.publisher = 'Duplicate Publisher' if i < 2 else f'Publisher {i}'

        ranked_items = await new_tab_slate_provider.rank_corpus_items(items=corpus_items_10)

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

    async def test_boost_syndicated_article(self, new_tab_slate_provider, corpus_items_10, aiocache_functions_fixture):
        # Append a syndicated article
        syndicated_article = CorpusItemModel(
            id='syndicated-rec',
            topic=business_topic.corpus_topic_id,
            publisher='The Original Publisher',
            url='https://getpocket.com/explore/item/this-is-a-syndicated-article',
        )
        corpus_items_10.append(syndicated_article)

        ranked_items = await new_tab_slate_provider.rank_corpus_items(items=corpus_items_10)

        assert len(corpus_items_10) == len(ranked_items)
        assert ranked_items[1] == syndicated_article

    @pytest.mark.parametrize(
        ('recommendation_surface_id', 'expected_utm_source'),
        [
            (RecommendationSurfaceId.NEW_TAB_EN_US, 'pocket-newtab-en-us'),
            (RecommendationSurfaceId.NEW_TAB_EN_GB, 'pocket-newtab-en-gb'),
            (RecommendationSurfaceId.NEW_TAB_EN_INTL, 'pocket-newtab-en-intl'),
            (RecommendationSurfaceId.NEW_TAB_DE_DE, 'pocket-newtab-de-de'),
            (RecommendationSurfaceId.NEW_TAB_ES_ES, 'pocket-newtab-es-es'),
            (RecommendationSurfaceId.NEW_TAB_FR_FR, 'pocket-newtab-fr-fr'),
            (RecommendationSurfaceId.NEW_TAB_IT_IT, 'pocket-newtab-it-it'),
        ]
    )
    async def test_rank_corpus_items(
            self, recommendation_surface_id, expected_utm_source, corpus_api_client, corpus_engagement_provider):
        new_tab_slate_provider = NewTabSlateProvider(
            corpus_api_client=corpus_api_client,
            corpus_engagement_provider=corpus_engagement_provider,
            recommendation_surface_id=recommendation_surface_id,
        )

        slate = await new_tab_slate_provider.get_slate()

        assert expected_utm_source == slate.utm_source
