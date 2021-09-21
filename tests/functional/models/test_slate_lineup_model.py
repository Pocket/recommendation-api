from tests.functional.test_dynamodb_base import TestDynamoDBBase
from tests.unit.utils import initialize_slate_lineups

from unittest.mock import patch

from copy import deepcopy

import app.config
from app.models.slate_lineup import SlateLineupModel
from app.models.slate_config import SlateConfigModel, CuratorTopic
from app.models.slate_experiment import SlateExperimentModel
from app.models.slate_lineup_experiment import SlateLineupExperimentModel
from app.models.slate_lineup_config import SlateLineupConfigModel
from app.models.personalized_topic_list import PersonalizedTopicList, PersonalizedTopicElement


test_candidate = {
    "id": "test-candidate-id",
    "version": 1,
    "created_at": 1612907252,
    "candidates": [
        {
            "feed_id": 1,
            "item_id": 3208490410,
            "publisher": "hbr.org"
        }
    ]
}

test_candidate_2 = {
    "id": "test-candidate-id-2",
    "version": 1,
    "created_at": 1612907252,
    "candidates": [
        {
            "feed_id": 1,
            "item_id": 11,
            "publisher": "getpocket.com"
        },
        {
            "feed_id": 1,
            "item_id": 12,
            "publisher": "getpocket.com"
        }
    ]
}

# First slate
slate_config_id = 'test-slate-config-id'
slate_experiment = SlateExperimentModel('test-ex', 'test-ex-desc', ['top15', 'thompson-sampling'],
                                        ['test-candidate-id'])
slate_config_model = SlateConfigModel(slate_config_id, 'test-this-slate', 'test-desc', experiments=[
    slate_experiment], curator_topic_label=CuratorTopic.HEALTH.value)

# Second slate
slate_config_id_2 = 'test-slate-config-id-2'
slate_experiment_2 = SlateExperimentModel('test-ex-2', 'test-ex-desc-2', ['top15', 'thompson-sampling'],
                                        ['test-candidate-id-2'])
slate_config_model_2 = SlateConfigModel(slate_config_id_2, 'test-this-slate-2', 'test-desc-2',
                                        experiments=[slate_experiment_2])

# Lineup with one slate
slate_lineup_config_id = 'test-slate_lineup-config-id'
slate_lineup_experiment = SlateLineupExperimentModel('test-ex', 'test-ex-desc', ['top15'], [slate_config_id])
slate_lineup_config_model = SlateLineupConfigModel(slate_lineup_config_id, 'test-desc', [slate_lineup_experiment])

# Lineup with two slates
slate_lineup_config_id_2 = 'test-slate_lineup-config-id-2'
slate_lineup_experiment_2 = SlateLineupExperimentModel('test-ex-2', 'test-ex-desc-2', ['top15'],
                                                     slates=[slate_config_id, slate_config_id_2])
slate_lineup_config_model_2 = SlateLineupConfigModel(slate_lineup_config_id_2, 'test-desc', [slate_lineup_experiment_2])

# personalized slate lineup
personalized_slate_lineup = deepcopy(slate_lineup_config_model)
personalized_slate_lineup.id = 'personalized-lineup-id'
personalized_slate_lineup.experiments[0].rankers = ["top1-topics"]

# Slate Lineups by id
slate_lineup_configs_by_id = {
    slate_lineup_config_model.id: slate_lineup_config_model,
    slate_lineup_config_model_2.id: slate_lineup_config_model_2,
    personalized_slate_lineup.id: personalized_slate_lineup,
}

# Slates by id
slate_configs_by_id = {
    slate_config_id: slate_config_model,
    slate_config_id_2: slate_config_model_2,
}


