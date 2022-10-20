import datetime
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
    COLLECTION_ALIAS = "pocket"

    def __init__(self):
        host = app.config.qdrant["host"]
        port = app.config.qdrant["port"]
        https = app.config.qdrant["https"] == "true"
        self._client = AsyncApis(host=f"http{'s' if https else ''}://{host}:{port}").points_api

    async def by_publisher(self, resolved_id: str, domain_id: int, count: int) -> List[str]:
        query_filter = _build_filter(days_old=30,
                                     domain_id=domain_id)

        return await self._recommend(resolved_id, query_filter, count)

    async def syndicated(self, resolved_id: str, count: int) -> List[str]:
        query_filter = _build_filter(days_old=365,
                                     is_syndicated=True)

        return await self._recommend(resolved_id, query_filter, count)

    async def _recommend(self, resolved_id: str, query_filter: Filter, count: int):
        recommended = await self._client.points_api.recommend_points(
            collection_name=self.COLLECTION_ALIAS,
            recommend_request=RecommendRequest(
                positive=[resolved_id],
                limit=count,
                query_filter=query_filter,
                with_vector=False,
                with_payload=True
            )
        )
        return [rec.id for rec in recommended]
