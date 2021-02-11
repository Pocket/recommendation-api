import random

from aws_xray_sdk.core import xray_recorder
from pydantic import BaseModel
from typing import List

from app.models.recommendation import RecommendationModel
from app.models.slate_config import SlateConfigModel


class SlateModel(BaseModel):
    id: str
    requestID: str = None
    experimentID: str = None
    pageviewGUID: str = None
    display_name: str = None
    description: str = None
    recommendations: List[RecommendationModel]

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_slate')
    async def get_slate(slate_id: str) -> 'SlateModel':
        return SlateModel.parse_obj({
            'id': slate_id,
            'requestID': '1',
            'experimentID': '1',
            'pageviewGUID': '1',
            'display_name': 'Fake slate',
            'description': 'Fake description for the people',
            'recommendations': [{
                'feed_item_id': '1',
                'item_id': '1',
                'feed_id': '1',
                'rec_src': 'RecommendationAPI',
                'publisher': 'Fake Times'
            }],
        })

    @staticmethod
    @xray_recorder.capture_async('models_slate_get_all')
    async def get_all() -> ['SlateModel']:
        return [SlateModel.get_slate('fake1'), SlateModel.get_slate('fake2')]

    @staticmethod
    async def get_slates_from_slate_configs(slate_configs: List['SlateConfigModel']) -> ['SlateModel']:
        slate_models = []
        # for each slate, get random experiment
        for slate_config in slate_configs:
            experiment = random.choice(slate_config.experiments)
            recommendations = await RecommendationModel.get_recommendations_from_experiment(experiment)

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
