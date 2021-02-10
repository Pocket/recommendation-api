import random

from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List
from time import perf_counter
from asyncio import gather

from app.models.slate import SlateModel
from app.models.layout_config import LayoutConfigModel
from app.models.slate_config import SlateConfigModel
from app.models.candidate_set import CandidateSetModel
from app.models.clickdata import ClickdataModel, RecommendationModules
from app.models.recommendation import RecommendationModel
from app.rankers import RANKERS


class LayoutModel(BaseModel):
    id: str
    requestID: str = None
    experimentID: str = None
    slates: List[SlateModel]

    @staticmethod
    @xray_recorder.capture_async('models_layout_get_layout')
    async def get_layout(layout_id: str) -> 'LayoutModel':
        t_start = perf_counter()
        layout_experiment, slates = await LayoutModel.__get_slates_from_layout(layout_id)

        layout = LayoutModel.parse_obj({
            'id': layout_id,
            'experimentID': layout_experiment.id,
            'slates': []
        })
        layout.slates = slates

        t_stop = perf_counter()
        print("Elapsed time during whole function execution seconds:", t_stop - t_start)

        return layout

    @staticmethod
    async def __get_slates_from_layout(layout_id):
        # get the requested layout from the config using the layout_id
        layout_config = LayoutConfigModel.find_by_id(layout_id)
        # get the random experiment from the layout
        experiment = random.choice(layout_config.experiments)
        # get slate_ids from the experiment
        slate_ids = experiment.slates
        # get slates from the slate_ids
        slate_configs = []
        for slate_id in slate_ids:
            slate_configs.append(SlateConfigModel.find_by_id(slate_id))
        # apply rankers from the layout experiment on the slates
        for ranker in experiment.rankers:
            slate_configs = RANKERS[ranker](slate_configs)
        return experiment, await LayoutModel.__get_slate_models(slate_configs)

    @staticmethod
    async def __get_slate_models(slate_configs):
        slate_models = []
        # for each slate, get random experiment
        for slate_config in slate_configs:
            experiment = random.choice(slate_config.experiments)
            recommendations = await LayoutModel.__get_slate_recommendations(experiment)

            # add the slate model to the list
            slate_model = SlateModel.parse_obj({
                'id': slate_config.id,
                'experimentID': experiment.id,
                'description': slate_config.description,
                'display_name': slate_config.displayName,
                'recommendations': []
            })
            slate_model.recommendations = recommendations
            slate_models.append(slate_model)

        return slate_models

    @staticmethod
    async def __get_slate_recommendations(experiment):
        recommendations = []
        candidate_sets = []
        # for each candidate set id, get the candidate set record from the db
        for candidate_set_id in experiment.candidate_sets:
            candidate_sets.append(CandidateSetModel.get(candidate_set_id))
        candidate_sets = await gather(*candidate_sets)
        for candidate_set in candidate_sets:
            # apply rankers from the slate experiment on the candidate set's candidates
            for ranker in experiment.rankers:
                if ranker == 'thompson-sampling':
                    # thompson sampling takes two specific arguments so it needs to be handled differently
                    candidate_set.candidates = await LayoutModel.__thompson_sample(candidate_set, ranker)
                    continue
                candidate_set.candidates = RANKERS[ranker](candidate_set.candidates)

                # add the recommendations
                for candidate in candidate_set.candidates:
                    recommendations.append(candidate)

        return recommendations

    @staticmethod
    async def __thompson_sample(candidate_set, ranker) -> ['RecommendationModel']:
        recs = [candidate.item_id for candidate in candidate_set.candidates]
        try:
            click_data = await ClickdataModel.get_clickdata(RecommendationModules.TOPIC, recs)
        except ValueError:
            print(f'click data not found for candidates in candidate set id {candidate_set.id}')
            click_data = {}
        return RANKERS[ranker](candidate_set.candidates, click_data)
