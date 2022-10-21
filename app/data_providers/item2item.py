import datetime
import logging
from typing import List

from qdrant_client.http import AsyncApis
from qdrant_client.http.models import Filter, FieldCondition, Range, MatchValue, RecommendRequest

import app.config


def _build_filter(days_old: int,
                  is_curated: bool = None,
                  is_syndicated: bool = None,
                  domain_id: int = None) -> Filter:
    timestamp = (datetime.datetime.now() - datetime.timedelta(days=days_old)).timestamp()
    conditions = [
        FieldCondition(
            key='timestamp',
            range=Range(
                gte=timestamp
            )
        )]
    if is_syndicated is not None:
        conditions.append(FieldCondition(
            key='is_syndicated',
            match=MatchValue(value=is_syndicated)
        ))
    if is_curated is not None:
        conditions.append(FieldCondition(
            key='is_curated',
            match=MatchValue(value=is_syndicated)
        ))
    if domain_id is not None:
        conditions.append(FieldCondition(
            key='domain_id',
            match=MatchValue(value=domain_id)
        ))
    return Filter(must=conditions)


class Item2ItemRecommender:
    def __init__(self):
        host = app.config.qdrant["host"]
        port = app.config.qdrant["port"]
        https = app.config.qdrant["https"]
        self.collection = app.config.qdrant["collection"]
        self._client = AsyncApis(host=f"http{'s' if https else ''}://{host}:{port}").points_api

    async def by_publisher(self, resolved_id: int, domain_id: int, count: int) -> List[int]:
        query_filter = _build_filter(days_old=30,
                                     domain_id=domain_id)

        return await self._recommend(resolved_id, query_filter, count)

    async def syndicated(self, resolved_id: int, count: int) -> List[int]:
        query_filter = _build_filter(days_old=365,
                                     is_syndicated=True)

        return await self._recommend(resolved_id, query_filter, count)

    async def _recommend(self, resolved_id: int, query_filter: Filter, count: int):
        # todo: logging doesn't log
        print(f'Item2items recs: filter {query_filter}')
        recommended = await self._client.recommend_points(
            collection_name=self.collection,
            recommend_request=RecommendRequest(
                positive=[resolved_id],
                negative=[],
                limit=count,
                query_filter=query_filter,
                with_vector=False,
                with_payload=True
            )
        )
        print(f'Item2items recs: {[r.payload["title"] for r in recommended.result]}')
        return [rec.id for rec in recommended.result]
