from tests.functional.test_dynamodb_base import TestDynamoDBBase

from unittest.mock import patch

from app.models.layout import LayoutModel
from app.models.slate_config import SlateConfigModel
from app.models.slate_experiment import SlateExperimentModel
from app.models.layout_experiment import LayoutExperimentModel
from app.models.layout_config import LayoutConfigModel

layout_config_id = 'test-layout-config-id'
layout_experiment = LayoutExperimentModel('test-ex', 'test-ex-desc', ['top15'], ['test-slate-id'])
layout_config_model = LayoutConfigModel(layout_config_id, 'test-desc', [layout_experiment])

slate_config_id = 'test-layout-config-id'
slate_experiment = SlateExperimentModel('test-ex', 'test-ex-desc', ['top15', 'thompson-sampling'], ['test-candidate-id'])
slate_config_model = SlateConfigModel(slate_config_id, 'test-this-slate', 'test-desc', [slate_experiment])


class TestLayoutModel(TestDynamoDBBase):

    @patch('app.models.layout_config.LayoutConfigModel.find_by_id', return_value=layout_config_model)
    @patch('app.models.slate_config.SlateConfigModel.find_by_id', return_value=slate_config_model)
    async def test_get_layout(self, slate_config, layout_config):
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

        layout = await LayoutModel.get_layout(layout_config_id)

        assert layout.id == layout_config_id
        assert layout.slates[0].id == slate_config_id
        assert len(layout.requestID) == 36  # length of uuid4
        assert layout.slates[0].recommendations[0].item.item_id == '3208490410'


