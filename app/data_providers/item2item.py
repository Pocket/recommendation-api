import logging
from typing import List

from aiocache import cached
from aiocache.plugins import BasePlugin
from qdrant_client.http import AsyncApis
from qdrant_client.http.exceptions import UnexpectedResponse
from qdrant_client.http.models import Filter, FieldCondition, MatchValue, RecommendRequest, ScrollRequest, Range

import app.config
from app.models.corpus_item_model import CorpusItemModel


class Item2ItemError(Exception):
    pass


class QdrantError(Item2ItemError):
    pass


class ArticleNotFound(Item2ItemError):
    def __init__(self, resolved_id):
        super().__init__(self)
        self.resolved_id = resolved_id


def _log(level, msg, method, filter=None, resolved_id=None, code=None, reason=None):
    """ Standardize logging for application metrics based on log parsing """
    logging.log(level, f'Related: {msg}; '
                       f'method: {method}, ' +
                # make more readable, we use only must condition
                (f'filter: {[cond.key for cond in filter.must]}, ' if filter else '') +
                (f'resolved_id: {resolved_id}, ' if resolved_id else '') +
                (f'code: {code}, ' if code else '') +
                (f'reason: {reason}' if reason else ''))


class CacheLogPlugin(BasePlugin):
    def __init__(self, name):
        super().__init__()
        self.name = name

    async def post_get(self, *args, **kwargs):
        if kwargs['ret'] is not None:
            _log(logging.INFO, msg=f'got cached {self.name}', method='cache')


class Item2ItemRecommender:
    def __init__(self):
        host = app.config.qdrant["host"]
        port = app.config.qdrant["port"]
        https = app.config.qdrant["https"]
        self.collection = app.config.qdrant["collection"]
        self._client = AsyncApis(host=f"http{'s' if https else ''}://{host}:{port}").points_api

    async def by_publisher(self, resolved_id: int, domain: str, count: int) -> List[CorpusItemModel]:
        query_filter = self._build_filter(
            is_curated=True,
            domain=domain)
        return await self._recommend(resolved_id, query_filter, count)

    async def syndicated(self, resolved_id: int, count: int) -> List[CorpusItemModel]:
        query_filter = self._build_filter(
            is_curated=True,
            is_syndicated=True)
        return await self._recommend(resolved_id, query_filter, count)

    async def related(self, resolved_id: int, count: int) -> List[CorpusItemModel]:
        query_filter = self._build_filter(is_curated=True)
        return await self._recommend(resolved_id, query_filter, count)

    @cached(ttl=3600, plugins=[CacheLogPlugin('curated')])
    async def frequently_saved_curated(self, count: int) -> List[CorpusItemModel]:
        query_filter = self._build_filter(is_curated=True,
                                          save_count=1000)
        return await self._scroll(query_filter, count)

    @cached(ttl=3600, plugins=[CacheLogPlugin('syndicated')])
    async def frequently_saved_syndicated(self, count: int) -> List[CorpusItemModel]:
        query_filter = self._build_filter(is_curated=True,
                                          save_count=1000,
                                          is_syndicated=True)
        return await self._scroll(query_filter, count)

    @cached(ttl=3600, plugins=[CacheLogPlugin('publisher')])
    async def random_by_publisher(self, domain: str, count: int) -> List[CorpusItemModel]:
        query_filter = self._build_filter(is_curated=True,
                                          domain=domain)
        return await self._scroll(query_filter, count)

    @staticmethod
    def _build_filter(is_curated: bool = None,
                      is_syndicated: bool = None,
                      domain: str = None,
                      save_count: int = None) -> Filter:
        conditions = []

        if is_syndicated is not None:
            conditions.append(FieldCondition(
                key='is_syndicated',
                match=MatchValue(value=is_syndicated)
            ))
        if is_curated is not None:
            conditions.append(FieldCondition(
                key='is_curated',
                match=MatchValue(value=is_curated)
            ))
        if domain is not None:
            conditions.append(FieldCondition(
                key='domain',
                match=MatchValue(value=domain)
            ))
        if save_count is not None:
            conditions.append(FieldCondition(
                key='save_count',
                range=Range(gte=save_count)
            ))

        return Filter(must=conditions)

    async def _recommend(self, resolved_id: int, query_filter: Filter, count: int) -> List[CorpusItemModel]:
        try:
            _log(logging.INFO, 'request', 'recommend', filter=query_filter, resolved_id=resolved_id)
            res = (await self._client.recommend_points(
                collection_name=self.collection,
                recommend_request=RecommendRequest(
                    positive=[resolved_id],
                    negative=[],
                    limit=count,
                    filter=query_filter,
                    with_vector=False,
                    with_payload=True
                ))).result
        except UnexpectedResponse as ex:
            if ex.status_code == 404 and 'Not found: No point with id' in ex.content.decode():
                # article does not exist in qdrant
                # fallback to returning random popular articles with the same filter
                _log(logging.WARNING, 'article not found', 'recommend',
                     filter=query_filter, code=ex.status_code, reason=ex.reason_phrase, resolved_id=resolved_id)
                raise ArticleNotFound(resolved_id)
            else:
                _log(logging.ERROR, 'unexpected response', 'recommend', resolved_id=resolved_id,
                     filter=query_filter, code=ex.status_code, reason=ex.reason_phrase)
                raise QdrantError()

        return [CorpusItemModel(id=rec.payload['corpus_item_id'], topic=rec.payload['topic'])
                for rec in res]

    async def _scroll(self, query_filter: Filter, count: int) -> List[CorpusItemModel]:
        try:
            _log(logging.INFO, 'request', 'scroll', filter=query_filter)
            res = (await self._client.scroll_points(
                collection_name=self.collection,
                scroll_request=ScrollRequest(
                    limit=count,
                    filter=query_filter,
                    with_vector=False,
                    with_payload=True
                ))).result.points
        except UnexpectedResponse as ex:
            _log(logging.ERROR, 'unexpected response', 'scroll',
                 filter=query_filter, code=ex.status_code, reason=ex.reason_phrase)
            raise QdrantError()

        return [CorpusItemModel(id=rec.payload['corpus_item_id'], topic=rec.payload['topic'])
                for rec in res]
