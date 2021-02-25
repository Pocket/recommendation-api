import random
from typing import ClassVar

from pydantic import BaseModel
from aiocache import caches, Cache
from aiocache.serializers import BaseSerializer

import app.config
from app.models.candidate_set import CandidateSetModel


class PydanticSerializer(BaseSerializer):

    def dumps(self, value: BaseModel):
        return value.json()

    def loads(self, value: str):
        if value is None:
            return None

        return CandidateSetModel.parse_raw(value)


def get_cache_config():
    server = random.choice(app.config.elasticache['servers'])
    endpoint, port = server.split(':')

    return {
        'cache': Cache.MEMCACHED,
        'endpoint': endpoint,
        'port': port,
        'serializer': {
            'class': PydanticSerializer,
        },
    }


alias = 'elasticache'


def initialize_caches():
    caches.add(alias, get_cache_config())

#
# try:
#     caches.get(alias)
# except KeyError:
#     initialize_caches()
