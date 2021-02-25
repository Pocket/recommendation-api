import random
from typing import ClassVar

from pydantic import BaseModel
from aiocache import caches, Cache
from aiocache.serializers import BaseSerializer


import app.config


class PydanticSerializer(BaseSerializer):

    def dumps(self, value: BaseModel):
        return value.json()

    def loads(self, value: str):
        from app.models.candidate_set import CandidateSetModel
        return CandidateSetModel.parse_obj(value)


def get_cache_config():
    server = random.choice(app.config.elasticache['servers'])
    endpoint, port = server.split(':')

    return {
        'default': {
            'cache': Cache.MEMCACHED,
            'endpoint': endpoint,
            'port': port,
            'serializer': {
                'class': PydanticSerializer,
            },
        }
    }


caches.set_config(get_cache_config())

alias = 'default'
