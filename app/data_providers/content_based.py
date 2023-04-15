from typing import List, Dict

import numpy as np
from qdrant_client.http import AsyncApis, models
from qdrant_client.http.models import PointRequest, SearchRequestBatch, SearchRequest
from sklearn.cluster import KMeans
from datetime import datetime, timedelta

import app.config


class ContentBasedRecommender:
    def __init__(self):
        host = app.config.qdrant["host"]
        port = app.config.qdrant["port"]
        https = app.config.qdrant["https"]
        # recommendations corpus
        self.recs_collection = app.config.qdrant["collection"] + '_recs'
        # all available items for lookup
        self.all_collection = app.config.qdrant["collection"] + '_all'
        self._client = AsyncApis(host=f"http{'s' if https else ''}://{host}:{port}").points_api
        self.n_clusters = 5
        self.limit_per_centroid = 3
        self.freshness = timedelta(days=90)

    async def search(self, resolved_ids: List[int]):
        found_vectors = await self._retrieve_vectors(resolved_ids)

        if not found_vectors:
            return None

        vectors = np.array([vec for id, vec in found_vectors.items()])

        if len(found_vectors) <= self.n_clusters:
            centroids = vectors
        else:
            kmeans = KMeans(n_clusters=self.n_clusters, random_state=0, n_init="auto").fit(vectors)
            centroids = kmeans.cluster_centers_

        recs_batch = await self._search(centroids, resolved_ids, limit=5)

        return {r.payload['corpus_item_id'] for recs in recs_batch for r in recs}

    async def _retrieve_vectors(self, point_ids: List[int]) -> Dict[int, List[float]]:
        response = await self._client.get_points(self.all_collection,
                                           point_request=PointRequest(ids=point_ids,
                                                                      with_payload=False,
                                                                      with_vector=True))
        return {record.id: record.vector for record in response.result}

    async def _search(self, vectors: np.array,
                      exclude_ids: List[int],
                      limit: int) -> List[List[object]]:
        response = await self._client.search_batch_points(
            self.recs_collection,
            search_request_batch=SearchRequestBatch(searches=[self._search_request(vector, exclude_ids)
                                                       for vector in vectors]))
        return response.result

    def _search_request(self, vector, exclude_ids):
        return SearchRequest(vector=vector.tolist(),
                             limit=self.limit_per_centroid,
                             with_vector=False,
                             with_payload=True,
                             filter=models.Filter(
                                 must_not=[
                                     models.HasIdCondition(
                                         has_id=exclude_ids),
                                 ],
                                 must=[models.FieldCondition(
                                     key='timestamp',
                                     range=models.Range(
                                         gte=(datetime.utcnow() - self.freshness).timestamp())
                                 )]
                             ))
