import aiomcache
from aiocache import caches

from app.cache import initialize_caches, candidate_set_alias, metrics_alias
from app import config
from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.topic_provider import TopicProvider


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


async def clear_function_caches():
    """
    Clears aioboto3 function caches
    :return:
    """
    cached_functions = [
        TopicProvider._scan_table,
        CorpusFeatureGroupClient._query_corpus_items,
    ]

    for f in cached_functions:
        # The cache is available in the function object as ``<function_name>.cache``.
        await f.cache.clear()


async def reset_caches():
    await clear_memcache()
    await clear_function_caches()
    delete_caches()
    initialize_caches()
