from unittest.mock import patch

from tests.functional.test_dynamodb_base import TestDynamoDBBase

from app.models.slate_config import SlateConfigModel
from app.models.slate_experiment import SlateExperimentModel
from app.models.slate import SlateModel

candidates = [
    {
        'feed_id': 1,
        'item_id': 3208490410,
        'publisher': 'hbr.org',
        "url": "https://hbr.org/12"
    },
    {
        'feed_id': 1,
        'item_id': 32087704190,
        'publisher': 'hbr.org',
        "url": "https://hbr.org/16"
    },
    {
        'feed_id': 12,
        'item_id': 32087904100,
        'publisher': 'hbr.org',
        "url": "https://hbr.org/18"
    },
    {
        'feed_id': 2,
        'item_id': 32087904870,
        'publisher': 'hbr.org',
        "url": "https://hbr.org/17"
    }
]

slate_config_id = 'test-slate_lineup-config-id'
slate_experiment = SlateExperimentModel('test-ex', 'test-ex-desc', ['top15-items', 'thompson-sampling-28day'],
                                        ['test-candidate-id'])
slate_config_model = SlateConfigModel(slate_config_id, 'test-this-slate', 'test-desc', experiments=[slate_experiment])


class TestSlateModel(TestDynamoDBBase):

    def _put_candidates(self, count=None):
        """
        Put n <= 4 candidates into the candidates set table.
        :param count: Number of candidates (up to 4) to insert.

        TODO: It would be nice if we could manage/generate these fixtures centrally. Currently there's duplicated code
              in at least 3 classes to put candidates in DynamoDB.
        """
        self.candidate_set_table.put_item(Item={
            'id': 'test-candidate-id',
            'version': 1,
            'created_at': 1612907252,
            'candidates': candidates if count is None else candidates[:count],
        })

    async def asyncTearDown(self):
        await super().asyncTearDown()
        SlateConfigModel.SLATE_CONFIGS_BY_ID = {}

    @patch('app.models.slate_config.SlateConfigModel.find_by_id', return_value=slate_config_model)
    async def test_get_slate(self, slate_config):
        self._put_candidates(1)

        slate = await SlateModel.get_slate(slate_config_id)

        assert slate.id == slate_config_id
        assert slate.recommendations[0].item.item_id == '3208490410'
        assert len(slate.requestId) == 36  # length of uuid4
        assert slate.recommendations[0].publisher == 'hbr.org'

    async def test_list_slates(self):
        self._put_candidates(1)

        SlateConfigModel.SLATE_CONFIGS_BY_ID = {slate_config_id: slate_config_model}
        slates = await SlateModel.get_all(None, recommendation_count=0)

        assert type(slates) is list
        assert slates[0].id == slate_config_id
        assert len(slates[0].recommendations) == 0

    async def test_get_slates_from_slate_configs_without_recs(self):
        slates = await SlateModel.get_slates_from_slate_configs([slate_config_model], None, recommendation_count=0)

        assert slates[0].id == slate_config_id
        assert len(slates[0].recommendations) == 0

    async def test_get_slates_from_slate_configs_with_recs(self):
        self._put_candidates(1)

        slates = await SlateModel.get_slates_from_slate_configs([slate_config_model], None)

        assert slates[0].id == slate_config_id
        assert len(slates[0].recommendations) == 1

    async def test_get_slates_from_slate_configs_with_limited_recs(self):
        self._put_candidates(4)

        slates = await SlateModel.get_slates_from_slate_configs([slate_config_model], None, recommendation_count=2)

        assert slates[0].id == slate_config_id
        assert len(slates[0].recommendations) == 2
