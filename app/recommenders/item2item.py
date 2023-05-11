import logging
from datetime import datetime, timedelta
from typing import List, NamedTuple

from aiocache import cached
from aiocache.plugins import BasePlugin
from qdrant_client.http import AsyncApis
from qdrant_client.http.exceptions import UnexpectedResponse
from qdrant_client.http.models import Filter, FieldCondition, MatchValue, RecommendRequest, ScrollRequest, Range, \
    HasIdCondition, LookupLocation

import app.config


class Item2ItemError(Exception):
    pass


class QdrantError(Item2ItemError):
    pass


class UnsupportedLanguage(Item2ItemError):
    def __init__(self, lang):
        super().__init__(self)
        self.lang = lang


class ArticleNotFound(Item2ItemError):
    def __init__(self, resolved_id):
        super().__init__(self)
        self.resolved_id = resolved_id


def _log(level, msg, method, filter=None, resolved_id=None, code=None, reason=None, lang=None):
    """ Standardize logging for application metrics based on log parsing """
    logging.log(level, f'Related: {msg}; '
                       f'method: {method}, ' +
                # make more readable, we use only must condition
                (f'filter: {[cond.key for cond in filter.must]}, ' if filter else '') +
                (f'resolved_id: {resolved_id}, ' if resolved_id else '') +
                (f'code: {code}, ' if code else '') +
                (f'reason: {reason}' if reason else '') +
                (f'lang: {lang}' if lang else ''))


class CacheLogPlugin(BasePlugin):
    def __init__(self, name):
        super().__init__()
        self.name = name

    async def post_get(self, *args, **kwargs):
        if kwargs['ret'] is not None:
            _log(logging.INFO, msg=f'got cached {self.name}', method='cache')


class RelatedItem(NamedTuple):
    corpus_item_id: str
    domain: str
    topic: str = None


class Item2ItemRecommender:
    # article freshness in days for non-syndicated recs
    FRESHNESS = 90
    # minimum save count for fallback scroll request
    MIN_SAVE_COUNT = 1000

    def __init__(self):
        host = app.config.qdrant["host"]
        port = app.config.qdrant["port"]
        https = app.config.qdrant["https"]
        # recommendations corpus
        self.recs_collection = app.config.qdrant["collection"] + '_recs'
        # all available items for lookup
        self.all_collection = app.config.qdrant["collection"] + '_all'
        self._client = AsyncApis(host=f"http{'s' if https else ''}://{host}:{port}").points_api

    @cached(ttl=3600, plugins=[CacheLogPlugin('related_publisher')])
    async def by_publisher(self,
                           resolved_id: int,
                           domain: str,
                           original_id: int,
                           count: int) -> List[RelatedItem]:
        query_filter = self._build_filter(
            is_curated=True,
            is_syndicated=False,
            domain=domain,
            exclude_id=original_id)
        return await self._recommend(resolved_id, query_filter, count)

    @cached(ttl=3600, plugins=[CacheLogPlugin('related_syndicated')])
    async def syndicated(self, resolved_id: int, count: int) -> List[RelatedItem]:
        query_filter = self._build_filter(
            is_curated=True,
            is_syndicated=True)
        return await self._recommend(resolved_id, query_filter, count)

    async def related(self, resolved_id: int, count: int, lang: str) -> List[RelatedItem]:
        query_filter = self._build_filter(is_curated=True, freshness_days=self.FRESHNESS)
        return await self._recommend(resolved_id, query_filter, count, lang)

    @cached(ttl=3600, plugins=[CacheLogPlugin('saved_curated')])
    async def frequently_saved_curated(self, count: int) -> List[RelatedItem]:
        query_filter = self._build_filter(is_curated=True,
                                          save_count=self.MIN_SAVE_COUNT,
                                          freshness_days=self.FRESHNESS)
        return await self._scroll(query_filter, count)

    @cached(ttl=3600, plugins=[CacheLogPlugin('saved_syndicated')])
    async def frequently_saved_syndicated(self, count: int) -> List[RelatedItem]:
        query_filter = self._build_filter(is_curated=True,
                                          save_count=self.MIN_SAVE_COUNT,
                                          is_syndicated=True)
        return await self._scroll(query_filter, count)

    @cached(ttl=3600, plugins=[CacheLogPlugin('random_publisher')])
    async def random_by_publisher(self, domain: str, count: int) -> List[RelatedItem]:
        query_filter = self._build_filter(is_curated=True,
                                          domain=domain)
        return await self._scroll(query_filter, count)

    @staticmethod
    def _build_filter(is_curated: bool = None,
                      is_syndicated: bool = None,
                      domain: str = None,
                      save_count: int = None,
                      exclude_id: int = None,
                      freshness_days: int = None
                      ) -> Filter:
        must = []
        must_not = []

        if is_syndicated is not None:
            must.append(FieldCondition(
                key='is_syndicated',
                match=MatchValue(value=is_syndicated)
            ))
        if is_curated is not None:
            must.append(FieldCondition(
                key='is_curated',
                match=MatchValue(value=is_curated)
            ))
        if domain is not None:
            must.append(FieldCondition(
                key='domain',
                match=MatchValue(value=domain)
            ))
        if save_count is not None:
            must.append(FieldCondition(
                key='save_count',
                range=Range(gte=save_count)
            ))
        if freshness_days is not None:
            must.append(FieldCondition(
                key='timestamp',
                range=Range(gte=(datetime.now() - timedelta(days=freshness_days)).timestamp())
            ))
        if exclude_id is not None:
            must_not.append(HasIdCondition(has_id=[exclude_id]))

        return Filter(must=must, must_not=must_not if must_not else None)

    async def _recommend(self,
                         resolved_id: int,
                         query_filter: Filter,
                         count: int,
                         lang: str = 'en') -> List[RelatedItem]:
        _log(logging.INFO, 'request', 'recommend', filter=query_filter,
             resolved_id=resolved_id, lang=lang)

        if lang != 'en':
            _log(logging.WARNING, 'unsupported language', 'recommend',
                 filter=query_filter, resolved_id=resolved_id, lang=lang)
            raise UnsupportedLanguage(lang)

        try:
            res = (await self._client.recommend_points(
                collection_name=self.recs_collection,
                recommend_request=RecommendRequest(
                    positive=[resolved_id],
                    negative=[],
                    limit=count,
                    filter=query_filter,
                    with_vector=False,
                    with_payload=True,
                    lookup_from=LookupLocation(collection=self.all_collection)
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
        except Exception as ex:
            _log(logging.ERROR, 'Qdrant error', 'recommend', resolved_id=resolved_id,
                 filter=query_filter, reason=str(ex))
            raise QdrantError()

        return self._convert_response(res)

    async def _scroll(self, query_filter: Filter, count: int) -> List[RelatedItem]:
        try:
            _log(logging.INFO, 'request', 'scroll', filter=query_filter)
            res = (await self._client.scroll_points(
                collection_name=self.recs_collection,
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
        except Exception as ex:
            _log(logging.ERROR, 'Qdrant error', 'scroll',
                 filter=query_filter, reason=str(ex))
            raise QdrantError()

        return self._convert_response(res)

    @staticmethod
    def _convert_response(res):
        logging.debug(f'Related: {res}')
        return [RelatedItem(corpus_item_id=rec.payload['corpus_item_id'],
                            domain=rec.payload['domain'])
                for rec in res]
