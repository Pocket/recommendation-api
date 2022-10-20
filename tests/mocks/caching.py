import asyncio

import pytest

from aiocache import caches

from tests.functional.test_util.caching import reset_caches


@pytest.fixture
def aiocache_fixture():
    asyncio.run(reset_caches())
    return caches