class TestSlateLineupModel(TestDynamoDBBase):

    @patch('app.models.slate_lineup_config.SlateLineupConfigModel.find_by_id', return_value=slate_lineup_config_model)
    @patch('app.models.slate_config.SlateConfigModel.find_by_id', return_value=slate_config_model)
    async def test_get_slate_lineup(self, slate_config, slate_lineup_config):
        self.candidate_set_table.put_item(Item=test_candidate)

        slate_lineup = await SlateLineupModel.get_slate_lineup_with_fallback(slate_lineup_config_id)

        assert slate_lineup.id == slate_lineup_config_id
        assert slate_lineup.slates[0].id == slate_config_id
        assert len(slate_lineup.requestId) == 36  # length of uuid4
        assert slate_lineup.slates[0].recommendations[0].item.item_id == '3208490410'

    @patch('app.models.slate_lineup_config.SlateLineupConfigModel.find_by_id', return_value=slate_lineup_config_model)
    @patch.object(SlateConfigModel, 'SLATE_CONFIGS_BY_ID', slate_configs_by_id)
    @patch.object(app.config, 'qa_slate_map', {slate_config_id: slate_config_id_2})
    async def test_get_slate_lineup_for_qa_user(self, slate_lineup_config):
        self.candidate_set_table.put_item(Item=test_candidate)
        self.candidate_set_table.put_item(Item=test_candidate_2)

        qa_user_id = app.config.qa_user_ids[0]
        slate_lineup = await SlateLineupModel.get_slate_lineup_with_fallback(slate_lineup_config_id, user_id=qa_user_id)

        assert slate_lineup.id == slate_lineup_config_id
        assert slate_lineup.slates[0].id == slate_config_id_2  # The slate is replace based on qa_slate_map.
        # Assert sets of items ids is equal. Order is random because of Thompson-sampling.
        assert {'11', '12'} == {recommendation.item_id for recommendation in slate_lineup.slates[0].recommendations}

    @patch.object(SlateLineupConfigModel, 'SLATE_LINEUP_CONFIGS_BY_ID', slate_lineup_configs_by_id)
    @patch.object(SlateConfigModel, 'SLATE_CONFIGS_BY_ID', slate_configs_by_id)
    @patch.object(app.config, 'personalization_fallback_slate_lineup', {personalized_slate_lineup.id: slate_lineup_config_id_2})
    async def test_get_slate_lineup_unpersonalized_fallback(self):
        self.candidate_set_table.put_item(Item=test_candidate)
        self.candidate_set_table.put_item(Item=test_candidate_2)


        # To test that the Slate lineup falls back to the default when the personalized lineup is not returned
        # Note: This throws an exception because user_id = None
        # Personalized to Default (personalization_fallback_slate_lineup) mapping: {personalized_slate_lineup.id: slate_lineup_config_id_2}
        unpersonalized_slate_lineup_id = slate_lineup_config_id_2
        slate_lineup = await SlateLineupModel.get_slate_lineup_with_fallback(personalized_slate_lineup.id, user_id = None)
        assert slate_lineup.id == unpersonalized_slate_lineup_id

    @patch.object(SlateLineupConfigModel, 'SLATE_LINEUP_CONFIGS_BY_ID', slate_lineup_configs_by_id)
    @patch.object(SlateConfigModel, 'SLATE_CONFIGS_BY_ID', slate_configs_by_id)
    @patch.object(app.config, 'personalization_fallback_slate_lineup', {personalized_slate_lineup.id: slate_lineup_config_id_2})
    @patch('app.models.personalized_topic_list.PersonalizedTopicList.get',
           return_value=PersonalizedTopicList(curator_topics=[PersonalizedTopicElement(
               curator_topic_label=CuratorTopic.HEALTH.value, score=1.0)], user_id='user-id')
           )
    async def test_get_slate_lineup_personalized(self, personalized_topic_list):
        self.candidate_set_table.put_item(Item=test_candidate)
        self.candidate_set_table.put_item(Item=test_candidate_2)

        # To test when Recit doesnt return error but returns a personalized list of topics
        #  the Slate lineup returned is the personalized lineup
        # initialize_slate_lineups()
        personalized_slate_lineup_id = personalized_slate_lineup.id
        unpersonalized_slate_lineup_id = slate_lineup_config_id_2
        slate_lineup = await SlateLineupModel.get_slate_lineup_with_fallback(personalized_slate_lineup_id, user_id ='user-id')
        assert slate_lineup.id == personalized_slate_lineup_id

    @patch('app.models.slate_lineup_config.SlateLineupConfigModel.find_by_id', return_value=slate_lineup_config_model)
    @patch('app.models.slate_config.SlateConfigModel.find_by_id', return_value=slate_config_model)
    async def test_get_slate_lineup_limited_recs(self, slate_config, slate_lineup_config):
        self.candidate_set_table.put_item(Item={
            "id": "test-candidate-id",
            "version": 1,
            "created_at": 1612907252,
            "candidates": [
                {
                    "feed_id": 1,
                    "item_id": 3208490410,
                    "publisher": "hbr.org"
                },
                {
                    "feed_id": 1,
                    "item_id": 3208650410,
                    "publisher": "hbr.org"
                },
                {
                    "feed_id": 1,
                    "item_id": 32084925410,
                    "publisher": "hbr.org"
                }
            ]
        })

        slate_lineup = await SlateLineupModel.get_slate_lineup_with_fallback(slate_lineup_config_id, recommendation_count=1)
        assert len(slate_lineup.slates[0].recommendations) == 1

    @patch('app.models.slate_lineup_config.SlateLineupConfigModel.find_by_id', return_value=slate_lineup_config_model)
    @patch('app.models.slate_config.SlateConfigModel.find_by_id', return_value=slate_config_model)
    async def test_get_slate_lineup_no_slates(self, slate_config, slate_lineup_config):
        self.candidate_set_table.put_item(Item=test_candidate)

        slate_lineup = await SlateLineupModel.get_slate_lineup_with_fallback(slate_lineup_config_id, slate_count=0)
        assert len(slate_lineup.slates) == 0

    @patch.object(SlateConfigModel, 'SLATE_CONFIGS_BY_ID', slate_configs_by_id)
    @patch('app.models.slate_lineup_config.SlateLineupConfigModel.find_by_id', return_value=slate_lineup_config_model_2)
    async def test_get_slate_lineup_dedupe_recs(self, slate_lineup_config):
        self.candidate_set_table.put_item(Item={
            "id": "test-candidate-id",
            "version": 1,
            "created_at": 1612907252,
            "candidates": [
                {
                    "feed_id": 1,
                    "item_id": 10,
                    "publisher": "hbr.org"
                },
                {
                    "feed_id": 1,
                    "item_id": 11,
                    "publisher": "hbr.org"
                },
            ]
        })

        self.candidate_set_table.put_item(Item=test_candidate_2)

        slate_lineup = await SlateLineupModel.get_slate_lineup_with_fallback(slate_lineup_config_id_2)
        assert len(slate_lineup.slates[0].recommendations) == 2
        assert len(slate_lineup.slates[1].recommendations) == 1

        # Assert sets of items ids is equal. Order is random because of Thompson-sampling.
        assert {'10', '11'} == {recommendation.item_id for recommendation in slate_lineup.slates[0].recommendations}
        # The items are deduplicated, so there is only one unique item left.
        assert slate_lineup.slates[1].recommendations[0].item_id == '12'
