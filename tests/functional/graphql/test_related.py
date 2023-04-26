import json
import logging
import os
from time import sleep
from unittest import TestCase, mock
from unittest.mock import patch
import re
from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient
from qdrant_client.http.api.points_api import AsyncPointsApi
from qdrant_client.http.exceptions import UnexpectedResponse

from app import config
from app.config import ROOT_DIR
from app.data_providers.item2item import Item2ItemRecommender
from app.main import app

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance


def populate_qdrant():
    with open(os.path.join(ROOT_DIR, 'tests/assets/json/qdrant_test_data.json')) as fp:
        test_data = json.load(fp)
        for p in test_data[2:]:
            p['payload']['timestamp'] = \
                (datetime.now() - timedelta(days=Item2ItemRecommender.FRESHNESS - 5)).timestamp()
        for p in test_data[:2]:
            p['payload']['timestamp'] = \
                (datetime.now() - timedelta(days=Item2ItemRecommender.FRESHNESS + 5)).timestamp()

        print(f"Populating Qdrant {config.qdrant['host']}, collection {config.qdrant['collection']} with test data")
        assert config.qdrant['host'] != 'qdrant.readitlater.com'
        assert 'articlesprod' not in config.qdrant['collection']

        client = QdrantClient(host=config.qdrant['host'],
                              port=config.qdrant['port'],
                              prefer_grpc=False,
                              https=config.qdrant['https'])

        points = [PointStruct(id=d['id'], vector=d['vector'], payload=d['payload']) for d in test_data]
        collection = config.qdrant['collection'] + '_recs'
        client.recreate_collection(
            collection_name=collection,
            vectors_config=VectorParams(size=160, distance=Distance.DOT))
        client.upsert(collection_name=collection, points=points)
        sleep(5)
        assert client.count(collection).count == len(test_data)

        points = [PointStruct(id=d['id'], vector=d['vector'], payload=None) for d in test_data]
        collection = config.qdrant['collection'] + '_all'
        client.recreate_collection(
            collection_name=collection,
            vectors_config=VectorParams(size=160, distance=Distance.DOT))
        client.upsert(collection_name=collection, points=points)
        sleep(5)
        assert client.count(collection).count == len(test_data)

        return test_data


def syndicated_json(item_id: str, pub_url: str, original_id: str = '222'):
    return {
        'query': '''
            query ($representations: [_Any!]!) {
              _entities(representations: $representations) {
                ... on SyndicatedArticle {
                    itemId
                    publisherUrl
                    originalItemId
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
                    'originalItemId': original_id
                },
            ],
        },
    }


def publisher_json(item_id: str, pub_url: str, original_id: str = '222'):
    return {
        'query': '''
            query ($representations: [_Any!]!) {
              _entities(representations: $representations) {
                ... on SyndicatedArticle {
                    itemId
                    publisherUrl
                    originalItemId
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
                    'originalItemId': original_id
                },
            ],
        },
    }


