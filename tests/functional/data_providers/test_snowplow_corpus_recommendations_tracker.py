import json
from datetime import datetime

import pytest
from aio_snowplow_tracker import Emitter, Tracker

from app.data_providers.snowplow.config import create_snowplow_tracker, SnowplowConfig
from app.data_providers.snowplow.snowplow_corpus_recommendations_tracker import SnowplowCorpusRecommendationsTracker
from app.models.corpus_recommendations_send_event import CorpusRecommendationsSendEvent
from app.models.corpus_slate_lineup_model import RecommendationSurfaceId
from app.models.localemodel import LocaleModel
from app.models.unleash_assignment import UnleashAssignmentModel
from tests.functional.test_util.snowplow import wait_for_snowplow_events


@pytest.fixture
def slate_send_event(corpus_slate_10_business_recs, web_client):
    return CorpusRecommendationsSendEvent(
        corpus_slate=corpus_slate_10_business_recs,
        recommendation_surface_id=RecommendationSurfaceId.NEW_TAB_EN_US,
        api_client=web_client,
        locale=LocaleModel.en_US,
    )


@pytest.fixture
def slate_lineup_send_event(lineup_with_business_slate, user_1, web_client):
    return CorpusRecommendationsSendEvent(
        corpus_slate_lineup=lineup_with_business_slate,
        recommendation_surface_id=RecommendationSurfaceId.NEW_TAB_EN_US,
        user=user_1,
        api_client=web_client,
        locale=LocaleModel.en_US,
    )


@pytest.fixture
def snowplow_recs_tracker():
    return SnowplowCorpusRecommendationsTracker(create_snowplow_tracker(), SnowplowConfig())


@pytest.mark.asyncio
async def test_track_slate_lineup(snowplow_micro, snowplow_recs_tracker, slate_lineup_send_event, caplog):
    await snowplow_recs_tracker.track(slate_lineup_send_event)

    # No warnings, errors, or critical log statements were created.
    assert not any(r for r in caplog.records if r.levelname in ('WARNING', 'ERROR', 'CRITICAL'))

    await wait_for_snowplow_events(snowplow_micro, n_expected_event=1)
    all_snowplow_events = snowplow_micro.get_event_counts()
    assert all_snowplow_events == {'total': 1, 'good': 1, 'bad': 0}


@pytest.mark.asyncio
async def test_track_slate(snowplow_micro, snowplow_recs_tracker, slate_send_event, caplog):
    await snowplow_recs_tracker.track(slate_send_event)

    # No warnings, errors, or critical log statements were created.
    assert not any(r for r in caplog.records if r.levelname in ('WARNING', 'ERROR', 'CRITICAL'))

    await wait_for_snowplow_events(snowplow_micro, n_expected_event=1)
    all_snowplow_events = snowplow_micro.get_event_counts()
    assert all_snowplow_events == {'total': 1, 'good': 1, 'bad': 0}


@pytest.mark.asyncio
async def test_track_engagement_updated_at(snowplow_micro, snowplow_recs_tracker, slate_send_event):
    # Simulate items being ranked with engagement data.
    recommendations = slate_send_event.corpus_slate.recommendations
    for i, rec in enumerate(recommendations):
        rec.corpus_item.ranked_with_engagement_updated_at = datetime(2023, 5, 8, 12, 0, i % 60)

    await snowplow_recs_tracker.track(slate_send_event)

    await wait_for_snowplow_events(snowplow_micro, n_expected_event=1)
    all_snowplow_events = snowplow_micro.get_event_counts()
    assert all_snowplow_events == {'total': 1, 'good': 1, 'bad': 0}

    # Check that engagement timestamp was sent to Snowplow
    good_event = json.dumps(snowplow_micro.get_good_events()[0]['event'])
    assert good_event.count('"ranked_with_engagement_updated_at"') == len(recommendations)


@pytest.mark.asyncio
async def test_track_tile_id(snowplow_micro, snowplow_recs_tracker, slate_send_event):
    # Add tile_id to recommendations.
    recommendations = slate_send_event.corpus_slate.recommendations
    for i, rec in enumerate(recommendations):
        rec.tile_id = 1000 + i

    await snowplow_recs_tracker.track(slate_send_event)

    # Assert two events were sent to Snowplow: an event with recommendation metadata and a variant_enroll event.
    await wait_for_snowplow_events(snowplow_micro, n_expected_event=1)
    all_snowplow_events = snowplow_micro.get_event_counts()
    assert all_snowplow_events == {'total': 1, 'good': 1, 'bad': 0}

    # Check that engagement timestamp was sent to Snowplow
    good_event = json.dumps(snowplow_micro.get_good_events()[0]['event'])
    assert good_event.count('"corpus_recommendation_tile_id"') == len(recommendations)


@pytest.mark.asyncio
async def test_track_experiment(snowplow_micro, snowplow_recs_tracker, slate_lineup_send_event):
    slate_lineup_send_event.experiment = UnleashAssignmentModel(assigned=True, name='getstarted', variant='control')

    await snowplow_recs_tracker.track(slate_lineup_send_event)

    # Assert two events were sent to Snowplow: an event with recommendation metadata and a variant_enroll event.
    await wait_for_snowplow_events(snowplow_micro, n_expected_event=2)
    all_snowplow_events = snowplow_micro.get_event_counts()
    assert all_snowplow_events == {'total': 2, 'good': 2, 'bad': 0}


@pytest.mark.asyncio
async def test_track_failure_response(slate_lineup_send_event, caplog):
    # Simulate a server failure by connecting the Snowplow tracker to the wrong host.
    snowplow_tracker = Tracker(Emitter('localhost', protocol='http', method='post', buffer_size=1))
    corpus_recommendations_tracker = SnowplowCorpusRecommendationsTracker(snowplow_tracker, SnowplowConfig())

    # Snowplow server errors don't cause an exception. Our service should continue to function independent of Snowplow.
    await corpus_recommendations_tracker.track(slate_lineup_send_event)

    # Assert that a 501 status code was logged.
    error_logs = [r for r in caplog.records if r.levelname == 'ERROR']
    assert len(error_logs) == 1
    assert "Cannot connect to host localhost" in error_logs[0].message
