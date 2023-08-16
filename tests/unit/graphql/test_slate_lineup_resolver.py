import logging
from unittest.mock import patch

import pytest

from app.graphql.resolvers.legacy.slate_lineup_resolver import resolve_get_slate_lineup
from app.models.slate_lineup import SlateLineupModel
from tests.mocks.graphql import mock_graphql_request_info


@pytest.mark.asyncio
async def test_resolve_get_slate_lineup_log_message(mock_graphql_request_info, caplog):
    dummy_slate_lineup = SlateLineupModel(id='123', requestId='', slates=[])

    with patch.object(SlateLineupModel, 'get_slate_lineup', return_value=dummy_slate_lineup):
        with caplog.at_level(logging.INFO):
            graphql_slate_lineup = await resolve_get_slate_lineup(
                root=None,
                info=mock_graphql_request_info,
                slate_lineup_id='123'
            )

            assert graphql_slate_lineup.id == '123'

            assert any(
                r.levelname == 'INFO' and 'resolving getSlateLineup with slate_lineup_id=123' in r.message
                for r in caplog.records
            ), f'Expected log record not found in {caplog.records}'
