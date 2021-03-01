from unittest.mock import patch

from tests.functional.test_dynamodb_base import TestDynamoDBBase

from app.models.slate_config import SlateConfigModel
from app.models.slate_experiment import SlateExperimentModel
from app.models.slate import SlateModel

slate_config_id = 'test-layout-config-id'
slate_experiment = SlateExperimentModel('test-ex', 'test-ex-desc', ['top15', 'thompson-sampling'],
                                        ['test-candidate-id'])
slate_config_model = SlateConfigModel(slate_config_id, 'test-this-slate', 'test-desc', [slate_experiment])


class TestSlateModel(TestDynamoDBBase):
    def setup_method(self, method):
        super().setup_method(method)
        self.candidateSetTable.put_item(Item={
            'id': 'test-candidate-id',
            'version': 1,
            'created_at': 1612907252,
            'candidates': [
                {
                    'feed_id': 1,
                    'item_id': 3208490410,
                    'publisher': 'hbr.org'
                }
            ]
        })

    def teardown_method(self, method):
        super().teardown_method(method)
        SlateConfigModel.SLATE_CONFIGS_BY_ID = {}

    @patch('app.models.slate_config.SlateConfigModel.find_by_id', return_value=slate_config_model)
    async def test_get_slate(self, slate_config):
        slate = await SlateModel.get_slate(slate_config_id)

        assert slate.id == slate_config_id
        assert slate.recommendations[0].item.item_id == '3208490410'
        assert len(slate.requestID) == 36  # length of uuid4
        assert slate.recommendations[0].publisher == 'hbr.org'

    async def test_list_slates(self):
        SlateConfigModel.SLATE_CONFIGS_BY_ID = {slate_config_id: slate_config_model}
        slates = await SlateModel.get_all()

        assert type(slates) is list
        assert slates[0].id == slate_config_id
        assert len(slates[0].recommendations) == 0

    async def test_get_slates_from_slate_configs_without_recs(self):
        slates = await SlateModel.get_slates_from_slate_configs([slate_config_model], recommendation_count=0)

        assert slates[0].id == slate_config_id
        assert len(slates[0].recommendations) == 0

    async def test_get_slates_from_slate_configs_with_recs(self):
        slates = await SlateModel.get_slates_from_slate_configs([slate_config_model])

        assert slates[0].id == slate_config_id
        assert len(slates[0].recommendations) == 1

    async def test_get_slates_from_slate_configs_with_limited_recs(self):
        self.candidateSetTable.put_item(Item={
            'id': 'test-candidate-id',
            'version': 1,
            'created_at': 1612907252,
            'candidates': [
                {
                    'feed_id': 1,
                    'item_id': 32087904190,
                    'publisher': 'hbr.org'
                }
            ]
        })

        self.candidateSetTable.put_item(Item={
            'id': 'test-candidate-id',
            'version': 1,
            'created_at': 1612907252,
            'candidates': [
                {
                    'feed_id': 1,
                    'item_id': 3208490510,
                    'publisher': 'hbr.org'
                }
            ]
        })
        slates = await SlateModel.get_slates_from_slate_configs([slate_config_model], recommendation_count=2)

        assert slates[0].id == slate_config_id
        assert len(slates[0].recommendations) == 2
