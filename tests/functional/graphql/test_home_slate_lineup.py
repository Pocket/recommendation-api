import datetime
import random
import uuid
from typing import Sequence

from asgi_lifespan import LifespanManager
from httpx import AsyncClient, ASGITransport

from app.data_providers.corpus.corpus_feature_group_client import CorpusFeatureGroupClient
from app.data_providers.feature_group.feature_group_client import FeatureGroupClient
from app.data_providers.snowplow.config import SnowplowConfig
from app.data_providers.unleash_provider import UnleashProvider
from app.data_providers.user_impression_cap_provider import UserImpressionCapProvider
from app.data_providers.user_recommendation_preferences_provider import UserRecommendationPreferencesProvider
from app.main import app
from app.models.corpus_item_model import CorpusItemModel
from app.models.request_user import RequestUser
from app.models.user_recommendation_preferences import UserRecommendationPreferencesModel
from tests.functional.test_util.snowplow import wait_for_snowplow_events
from tests.assets.topics import *
from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch

from tests.functional.test_util.snowplow import SnowplowMicroClient


corpus_topics = [health_topic, business_topic, entertainment_topic, technology_topic, gaming_topic, travel_topic]
corpus_topic_ids = [t.corpus_topic_id for t in corpus_topics]
topics_by_id = {t.id: t for t in corpus_topics}


def _user_recommendation_preferences_fixture(
        hashed_user_id: str, preferred_topics: List[TopicModel]
) -> UserRecommendationPreferencesModel:
    return UserRecommendationPreferencesModel(
        hashed_user_id=hashed_user_id,
        updated_at=datetime.datetime(2022, 5, 12, 15, 30),
        preferred_topics=preferred_topics,
    )


def _corpus_items_fixture(n: int) -> [CorpusItemModel]:
    return [CorpusItemModel(id=str(uuid.uuid4()), topic=random.choice(corpus_topic_ids)) for _ in range(n)]


def _get_topics_fixture(topics_ids: Sequence[str]) -> List[TopicModel]:
    return [topics_by_id[id] for id in topics_ids]


def _get_home_query(locale=None):
    return '''
        query {
          homeSlateLineup''' + (f'(locale: "{locale}")' if locale else '') + ''' {
            id
            slates {
              headline
              subheadline
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
    '''


HOME_SLATE_LINEUP_QUERY = _get_home_query()


