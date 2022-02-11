import aioboto3

from asyncio import gather

import logging
from aws_xray_sdk.core import xray_recorder
from boto3.dynamodb.conditions import Key
from enum import Enum
from pydantic import BaseModel

from app.config import dynamodb as dynamodb_config
# Needs to exist for pydantic to resolve the model field "item: ItemModel" in the RecommendationModel
from app.graphql.item import Item
from app.models.candidate_set import candidate_set_factory
from app.models.metrics.recommendation_metrics_factory import RecommendationMetricsFactory
from app.models.item import ItemModel
from app.models.slate_experiment import SlateExperimentModel
from app.rankers import get_ranker, THOMPSON_SAMPLING_RANKERS

class CorpusItem (BaseModel):
    id: str = None