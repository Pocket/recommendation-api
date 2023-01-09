from typing import NewType

import strawberry

Locale = strawberry.scalar(
    NewType("Locale", str),
    description="A locale consisting of a 2-letter language code and a 2 letter country code, e.g. \"en-US\"",
)