class TestHomeSlateLineup(TestDynamoDBBase):
    async def asyncSetUp(self):
        await super().asyncSetUp()
        self.request_user = RequestUser(
            user_id=1,
            hashed_user_id='426T0A36g8844p7442d8by2d79p8gc136e6E1bN0x6Q1cqQ52dibya97x14US411',
        )
        self.headers = {
            'userId': str(self.request_user.user_id),
            'encodedId': self.request_user.hashed_user_id,
            'apiId': '94110',
            'consumerKey': 'web-client-consumer-key',
            'applicationName': 'Pocket web-client',
            'applicationIsNative': 'true',
            'applicationIsTrusted': 'true',
        }

        populate_topics(self.metadata_table)
        self.snowplow_micro = SnowplowMicroClient(config=SnowplowConfig())
        self.snowplow_micro.reset_snowplow_events()

    @patch.object(CorpusFeatureGroupClient, 'fetch')
    @patch.object(UserRecommendationPreferencesProvider, 'fetch')
    @patch.object(UserImpressionCapProvider, 'get')
    @patch.object(UnleashProvider, '_get_all_assignments')
    @patch.object(FeatureGroupClient, 'batch_get_records')
    async def test_personalized_home_slate_lineup(
            self,
            mock_batch_get_records,
            mock_get_all_assignments,
            mock_get_user_impression_caps,
            mock_fetch_user_recommendation_preferences,
            mock_fetch_corpus_items
    ):
        corpus_items_fixture = _corpus_items_fixture(n=100)
        mock_fetch_corpus_items.return_value = corpus_items_fixture

        preferred_topics = [technology_topic, gaming_topic]
        preferences_fixture = _user_recommendation_preferences_fixture(
            self.request_user.hashed_user_id, preferred_topics)
        mock_fetch_user_recommendation_preferences.return_value = preferences_fixture
        mock_get_user_impression_caps.return_value = corpus_items_fixture[:6]
        mock_get_all_assignments.return_value = []

        async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client, LifespanManager(app):
            response = await client.post('/', json={'query': HOME_SLATE_LINEUP_QUERY}, headers=self.headers)
            data = response.json()

            assert not data.get('errors')
            slates = data['data']['homeSlateLineup']['slates']

            # Assert that the expected number of slates is being returned.
            assert len(slates) == 5
            # First slate is Pocket Worthy
            assert slates[0]['headline'] == 'Pocket-Worthy Reads'
            # Second slate is Collections
            assert slates[1]['headline'] == 'Popular Collections'
            # Third slate is Pocket Hits
            assert slates[2]['headline'] == 'Today’s Pocket Hits'
            # Fourth slate is For You
            assert slates[3]['headline'] == 'For You'
            # Fifth slate is Life Hacks
            assert slates[4]['headline'] == 'Life Hacks'

            recommendation_counts = [len(slate['recommendations']) for slate in slates]
            assert recommendation_counts == len(slates)*[5]  # Each slates has 5 recs each

            await wait_for_snowplow_events(self.snowplow_micro, n_expected_event=2)
            all_snowplow_events = self.snowplow_micro.get_event_counts()
            assert all_snowplow_events == {'total': 1, 'good': 1, 'bad': 0}

    @patch.object(CorpusFeatureGroupClient, 'fetch')
    @patch.object(UserRecommendationPreferencesProvider, 'fetch')
    @patch.object(UserImpressionCapProvider, 'get')
    @patch.object(UnleashProvider, '_get_all_assignments')
    @patch.object(FeatureGroupClient, 'batch_get_records')
    async def test_unpersonalized_home_slate_lineup(
            self,
            mock_batch_get_records,
            mock_get_all_assignments,
            mock_get_user_impression_caps,
            mock_fetch_user_recommendation_preferences,
            mock_fetch_corpus_items
    ):
        corpus_items_fixture = _corpus_items_fixture(n=100)
        mock_fetch_corpus_items.return_value = corpus_items_fixture
        mock_fetch_user_recommendation_preferences.return_value = None  # User has does not have a preferences record
        mock_get_user_impression_caps.return_value = corpus_items_fixture[:6]
        mock_get_all_assignments.return_value = []

        async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client, LifespanManager(app):
            response = await client.post('/', json={'query': HOME_SLATE_LINEUP_QUERY}, headers=self.headers)
            data = response.json()

            assert not data.get('errors')
            slates = data['data']['homeSlateLineup']['slates']

            # First slate has Worthy Reads
            assert slates[0]['headline'] == 'Pocket-Worthy Reads'

            recommendation_counts = [len(slate['recommendations']) for slate in slates]
            assert recommendation_counts == len(slates)*[5]  # Each slates has 5 recs each

            await wait_for_snowplow_events(self.snowplow_micro, n_expected_event=2)
            all_snowplow_events = self.snowplow_micro.get_event_counts()
            assert all_snowplow_events == {'total': 1, 'good': 1, 'bad': 0}

    @patch.object(CorpusFeatureGroupClient, 'fetch')
    @patch.object(UserRecommendationPreferencesProvider, 'fetch')
    @patch.object(UserImpressionCapProvider, 'get')
    @patch.object(UnleashProvider, '_get_all_assignments')
    @patch.object(FeatureGroupClient, 'batch_get_records')
    async def test_german_unpersonalized_home_slate_lineup(
            self,
            mock_batch_get_records,
            mock_get_all_assignments,
            mock_get_user_impression_caps,
            mock_fetch_user_recommendation_preferences,
            mock_fetch_corpus_items,
    ):
        corpus_items_fixture = _corpus_items_fixture(n=100)
        mock_fetch_corpus_items.return_value = corpus_items_fixture
        mock_fetch_user_recommendation_preferences.return_value = None  # User has does not have a preferences record
        mock_get_user_impression_caps.return_value = []
        mock_get_all_assignments.return_value = []
        mock_batch_get_records.return_value = []

        async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client, LifespanManager(app):
            response = await client.post('/', json={'query': _get_home_query('de-DE')}, headers=self.headers)
            data = response.json()

            assert not data.get('errors')
            slates = data['data']['homeSlateLineup']['slates']
            assert slates[0]['headline'] == 'Beliebte Collections'
            assert slates[0]['moreLink']['url'] == 'https://getpocket.com/collections'
            assert slates[0]['moreLink']['text'] == 'Mehr Collections entdecken'
            assert slates[1]['headline'] == 'Empfohlene Artikel'
            assert slates[1]['subheadline'] == 'Von Pocket kuratiert'

            await wait_for_snowplow_events(self.snowplow_micro, n_expected_event=2)
            all_snowplow_events = self.snowplow_micro.get_event_counts()
            assert all_snowplow_events == {'total': 1, 'good': 1, 'bad': 0}

    @patch.object(CorpusFeatureGroupClient, 'fetch')
    @patch.object(UserRecommendationPreferencesProvider, 'fetch')
    @patch.object(UserImpressionCapProvider, 'get')
    @patch.object(UnleashProvider, '_get_all_assignments')
    @patch.object(FeatureGroupClient, 'batch_get_records')
    async def test_no_user_home_slate_lineup(
            self,
            mock_batch_get_records,
            mock_get_all_assignments,
            mock_get_user_impression_caps,
            mock_fetch_user_recommendation_preferences,
            mock_fetch_corpus_items
    ):
        corpus_items_fixture = _corpus_items_fixture(n=100)
        mock_fetch_corpus_items.return_value = corpus_items_fixture
        mock_fetch_user_recommendation_preferences.return_value = None  # User has does not have a preferences record
        mock_get_user_impression_caps.return_value = []
        mock_get_all_assignments.return_value = []

        async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client, LifespanManager(app):
            response = await client.post('/', json={'query': HOME_SLATE_LINEUP_QUERY}, headers={
            'apiId': '94110',
            'consumerKey': 'web-client-consumer-key',
            'applicationName': 'Pocket web-client',
            'applicationIsNative': 'true',
            'applicationIsTrusted': 'true',
        })
            data = response.json()

            assert not data.get('errors')
            slates = data['data']['homeSlateLineup']['slates']

            # First slate has an unpersonalized recommendations
            assert slates[0]['headline'] == 'Pocket-Worthy Reads'
            assert slates[0]['recommendationReasonType'] is None

            recommendation_counts = [len(slate['recommendations']) for slate in slates]
            assert recommendation_counts == len(slates)*[5]  # Each slates has 5 recs each

            await wait_for_snowplow_events(self.snowplow_micro, n_expected_event=2)
            all_snowplow_events = self.snowplow_micro.get_event_counts()
            assert all_snowplow_events == {'total': 1, 'good': 1, 'bad': 0}
