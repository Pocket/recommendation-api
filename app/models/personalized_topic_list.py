import aiohttp
import logging
from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List, Dict

import app.config
from app.exceptions.personalization_error import PersonalizationError


class PersonalizedTopicElement(BaseModel):
    curator_topic_label: str
    score: float

