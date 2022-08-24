import asyncio

import pytest

import aiomcache
from aiocache import caches

from app.cache import initialize_caches, candidate_set_alias, metrics_alias
from app import config


def delete_caches():
    """
    Deletes the aiocache caches used by our app.
    """
    for alias in (candidate_set_alias, metrics_alias):
        # aiocache doesn't support deleting caches, and maintains a global object `aiocache.caches`.
        # If we don't delete caches, then an error is raised "attached to a different loop", because test cases do not
        # all share the same event loop with which `aiocache.caches` was created.
        if alias in caches._caches:
            del caches._caches[alias]


async def clear_memcache():
    """
    Deletes all keys in memcache
    :return:
    """
    for server in config.elasticache['servers']:
        endpoint, port = server.split(':')
        client = aiomcache.Client(endpoint, port)
        await client.flush_all()


async def reset_caches():
    await clear_memcache()
    delete_caches()
    initialize_caches()


@pytest.fixture
def aiocache_fixture():
    asyncio.run(reset_caches())
    return caches
