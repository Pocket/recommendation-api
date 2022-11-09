import json
import os
from time import sleep
from unittest import TestCase

from fastapi.testclient import TestClient

from app import config
from app.config import ROOT_DIR
from app.main import app

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance


def populate_qdrant():
    with open(os.path.join(ROOT_DIR, 'tests/assets/json/qdrant_test_data.json')) as fp:
        test_data = json.load(fp)

        print(f"Populating Qdrant {config.qdrant['host']}, collection {config.qdrant['collection']} with test data")
        assert config.qdrant['host'] != 'qdrant.readitlater.com'
        assert config.qdrant['collection'] != 'articlesprod'

        client = QdrantClient(host=config.qdrant['host'],
                              port=config.qdrant['port'],
                              prefer_grpc=False,
                              https=config.qdrant['https'])
        points = [PointStruct(id=d['id'], vector=d['vector'], payload=d['payload']) for d in test_data]
        client.recreate_collection(
            collection_name=config.qdrant['collection'],
            vectors_config=VectorParams(size=160, distance=Distance.DOT))
        client.upsert(collection_name=config.qdrant['collection'], points=points)
        sleep(5)
        assert client.count(config.qdrant['collection']).count == len(test_data)
        return test_data


class TestGraphQLRelated(TestCase):
    @classmethod
    def setUpClass(cls):
        populate_qdrant()

    def test_related_end_of_article_basic(self):
        item_id = '3727511744'
        pub_url = 'https://time.com/6223012/workplaces-of-the-future/'

        with TestClient(app) as client:
            response = client.post("/", json={
                    'query': '''
                        query ($representations: [_Any!]!) {
                          _entities(representations: $representations) {
                            ... on SyndicatedArticle {
                                itemId
                                publisherUrl
                                relatedEndOfArticle(count: 3) {
                                    id
                                    corpusItem {
                                      id
                                    }
                                }
                            }
                          }
                        }
                    ''',
                    'variables': {
                        'representations': [
                            {
                                '__typename': 'SyndicatedArticle',
                                'itemId': item_id,
                                'publisherUrl': pub_url,
                            },
                        ],
                    },
                }).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedEndOfArticle']
            assert entity['itemId'] == item_id
            assert entity['publisherUrl'] == pub_url
            assert len(recs) == 3
            assert 'id' in recs[0]
            assert 'corpusItem' in recs[0]
            assert 'id' in recs[0]['corpusItem']
            assert {r['corpusItem']['id'] for r in recs} == {'22bfe98b-857d-4c98-aae2-9e750d0eaa9d',
                                                             '66b86a8e-b3f6-45b5-a06d-82d24f4d5c40',
                                                             'ec0421ff-e2db-4496-8d64-a675c5824bf7'}

    def test_related_right_rail_basic(self):
        item_id = '3727501830'
        pub_url = 'https://psyche.co/ideas/are-successful-authors-creative-geniuses-or-literary-labourers'

        with TestClient(app) as client:
            response = client.post("/", json={
                'query': '''
                        query ($representations: [_Any!]!) {
                          _entities(representations: $representations) {
                            ... on SyndicatedArticle {
                                itemId
                                publisherUrl
                                relatedRightRail(count: 3) {
                                    id
                                    corpusItem {
                                      id
                                    }
                                }
                            }
                          }
                        }
                    ''',
                    'variables': {
                        'representations': [
                            {
                                '__typename': 'SyndicatedArticle',
                                'itemId': item_id,
                                'publisherUrl': pub_url,
                            },
                        ],
                    },
                }).json()


            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedRightRail']
            assert entity['itemId'] == item_id
            assert entity['publisherUrl'] == pub_url
            assert len(recs) == 3
            assert 'id' in recs[0]
            assert 'corpusItem' in recs[0]
            assert 'id' in recs[0]['corpusItem']
            assert {r['corpusItem']['id'] for r in recs} == {"253c3f1e-00c3-4ec2-a03a-3e046ab16652",
                                                             "3edd22f6-0967-4eda-af23-d06d7cfea722",
                                                             "b4cbf203-50cd-45fc-97c8-e1fddac2f270"}

    def test_related_end_of_article_article_doesnt_exist(self):
        with TestClient(app) as client:
            response = client.post("/", json={
                    'query': '''
                        query ($representations: [_Any!]!) {
                          _entities(representations: $representations) {
                            ... on SyndicatedArticle {
                                itemId
                                publisherUrl
                                relatedEndOfArticle(count: 3) {
                                    id
                                    corpusItem {
                                      id
                                    }
                                }
                            }
                          }
                        }
                    ''',
                    'variables': {
                        'representations': [
                            {
                                '__typename': 'SyndicatedArticle',
                                'itemId': "11111",
                                'publisherUrl': "xxxxx",
                            },
                        ],
                    },
                }).json()

            assert not response.get('errors')
            recs = response['data']['_entities'][0]['relatedEndOfArticle']
            assert len(recs) == 0

    def test_related_right_rail_article_doesnt_exist(self):
        with TestClient(app) as client:
            response = client.post("/", json={
                'query': '''
                        query ($representations: [_Any!]!) {
                          _entities(representations: $representations) {
                            ... on SyndicatedArticle {
                                itemId
                                publisherUrl
                                relatedRightRail(count: 3) {
                                    id
                                    corpusItem {
                                      id
                                    }
                                }
                            }
                          }
                        }
                    ''',
                    'variables': {
                        'representations': [
                            {
                                '__typename': 'SyndicatedArticle',
                                'itemId': "111111",
                                'publisherUrl': "xxxx",
                            },
                        ],
                    },
                }).json()

            assert not response.get('errors')
            recs = response['data']['_entities'][0]['relatedRightRail']
            assert len(recs) == 0
