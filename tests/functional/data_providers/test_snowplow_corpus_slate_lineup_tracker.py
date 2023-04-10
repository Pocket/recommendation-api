import asyncio

from app.data_providers.snowplow.config import SnowplowConfig
from app.data_providers.snowplow.snowplow_corpus_recommendations_tracker import SnowplowCorpusRecommendationsTracker
from app.models.corpus_recommendations_send_event import CorpusRecommendationsSendEvent
from app.models.unleash_assignment import UnleashAssignmentModel

# PyTest is not able to find fixtures in these files without importing them.
from tests.mocks.snowplow import *
from tests.mocks.corpus_slate_lineup_model import *
from tests.mocks.user import *
from tests.mocks.api_client import *


@pytest.mark.asyncio
async def test_track_successful_slate_lineup_response(snowplow_server, lineup_with_business_slate, user_1, caplog, web_client):
    snowplow_tracker = create_snowplow_tracker(snowplow_server)
    corpus_recommendations_tracker = SnowplowCorpusRecommendationsTracker(snowplow_tracker, SnowplowConfig())
    await corpus_recommendations_tracker.track(CorpusRecommendationsSendEvent(
        corpus_slate_lineup=lineup_with_business_slate,
        recommendation_surface_id=RecommendationSurfaceId.HOME,
        user=user_1,
        api_client=web_client,
        locale=LocaleModel.en_US,
    ))

    # No warnings, errors, or critical log statements were created.
    assert not any(r for r in caplog.records if r.levelname in ('WARNING', 'ERROR', 'CRITICAL'))
    # Assert one request was made to Snowplow
    assert len(snowplow_server.app['requests']) == 1


@pytest.mark.asyncio
async def test_track_successful_response(snowplow_tracker, corpus_slate_10_business_recs, user_1, caplog, web_client):
    corpus_recommendations_tracker = SnowplowCorpusRecommendationsTracker(snowplow_tracker, SnowplowConfig())
    await corpus_recommendations_tracker.track(CorpusRecommendationsSendEvent(
        corpus_slate=corpus_slate_10_business_recs,
        recommendation_surface_id=RecommendationSurfaceId.NEW_TAB_EN_US,
        api_client=web_client,
        locale=LocaleModel.en_US,
    ))

    # No warnings, errors, or critical log statements were created.
    assert not any(r for r in caplog.records if r.levelname in ('WARNING', 'ERROR', 'CRITICAL'))


@pytest.mark.asyncio
async def test_track_successful_experiment_response(
        snowplow_server, lineup_with_business_slate, user_1, caplog, web_client):
    snowplow_tracker = create_snowplow_tracker(snowplow_server)

    slate_tracker = SnowplowCorpusRecommendationsTracker(snowplow_tracker, SnowplowConfig())
    await slate_tracker.track(CorpusRecommendationsSendEvent(
        corpus_slate_lineup=lineup_with_business_slate,
        recommendation_surface_id=RecommendationSurfaceId.HOME,
        user=user_1,
        api_client=web_client,
        locale=LocaleModel.en_US,
        experiment=UnleashAssignmentModel(assigned=True, name='getstarted', variant='control')
    ))

    # No warnings, errors, or critical log statements were created.
    assert not any(r for r in caplog.records if r.levelname in ('WARNING', 'ERROR', 'CRITICAL'))
    # Assert two requests were made to Snowplow: an event with recommendation metadata and a variant_enroll event.
    assert len(snowplow_server.app['requests']) == 2


@pytest.mark.asyncio
async def test_track_failure_response(
        snowplow_tracker_with_server_failure, lineup_with_business_slate, user_1, caplog, web_client):
    corpus_recommendations_tracker = SnowplowCorpusRecommendationsTracker(
        snowplow_tracker_with_server_failure, SnowplowConfig())
    # Snowplow server errors don't cause an exception. Our service should continue to function independent of Snowplow.
    await corpus_recommendations_tracker.track(CorpusRecommendationsSendEvent(
        corpus_slate_lineup=lineup_with_business_slate,
        recommendation_surface_id=RecommendationSurfaceId.NEW_TAB_EN_US,
        api_client=web_client,
        locale=LocaleModel.en_US,
    ))

    # Assert that a 501 status code was logged.
    error_logs = [r for r in caplog.records if r.levelname == 'ERROR']
    assert len(error_logs) == 1
    assert "status code: 501" in error_logs[0].message
