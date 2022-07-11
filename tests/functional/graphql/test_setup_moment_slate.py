import datetime
import random
import uuid
from typing import List, Sequence

from graphql.execution.executors.asyncio import AsyncioExecutor
from graphene.test import Client
from fastapi.testclient import TestClient

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.dispatch import SetupMomentDispatch
from app.data_providers.topic_provider import TopicProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.graphql.graphql_router import schema
from app.main import app
from app.models.corpus_item_model import CorpusItemModel
from app.models.topic import TopicModel
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel
from tests.assets.topics import *
from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch
from collections import namedtuple

MockResponse = namedtuple('MockResponse', 'status')


corpus_topics = [health_topic, business_topic, entertainment_topic, technology_topic, gaming_topic]
corpus_topic_ids = [t.corpus_topic_id for t in corpus_topics]
topics_by_id = {t.id: t for t in corpus_topics}


def _corpus_items_fixture(n: int) -> [CorpusItemModel]:
    return [CorpusItemModel(id=uuid.uuid4().hex, topic=random.choice(corpus_topic_ids)) for _ in range(n)]


def _user_recommendation_preferences_fixture(
        user_id: str, preferred_topics: List[TopicModel]
) -> UserRecommendationPreferencesModel:
    return UserRecommendationPreferencesModel(
        user_id=user_id,
        updated_at=datetime.datetime(2022, 5, 12, 15, 30),
        preferred_topics=preferred_topics,
    )


def _get_topics_fixture(topics_ids: Sequence[str]) -> List[TopicModel]:
    return [topics_by_id[id] for id in topics_ids]


class TestSetupMomentSlate(TestDynamoDBBase):
    client: Client

    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.client = Client(schema)
        self.user_id = 'johnjacobjingleheimerschmidt'

    @patch.object(CorpusFeatureGroupClient, 'get_corpus_items')
    @patch.object(UserRecommendationPreferencesProvider, 'fetch')
    def test_setup_moment_slate(self, mock_fetch_user_recommendation_preferences, mock_get_ranked_corpus_items):
        corpus_items_fixture = _corpus_items_fixture(n=100)
        mock_get_ranked_corpus_items.return_value = corpus_items_fixture

        preferred_topics = [technology_topic, gaming_topic]
        preferences_fixture = _user_recommendation_preferences_fixture(self.user_id, preferred_topics)
        mock_fetch_user_recommendation_preferences.return_value = preferences_fixture

        with TestClient(app):
            executed = self.client.execute(
                '''
                query SetupMomentSlate {
                  setupMomentSlate {
                    headline
                    subheadline
                    recommendations(count: 100) {
                      id
                      corpusItem {
                        id
                        topic
                      }
                    }
                  }
                }
                ''',
                context_value={'user_id': self.user_id},
                executor=AsyncioExecutor())

            response = executed['data']['setupMomentSlate']
            recs = response['recommendations']
            assert response['headline'] == 'Save an article you find interesting'

            # Assert that all corpus items are being returned.
            assert len(recs) == len(corpus_items_fixture)
            assert {rec['corpusItem']['id'] for rec in recs} == {item.id for item in corpus_items_fixture}

            # Assert that recommendations of preferred topics are ordered before non-preferred ones.
            # recommendations are rotated to spread topics
            pref_corpus_topic_ids = [t.corpus_topic_id for t in preferred_topics]
            pref_corpus_item_ids = {c.id for c in corpus_items_fixture if c.topic in pref_corpus_topic_ids}
            non_pref_corpus_item_ids = {c.id for c in corpus_items_fixture if c.topic not in pref_corpus_topic_ids}
            assert {rec['corpusItem']['id'] for rec in recs[:len(pref_corpus_item_ids)]} == pref_corpus_item_ids
            assert {rec['corpusItem']['id'] for rec in recs[len(pref_corpus_item_ids):]} == non_pref_corpus_item_ids

    @patch.object(CorpusFeatureGroupClient, 'get_corpus_items')
    @patch.object(UserRecommendationPreferencesProvider, 'fetch')
    @patch.object(TopicProvider, 'get_topics')
    def test_default_count(self, mock_get_topics, mock_fetch_user_recommendation_preferences, mock_get_ranked_corpus_items):
        corpus_items_fixture = _corpus_items_fixture(n=100)
        mock_get_ranked_corpus_items.return_value = corpus_items_fixture
        mock_fetch_user_recommendation_preferences.return_value = \
            _user_recommendation_preferences_fixture(self.user_id, [])
        mock_get_topics.return_value = _get_topics_fixture(SetupMomentDispatch.DEFAULT_TOPICS)

        with TestClient(app):
            executed = self.client.execute(
                '''
                query SetupMomentSlate {
                  setupMomentSlate {
                    headline
                    subheadline
                    recommendations {
                      id
                      corpusItem {
                        id
                        topic
                      }
                    }
                  }
                }
                ''',
                context_value={'user_id': self.user_id},
                executor=AsyncioExecutor())

            response = executed['data']['setupMomentSlate']
            recs = response['recommendations']

            # Assert that 10 (the default for count) corpus items are being returned.
            assert len(recs) == 10
            # Because the user doesn't have any preferred topics, the order of recommendations should be unchanged.
            assert {rec['corpusItem']['topic'] for rec in recs} == \
                   {health_topic.corpus_topic_id, business_topic.corpus_topic_id, entertainment_topic.corpus_topic_id}