def after_article_json(item_id: str, lang='en'):
    return {
        'query': '''
            query ($representations: [_Any!]!) {
              _entities(representations: $representations) {
                ... on Item {
                    itemId
                    relatedAfterArticle(count: 3) {
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
                    '__typename': 'Item',
                    'itemId': item_id,
                    'language': lang
                },
            ],
        },
    }


def after_save_json(item_id: str, lang='en'):
    return {
        'query': '''
            query ($representations: [_Any!]!) {
              _entities(representations: $representations) {
                ... on Item {
                    itemId
                    relatedAfterCreate(count: 3) {
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
                    '__typename': 'Item',
                    'itemId': item_id,
                    'language': lang
                },
            ],
        },
    }


qdrant_error_mock = mock.Mock()
qdrant_error_mock.side_effect = UnexpectedResponse(500, 'error', None, None)
qdrant_unexpected_error_mock = mock.Mock()
qdrant_unexpected_error_mock.side_effect = ValueError('something went wrong')
log_pattern = re.compile(
    'Related: [\w ]+; method: \w+,( filter: [\'\[\] \w,]+,)?( resolved_id: \d+,)?( code: \d+,)?( reason: [\w ]+,)?( lang: \w+)?')


class TestGraphQLRelated(TestCase):
    @classmethod
    def setUpClass(cls):
        test_data = populate_qdrant()
        cls.art_by_corpus_id = {}
        for d in test_data:
            d['payload']['resolved_id'] = d['id']
            cls.art_by_corpus_id[d['payload']['corpus_item_id']] = d['payload']

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog):
        self.caplog = caplog

    def verify_logs(self, level: int, resolved_id=None, msg=None, method=None, lang=None):
        related_logs = [rec for rec in self.caplog.records if 'Related:' in rec.message and level == rec.levelno]
        assert related_logs
        for rec in related_logs:
            assert re.search(log_pattern, rec.msg)

        last_rec = related_logs[-1].message
        if resolved_id:
            assert str(resolved_id) in last_rec
        if msg:
            assert msg in last_rec
        if method:
            assert f'method: {method}' in last_rec
        if lang:
            assert lang in last_rec

    def test_related_after_save_basic(self):
        """ recommend similar curated """
        item_id = '3727699409'

        with TestClient(app) as client:
            response = client.post("/", json=after_save_json(item_id)).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedAfterCreate']
            assert entity['itemId'] == item_id
            assert len(recs) == 3
            assert 'id' in recs[0]
            assert 'corpusItem' in recs[0]
            assert 'id' in recs[0]['corpusItem']
            assert all(self.art_by_corpus_id[r['corpusItem']['id']]['is_curated'] for r in recs)
            assert all((datetime.now() - datetime.fromtimestamp
                    (self.art_by_corpus_id[r['corpusItem']['id']]['timestamp'])).days < Item2ItemRecommender.FRESHNESS
                       for r in recs)
            self.verify_logs(logging.INFO, item_id)

    def test_related_after_article(self):
        """ recommend similar curated """
        item_id = '3727699409'

        with TestClient(app) as client:
            response = client.post("/", json=after_article_json(item_id)).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedAfterArticle']
            assert entity['itemId'] == item_id
            assert len(recs) == 3
            assert 'id' in recs[0]
            assert 'corpusItem' in recs[0]
            assert 'id' in recs[0]['corpusItem']
            assert all(self.art_by_corpus_id[r['corpusItem']['id']]['is_curated'] for r in recs)
            assert all((datetime.now() - datetime.fromtimestamp
                    (self.art_by_corpus_id[r['corpusItem']['id']]['timestamp'])).days < Item2ItemRecommender.FRESHNESS
                       for r in recs)
            assert len(set(self.art_by_corpus_id[r['corpusItem']['id']]['domain'] for r in recs)) == 3
            self.verify_logs(logging.INFO, item_id)

    def test_related_end_of_syndicated_basic(self):
        """ recommend similar syndicated """
        item_id = '3727511744'
        pub_url = 'https://time.com/6223012/workplaces-of-the-future/'
        original_id = '2345678'

        with TestClient(app) as client:
            response = client.post("/", json=syndicated_json(item_id, pub_url, original_id)).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedEndOfArticle']
            assert entity['itemId'] == item_id
            assert entity['publisherUrl'] == pub_url
            assert len(recs) == 3
            assert 'id' in recs[0]
            assert 'corpusItem' in recs[0]
            assert 'id' in recs[0]['corpusItem']
            assert all(self.art_by_corpus_id[r['corpusItem']['id']]['is_syndicated'] for r in recs)
            assert len(set(self.art_by_corpus_id[r['corpusItem']['id']]['domain'] for r in recs)) == 3
            self.verify_logs(logging.INFO, item_id)

    def test_related_right_rail_basic(self):
        """ recommend similar curated from the same publisher """
        item_id = '3727501830'
        # make sure www is ignored
        pub_url = 'https://www.psyche.co/ideas/are-successful-authors-creative-geniuses-or-literary-labourers'
        original_id = '2345678'

        with TestClient(app) as client:
            response = client.post("/", json=publisher_json(item_id, pub_url, original_id)).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedRightRail']
            assert entity['itemId'] == item_id
            assert entity['publisherUrl'] == pub_url
            assert len(recs) == 3
            assert 'id' in recs[0]
            assert 'corpusItem' in recs[0]
            assert 'id' in recs[0]['corpusItem']
            assert all(self.art_by_corpus_id[r['corpusItem']['id']]['domain'] == 'psyche.co' for r in recs)
            assert all(self.art_by_corpus_id[r['corpusItem']['id']]['is_curated'] for r in recs)
            assert all(not self.art_by_corpus_id[r['corpusItem']['id']]['is_syndicated'] for r in recs)
            # filter original article
            assert all(self.art_by_corpus_id[r['corpusItem']['id']]['resolved_id'] != 2345678 for r in recs)
            self.verify_logs(logging.INFO, item_id)

    def test_related_syndicated_article_doesnt_exist(self):
        """ fallback to random frequently saved syndicated """
        item_id = '11111'
        pub_url = 'xxxx'

        with TestClient(app) as client:
            response = client.post("/", json=syndicated_json(item_id, pub_url)).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedEndOfArticle']
            assert entity['itemId'] == item_id
            assert entity['publisherUrl'] == pub_url
            assert len(recs) == 3
            assert 'id' in recs[0]
            assert 'corpusItem' in recs[0]
            assert 'id' in recs[0]['corpusItem']
            assert all(self.art_by_corpus_id[r['corpusItem']['id']]['is_syndicated'] for r in recs)
            assert all(self.art_by_corpus_id[r['corpusItem']['id']]['save_count'] > Item2ItemRecommender.MIN_SAVE_COUNT
                       for r in recs)
            assert len(set(self.art_by_corpus_id[r['corpusItem']['id']]['domain'] for r in recs)) == 3
            self.verify_logs(logging.WARNING, item_id, msg='article not found')
            self.verify_logs(logging.INFO, msg='scroll')

    def test_related_right_rail_article_doesnt_exist(self):
        """ fallback to random from the same publisher """
        item_id = '11111'
        pub_url = 'https://psyche.co/ideas/are-successful-authors-creative-geniuses-or-literary-labourers'

        with TestClient(app) as client:
            response = client.post("/", json=publisher_json(item_id, pub_url)).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedRightRail']
            assert entity['itemId'] == item_id
            assert entity['publisherUrl'] == pub_url
            assert len(recs) == 3
            assert 'id' in recs[0]
            assert 'corpusItem' in recs[0]
            assert 'id' in recs[0]['corpusItem']
            assert all(self.art_by_corpus_id[r['corpusItem']['id']]['domain'] == 'psyche.co' for r in recs)
            self.verify_logs(logging.WARNING, item_id, msg='article not found')
            self.verify_logs(logging.INFO, msg='scroll')

    def test_related_right_rail_publisher_doesnt_exist(self):
        """ do not fallback, having the same publisher is a hard requirement """
        item_id = '3727501830'
        pub_url = 'https://xxx.co/ideas/'

        with TestClient(app) as client:
            response = client.post("/", json=publisher_json(item_id, pub_url)).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedRightRail']
            assert entity['itemId'] == item_id
            assert entity['publisherUrl'] == pub_url
            assert len(recs) == 0
            self.verify_logs(logging.INFO, item_id)

    def test_related_right_rail_article_and_publisher_dont_exist(self):
        """ do not fallback, having the same publisher is a hard requirement """
        item_id = '11111'
        pub_url = 'https://xxx.co/ideas/'

        with TestClient(app) as client:
            response = client.post("/", json=publisher_json(item_id, pub_url)).json()

            assert not response.get('errors')
            recs = response['data']['_entities'][0]['relatedRightRail']
            assert len(recs) == 0
            self.verify_logs(logging.WARNING, item_id, msg='article not found')
            self.verify_logs(logging.INFO, msg='scroll')

    def test_related_after_article_article_doesnt_exist(self):
        """ fallback to random frequently saved curated """
        item_id = '11111'

        with TestClient(app) as client:
            response = client.post("/", json=after_article_json(item_id)).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedAfterArticle']
            assert entity['itemId'] == item_id
            assert len(recs) == 3
            assert 'id' in recs[0]
            assert 'corpusItem' in recs[0]
            assert 'id' in recs[0]['corpusItem']
            assert all(self.art_by_corpus_id[r['corpusItem']['id']]['is_curated'] for r in recs)
            assert all(self.art_by_corpus_id[r['corpusItem']['id']]['save_count'] > Item2ItemRecommender.MIN_SAVE_COUNT
                       for r in recs)
            assert all((datetime.now() - datetime.fromtimestamp
                    (self.art_by_corpus_id[r['corpusItem']['id']]['timestamp'])).days < Item2ItemRecommender.FRESHNESS
                       for r in recs)
            assert len(set(self.art_by_corpus_id[r['corpusItem']['id']]['domain'] for r in recs)) == 3
            self.verify_logs(logging.WARNING, item_id, msg='article not found')
            self.verify_logs(logging.INFO, msg='scroll')

    def test_related_after_save_article_doesnt_exist(self):
        """ do not fallback """
        item_id = '11111'

        with TestClient(app) as client:
            response = client.post("/", json=after_save_json(item_id)).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedAfterCreate']
            assert entity['itemId'] == item_id
            assert len(recs) == 0
            self.verify_logs(logging.WARNING, item_id, msg='article not found')
            self.verify_logs(logging.INFO, item_id, msg='recommend')

    def test_related_after_save_lang_not_supported(self):
        """ do not fallback """
        item_id = '11111'
        lang = 'de'

        with TestClient(app) as client:
            response = client.post("/", json=after_save_json(item_id, lang=lang)).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedAfterCreate']
            assert entity['itemId'] == item_id
            assert len(recs) == 0
            self.verify_logs(logging.WARNING, item_id, lang=lang, msg='unsupported language')
            self.verify_logs(logging.INFO, item_id, lang=lang, msg='recommend')

    def test_related_after_article_lang_not_supported(self):
        """ do not fallback """
        item_id = '11111'
        lang = 'de'

        with TestClient(app) as client:
            response = client.post("/", json=after_article_json(item_id, lang=lang)).json()

            assert not response.get('errors')
            entity = response['data']['_entities'][0]
            recs = entity['relatedAfterArticle']
            assert entity['itemId'] == item_id
            assert len(recs) == 0
            self.verify_logs(logging.WARNING, item_id, lang=lang, msg='unsupported language')
            self.verify_logs(logging.INFO, item_id, lang=lang, msg='recommend')

    @patch.object(AsyncPointsApi, 'recommend_points', qdrant_error_mock)
    @patch.object(AsyncPointsApi, 'scroll_points', qdrant_error_mock)
    def test_related_after_save_qdrant_outage(self):
        item_id = '3727501830'

        with TestClient(app) as client:
            response = client.post("/", json=after_save_json(item_id)).json()

            assert not response.get('errors')
            assert len(response['data']['_entities'][0]['relatedAfterCreate']) == 0
            self.verify_logs(logging.ERROR, msg='unexpected response')

    @patch.object(AsyncPointsApi, 'recommend_points', qdrant_unexpected_error_mock)
    @patch.object(AsyncPointsApi, 'scroll_points', qdrant_unexpected_error_mock)
    def test_related_after_article_qdrant_outage(self):
        item_id = '3727699409'

        with TestClient(app) as client:
            response = client.post("/", json=after_article_json(item_id)).json()

            assert not response.get('errors')
            assert len(response['data']['_entities'][0]['relatedAfterArticle']) == 0
            self.verify_logs(logging.ERROR, msg='Qdrant error')

    @patch.object(AsyncPointsApi, 'recommend_points', qdrant_error_mock)
    @patch.object(AsyncPointsApi, 'scroll_points', qdrant_error_mock)
    def test_related_end_of_syndicated_qdrant_outage(self):
        item_id = '3727511744'
        pub_url = 'https://time.com/6223012/workplaces-of-the-future/'

        with TestClient(app) as client:
            response = client.post("/", json=syndicated_json(item_id, pub_url)).json()

            assert not response.get('errors')
            assert len(response['data']['_entities'][0]['relatedEndOfArticle']) == 0
            self.verify_logs(logging.ERROR, msg='unexpected response')

    @patch.object(AsyncPointsApi, 'recommend_points', qdrant_error_mock)
    @patch.object(AsyncPointsApi, 'scroll_points', qdrant_error_mock)
    def test_related_right_rail_qdrant_outage(self):
        item_id = '3727501830'
        pub_url = 'https://psyche.co/ideas/are-successful-authors-creative-geniuses-or-literary-labourers'

        with TestClient(app) as client:
            response = client.post("/", json=publisher_json(item_id, pub_url)).json()

            assert not response.get('errors')
            assert len(response['data']['_entities'][0]['relatedRightRail']) == 0
            self.verify_logs(logging.ERROR, msg='unexpected response')

    @patch.object(AsyncPointsApi, 'recommend_points', qdrant_error_mock)
    def test_related_after_article_fallback_cached(self):
        item_id = '3727699409'

        with TestClient(app) as client:
            response = client.post("/", json=after_article_json(item_id)).json()

            assert not response.get('errors')
            assert len(response['data']['_entities'][0]['relatedAfterArticle']) == 3
            self.verify_logs(logging.INFO, method='scroll')

            with patch.object(AsyncPointsApi, 'scroll_points', qdrant_error_mock):
                response = client.post("/", json=after_article_json(item_id)).json()

            assert not response.get('errors')
            assert len(response['data']['_entities'][0]['relatedAfterArticle']) == 3
            self.verify_logs(logging.INFO, method='cache', msg='curated')

    @patch.object(AsyncPointsApi, 'recommend_points', qdrant_error_mock)
    def test_related_end_of_syndicated_fallback_cached(self):
        item_id = '3727511744'
        pub_url = 'https://time.com/6223012/workplaces-of-the-future/'

        with TestClient(app) as client:
            response = client.post("/", json=syndicated_json(item_id, pub_url)).json()

            assert not response.get('errors')
            assert len(response['data']['_entities'][0]['relatedEndOfArticle']) == 3
            self.verify_logs(logging.INFO, msg='scroll')

            with patch.object(AsyncPointsApi, 'scroll_points', qdrant_error_mock):
                response = client.post("/", json=syndicated_json(item_id, pub_url)).json()

            assert not response.get('errors')
            assert len(response['data']['_entities'][0]['relatedEndOfArticle']) == 3
            self.verify_logs(logging.INFO, method='cache', msg='syndicated')

    @patch.object(AsyncPointsApi, 'recommend_points', qdrant_error_mock)
    def test_related_right_rail_fallback_cached(self):
        item_id = '3727501830'
        pub_url = 'https://psyche.co/ideas/are-successful-authors-creative-geniuses-or-literary-labourers'

        with TestClient(app) as client:
            response = client.post("/", json=publisher_json(item_id, pub_url)).json()

            assert not response.get('errors')
            assert len(response['data']['_entities'][0]['relatedRightRail']) == 3
            self.verify_logs(logging.INFO, msg='scroll')

            with patch.object(AsyncPointsApi, 'scroll_points', qdrant_error_mock):
                response = client.post("/", json=publisher_json(item_id, pub_url)).json()

            assert not response.get('errors')
            assert len(response['data']['_entities'][0]['relatedRightRail']) == 3
            self.verify_logs(logging.INFO, method='cache', msg='publisher')
