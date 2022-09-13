import datetime
import random
import uuid
from typing import Sequence

from fastapi.testclient import TestClient

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.snowplow.config import SnowplowConfig
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.main import app
from app.models.corpus_item_model import CorpusItemModel
from app.models.topic import TopicModel
from app.models.user_ids import UserIds
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel
from tests.assets.topics import *
from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch

from tests.functional.test_util.snowplow import SnowplowMicroClient


corpus_topics = [health_topic, business_topic, entertainment_topic, technology_topic, gaming_topic, travel_topic]
corpus_topic_ids = [t.corpus_topic_id for t in corpus_topics]
topics_by_id = {t.id: t for t in corpus_topics}


def _user_recommendation_preferences_fixture(
        user_id: str, preferred_topics: List[TopicModel]
) -> UserRecommendationPreferencesModel:
    return UserRecommendationPreferencesModel(
        user_id=user_id,
        updated_at=datetime.datetime(2022, 5, 12, 15, 30),
        preferred_topics=preferred_topics,
    )


def _corpus_items_fixture(n: int) -> [CorpusItemModel]:
    return [CorpusItemModel(id=str(uuid.uuid4()), topic=random.choice(corpus_topic_ids)) for _ in range(n)]


def _get_topics_fixture(topics_ids: Sequence[str]) -> List[TopicModel]:
    return [topics_by_id[id] for id in topics_ids]


class TestHomeSlateLineup(TestDynamoDBBase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.user_ids = UserIds(
            user_id=1,
            hashed_user_id='1-hashed',
        )

        populate_topics(self.metadata_table)

        self.snowplow_micro = SnowplowMicroClient(config=SnowplowConfig())
        self.snowplow_micro.reset_snowplow_events()

    @patch.object(CorpusFeatureGroupClient, 'fetch')
    @patch.object(UserRecommendationPreferencesProvider, 'fetch')
    def test_home_slate_lineup(self, mock_fetch_user_recommendation_preferences, mock_get_ranked_corpus_items):
        corpus_items_fixture = _corpus_items_fixture(n=100)
        mock_get_ranked_corpus_items.return_value = corpus_items_fixture

        preferred_topics = [technology_topic, gaming_topic]
        preferences_fixture = _user_recommendation_preferences_fixture(str(self.user_ids.user_id), preferred_topics)
        mock_fetch_user_recommendation_preferences.return_value = preferences_fixture

        with TestClient(app) as client:
            data = client.post(
                '/',
                json={
                    'query': '''
                        query {
                          homeSlateLineup {
                            id
                            slates(count: 4) {
                              headline
                              moreLink {
                                url
                                text
                              }
                              recommendationReasonType
                              recommendations(count: 5) {
                                corpusItem {
                                  id
                                }
                                reason {
                                  name
                                  type
                                }
                              }
                            }
                          }
                        }
                    ''',
                },
                headers={
                    'userId': str(self.user_ids.user_id),
                    'encodedId': self.user_ids.hashed_user_id,
                }
            ).json()

            assert not data.get('errors')
            slate_lineup = data['data']['homeSlateLineup']
            slates = slate_lineup['slates']

            # Assert that the expected number of slates is being returned.
            assert len(slates) == 4

            # First slate has a link to the collections page
            assert slates[0]['moreLink']['url'] == 'https://getpocket.com/collections'
            # Last slates have topic explore links
            assert slates[1]['moreLink']['url'] == 'https://getpocket.com/explore/technology'
            assert slates[2]['moreLink']['url'] == 'https://getpocket.com/explore/entertainment'
            assert slates[3]['moreLink']['url'] == 'https://getpocket.com/explore/self-improvement'

            recommendation_counts = [len(slate['recommendations']) for slate in slates]
            assert recommendation_counts == len(slates)*[5]  # Each slates has 5 recs each

            all_snowplow_events = self.snowplow_micro.get_event_counts()
            # No Snowplow events are expected to be emitted at this point.
            assert all_snowplow_events == {'total': 0, 'good': 0, 'bad': 0}, self.snowplow_micro.get_last_error()
