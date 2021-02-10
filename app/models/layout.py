import random

from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List
from time import perf_counter

from app.models.slate import SlateModel
from app.models.layout_config import LayoutConfigModel
from app.models.slate_config import SlateConfigModel
from app.models.candidate_set import CandidateSetModel
from app.models.clickdata import ClickdataModel
from app.models.topic_recommendations import TopicRecommendationsModelUtils
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
        # get the requested layout from the config using the layout_id
        layout_configs = LayoutConfigModel.load_layout_configs()
        layout_config = None

        for config in layout_configs:
            if config.id == layout_id:
                layout_config = config
                break

        # get the random experiment from the layout
        experiment = random.choice(layout_config.experiments)

        # get slate_ids from the experiment
        slate_ids = experiment.slates

        # get slates from the slate_ids
        slates = []
        for slate_id in slate_ids:
            slate_configs = SlateConfigModel.load_slate_configs()
            for config in slate_configs:
                if config.id == slate_id:
                    slates.append(config)
                    break

        # apply rankers from the layout experiment on the slates
        for ranker in experiment.rankers:
            slates = RANKERS[ranker](slates)

        slate_models = []
        # for each slate, get random experiment
        for slate in slates:
            experiment = random.choice(slate.experiments)

            recommendations = []
            # for each candidate set id, get the candidate set record from the db
            for candidate_set_id in experiment.candidate_sets:
                candidate_set = await CandidateSetModel.get(candidate_set_id)

                # apply rankers from the slate experiment on the candidate set's candidates
                for ranker in experiment.rankers:
                    if ranker == 'thompson-sampling':
                        # thompson sampling takes two specific arguments so it needs to be handled differently
                        continue
                    candidate_set.candidates = RANKERS[ranker](candidate_set.candidates)

                    # add the recommendations
                    for candidate in candidate_set.candidates:
                        recommendations.append(candidate)

            # add the slate model to the list
            slate_model = SlateModel.parse_obj({
                'id': slate.id,
                'experimentID': experiment.id,
                'description': slate.description,
                'recommendations': []
            })
            slate_model.recommendations = recommendations
            slate_models.append(slate_model)

        layout = LayoutModel.parse_obj({
            'id': layout_id,
            'requestID': None,
            'experimentID': experiment.id,
            'slates': []
        })
        layout.slates = slate_models

        t_stop = perf_counter()
        print("Elapsed time during the whole program in seconds:", t_stop - t_start)

        return layout
