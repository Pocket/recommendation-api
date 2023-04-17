import logging
from typing import List, Optional

from app.data_providers.PocketGraphClientSession import PocketGraphClientSession
from app.models.request_user import RequestUser


class UserSavesProvider:

    def __init__(self, pocket_graph_client_session: PocketGraphClientSession):
        self.pocket_graph_client_session = pocket_graph_client_session

    async def get_saves(self, user: RequestUser) -> Optional[List[int]]:
        query = """
            query SavedItems($filter: SavedItemsFilter, $sort: SavedItemsSort, pagination: $pagination) {
              user {
                savedItems(filter: $filter, sort: $sort) {
                  edges {
                    node {
                      id
                  }
                  totalCount
                }
              }
            }
            """

        #TODO: how to authenticate?
        body = {
            'query': query,
            'variables': {
                "filter": {
                    "contentType": "IS_READABLE"
                },
                "sort": {
                    "sortBy": "CREATED_AT",
                    "sortOrder": "DESC"
                },
                "pagination": {
                    "first": 100
                }
            }
        }

        async with self.pocket_graph_client_session.post(url='/', json=body, raise_for_status=True) as resp:
            try:
                response_json = await resp.json()
                saves = [int(edge['node']['id']) for edge in response_json['data']['user']['savedItems']['edges']]
                return saves
            except Exception as ex:
                logging.error(f'Error while loading user saves: {ex}')
                return None


