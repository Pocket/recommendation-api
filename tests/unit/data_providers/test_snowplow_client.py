import pytest
import json

from app.data_providers.snowplow_client import SnowplowClient
from app.graphql.corpus_item import CorpusItem


class MockTracker():
    def __init__(self):
        self.tracked_contexts = []
        self.tracked_events = []
        self.flush_called = False

    def track_self_describing_event(self, context, event_json):
        self.tracked_contexts.append(context)
        self.tracked_events.append(event_json)
        return self

    def flush(self):
        self.flush_called = True
        return self

@pytest.mark.asyncio
async def test_log_event():
    mock_tracker = MockTracker()

    snowplow_tracking = SnowplowClient(tracker=mock_tracker)

    test_user_id = 14464
    await snowplow_tracking.log_event(
        user_id=test_user_id,
        slate_id="uuid-representing-a-slate",
        items = [CorpusItem(id='example-uuid-1'), CorpusItem(id='example-uuid-2'), CorpusItem(id='example-uuid-3')]
    )

    assert len(mock_tracker.tracked_contexts) == 4
    assert mock_tracker.tracked_contexts[0][0].schema == "iglu:com.pocket/recommendation_result/jsonschema/1-0-0"
    assert mock_tracker.tracked_contexts[0][0].data.get("slate_id") == "uuid-representing-a-slate"
    assert [item.get("scheduled_corpus_item_id") for item in mock_tracker.tracked_contexts[0][0].data.get("recommendation_result_items")] == \
           ['example-uuid-1', 'example-uuid-2', 'example-uuid-3']

    assert all([context[0].schema == "iglu:com.pocket/tile_recommendation_mapping/jsonschema/1-0-0" for context in mock_tracker.tracked_contexts[1:3]])
    assert all([context[0].data.get('slate_id') == "uuid-representing-a-slate" for context in mock_tracker.tracked_contexts[1:3]])
    
    assert mock_tracker.tracked_contexts[1][0].data.get('scheduled_corpus_item_external_id') == "example-uuid-1"
    assert mock_tracker.tracked_contexts[1][0].data.get('url') == "example-uuid-1"
    assert mock_tracker.tracked_contexts[2][0].data.get('scheduled_corpus_item_external_id') == "example-uuid-2"
    assert mock_tracker.tracked_contexts[2][0].data.get('url') == "example-uuid-2"
    assert mock_tracker.tracked_contexts[3][0].data.get('scheduled_corpus_item_external_id') == "example-uuid-3"
    assert mock_tracker.tracked_contexts[3][0].data.get('url') == "example-uuid-3"

    assert len(mock_tracker.tracked_events) == 4
    assert all([event.schema == "iglu:com.pocket/object_update/jsonschema/1-0-6" for event in mock_tracker.tracked_events])

    mock_tracker.tracked_events[0].data.get('object') == "recommendation_result"
    assert all([event.data.get('object') == "tile_recommendation_mapping" for event in mock_tracker.tracked_events[1:]])

    assert mock_tracker.flush_called

