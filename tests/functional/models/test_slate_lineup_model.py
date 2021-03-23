from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch

from app.models.slate_lineup import SlateLineupModel
from app.models.slate_config import SlateConfigModel
from app.models.slate_experiment import SlateExperimentModel
from app.models.slate_lineup_experiment import SlateLineupExperimentModel
from app.models.slate_lineup_config import SlateLineupConfigModel

slate_lineup_config_id = 'test-slate_lineup-config-id'
slate_lineup_experiment = SlateLineupExperimentModel('test-ex', 'test-ex-desc', ['top15'], ['test-slate-id'])
slate_lineup_config_model = SlateLineupConfigModel(slate_lineup_config_id, 'test-desc', [slate_lineup_experiment])

slate_config_id = 'test-slate_lineup-config-id'
slate_experiment = SlateExperimentModel('test-ex', 'test-ex-desc', ['top15', 'thompson-sampling'],
                                        ['test-candidate-id'])
slate_config_model = SlateConfigModel(slate_config_id, 'test-this-slate', 'test-desc', [slate_experiment])


class TestSlateLineupModel(TestDynamoDBBase):

    @patch('app.models.slate_lineup_config.SlateLineupConfigModel.find_by_id', return_value=slate_lineup_config_model)
    @patch('app.models.slate_config.SlateConfigModel.find_by_id', return_value=slate_config_model)
    async def test_get_slate_lineup(self, slate_config, slate_lineup_config):
        self.candidateSetTable.put_item(Item={
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
        })

        slate_lineup = await SlateLineupModel.get_slate_lineup(slate_lineup_config_id)

        assert slate_lineup.id == slate_lineup_config_id
        assert slate_lineup.slates[0].id == slate_config_id
        assert len(slate_lineup.requestId) == 36  # length of uuid4
        assert slate_lineup.slates[0].recommendations[0].item.item_id == '3208490410'

    @patch('app.models.slate_lineup_config.SlateLineupConfigModel.find_by_id', return_value=slate_lineup_config_model)
    @patch('app.models.slate_config.SlateConfigModel.find_by_id', return_value=slate_config_model)
    async def test_get_slate_lineup_limited_recs(self, slate_config, slate_lineup_config):
        self.candidateSetTable.put_item(Item={
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

        slate_lineup = await SlateLineupModel.get_slate_lineup(slate_lineup_config_id, recommendation_count=1)
        assert len(slate_lineup.slates[0].recommendations) == 1

    @patch('app.models.slate_lineup_config.SlateLineupConfigModel.find_by_id', return_value=slate_lineup_config_model)
    @patch('app.models.slate_config.SlateConfigModel.find_by_id', return_value=slate_config_model)
    async def test_get_slate_lineup_no_slates(self, slate_config, slate_lineup_config):
        self.candidateSetTable.put_item(Item={
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
        })

        slate_lineup = await SlateLineupModel.get_slate_lineup(slate_lineup_config_id, slate_count=0)
        assert len(slate_lineup.slates) == 0
