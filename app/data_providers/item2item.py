import logging
from typing import List

from qdrant_client.http import AsyncApis
from qdrant_client.http.exceptions import UnexpectedResponse
from qdrant_client.http.models import Filter, FieldCondition, MatchValue, RecommendRequest, ScrollRequest

import app.config
from app.models.corpus_item_model import CorpusItemModel


def _build_filter(is_curated: bool = None,
                  is_syndicated: bool = None,
                  domain: str = None) -> Filter:
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

    return Filter(must=conditions)


class Item2ItemRecommender:
    def __init__(self):
        host = app.config.qdrant["host"]
        port = app.config.qdrant["port"]
        https = app.config.qdrant["https"]
        self.collection = app.config.qdrant["collection"]
        self._client = AsyncApis(host=f"http{'s' if https else ''}://{host}:{port}").points_api

    async def by_publisher(self, resolved_id: int, domain: str, count: int) -> List[CorpusItemModel]:
        query_filter = _build_filter(
            is_curated=True,
            domain=domain)

        return await self._recommend(resolved_id, query_filter, count)

    async def syndicated(self, resolved_id: int, count: int) -> List[CorpusItemModel]:
        query_filter = _build_filter(
            is_curated=True,
            is_syndicated=True)

        return await self._recommend(resolved_id, query_filter, count)

    async def _recommend(self, resolved_id: int, query_filter: Filter, count: int):
        try:
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
            if ex.status_code == 404:
                # point or collection does not exist
                # it can happen when a new syndicated article was just added or qdrant state was reset by accident
                # fallback to returning random articles with the same filter
                # it should fail if the problem is not the article
                res = (await self._client.scroll_points(
                    collection_name=self.collection,
                    scroll_request=ScrollRequest(
                        limit=count,
                        filter=query_filter,
                        with_vector=False,
                        with_payload=True
                    ))).result.points
                logging.warning(f'Related: article is not found, fallback to Qdrant scroll method. '
                                f'resolved_id: {resolved_id}, filter: {query_filter}')
            else:
                raise

        return [CorpusItemModel(id=rec.payload['corpus_item_id'], topic=rec.payload['topic'])
                for rec in res]
