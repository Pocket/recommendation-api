from unittest.mock import MagicMock

import pytest

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession
from app.data_providers.unleash_provider import UnleashProvider, UnleashConfig
from tests.mocks.pocket_graph import get_pocket_graph_config


@pytest.fixture
def no_flags_unleash_provider() -> UnleashProvider:
    unleash_provider = MagicMock(UnleashProvider)
    unleash_provider.get_assignment.return_value = None
    return unleash_provider

@pytest.fixture
def pocket_home_v3_unleash_provider() -> UnleashProvider:
    unleash_provider = MagicMock(UnleashProvider)
    unleash_provider.get_assignment.return_value = None
    return unleash_provider