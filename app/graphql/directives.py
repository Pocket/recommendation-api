from enum import Enum

import strawberry
from strawberry import schema_directive
from strawberry.schema_directive import Location


@strawberry.enum()
class CacheControlScope(Enum):
    PUBLIC = strawberry.enum_value('PUBLIC')
    PRIVATE = strawberry.enum_value('PRIVATE')


@schema_directive(
    locations=[
        Location.FIELD_DEFINITION,
        Location.INTERFACE,
        Location.OBJECT
    ],
    name="cacheControl",
    print_definition=True,
)
class CacheControl:
    maxAge: int
    scope: CacheControlScope = CacheControlScope.PUBLIC
