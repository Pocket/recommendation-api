import asyncio

import pytest

from aiocache import caches

from tests.functional.test_util.caching import reset_caches, clear_function_caches


@pytest.fixture
def aiocache_fixture():
    asyncio.run(reset_caches())
    return caches


@pytest.fixture
def aiocache_functions_fixture():
    asyncio.run(clear_function_caches())
    return caches
