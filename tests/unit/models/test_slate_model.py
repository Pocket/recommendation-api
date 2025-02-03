import json
import unittest
from typing import List

from app.models.slate import SlateModel, deduplicate_recommendations_across_slates
from app.models.recommendation import RecommendationModel


class TestSlateModel(unittest.IsolatedAsyncioTestCase):

    async def test_deduplicate_slates_without_empty_input(self):
        slate = self.__get_slate_model([])

        deduped_slate = await deduplicate_recommendations_across_slates([slate])

        assert len(deduped_slate[0].recommendations) == 0

    async def test_deduplicate_slates_without_dupes(self):
        slate0 = self.__get_slate_model(['1', '2'])
        slate1 = self.__get_slate_model(['3', '4'])

        deduped_slate_0, deduped_slate_1 = await deduplicate_recommendations_across_slates([slate0, slate1])

        assert len(deduped_slate_0.recommendations) == 2
        assert len(deduped_slate_1.recommendations) == 2

        assert deduped_slate_0.recommendations[0].item_id == '1'
        assert deduped_slate_0.recommendations[1].item_id == '2'
        assert deduped_slate_1.recommendations[0].item_id == '3'
        assert deduped_slate_1.recommendations[1].item_id == '4'

    async def test_deduplicate_slates(self):
        slate0 = self.__get_slate_model(['1', '2'])
        slate1 = self.__get_slate_model(['2', '3'])
        slate2 = self.__get_slate_model(['2', '3', '4'])

        deduped_slate_0, deduped_slate_1, deduped_slate_2 =\
            await deduplicate_recommendations_across_slates([slate0, slate1, slate2])

        assert len(deduped_slate_0.recommendations) == 2
        assert len(deduped_slate_1.recommendations) == 1
        assert len(deduped_slate_2.recommendations) == 1

        assert deduped_slate_0.recommendations[0].item_id == '1'
        assert deduped_slate_0.recommendations[1].item_id == '2'
        assert deduped_slate_1.recommendations[0].item_id == '3'
        assert deduped_slate_2.recommendations[0].item_id == '4'

    def __get_slate_model(self, item_ids: List[str]) -> SlateModel:
        recommendations = [
            RecommendationModel.candidate_dict_to_recommendation({'item_id': item_id}) for item_id in item_ids
        ]
        return SlateModel(id=1, recommendations=recommendations)
