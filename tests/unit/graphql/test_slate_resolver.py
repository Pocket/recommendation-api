import logging
from unittest.mock import patch

import pytest

from app.graphql.resolvers.legacy.slate_resolver import resolve_get_slate
from app.models.slate import SlateModel
from tests.mocks.graphql import mock_graphql_request_info


@pytest.mark.asyncio
async def test_resolve_get_slate_log_message(mock_graphql_request_info, caplog):
    with patch.object(SlateModel, 'get_slate', return_value=SlateModel(id='123', recommendations=[])):
        with caplog.at_level(logging.INFO):
            graphql_slate = await resolve_get_slate(
                root=None,
                info=mock_graphql_request_info,
                slate_id='123'
            )

            assert graphql_slate.id == '123'

            assert any(
                r.levelname == 'INFO' and 'resolving getSlate with slate_id=123' in r.message
                for r in caplog.records
            ), f'Expected log record not found in {caplog.records}'
