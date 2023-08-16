from typing import Dict

import pytest
from strawberry.types import Info


class DummyGraphQLInfo:
    def __init__(self, context: Dict) -> None:
        self.context = context


class DummyRequest:
    def __init__(self, headers: Dict) -> None:
        self.headers = headers


@pytest.fixture
def mock_graphql_request_info():
    return Info(DummyGraphQLInfo(context={'request': DummyRequest(headers={'user_id': 123})}), None)  # noqa
