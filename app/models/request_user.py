from typing import List

from pydantic import BaseModel


class RequestUser(BaseModel):
    """
    Represents user and session identifiers in internal and encoded representation:
    - user_id: integer user id for Pocket account. Not present on logged-out requests.
    - hashed_user_id: hashed (encoded) user_id. Not present on logged-out requests.
    - guid: integer identifier that is consistent across sessions.
    - hashed_user_id: hashed (encoded) guid.
    - user_models: models to use in hasUserModel Unleash strategy
    """

    user_id: int = None
    hashed_user_id: str = None
    guid: int = None
    hashed_guid: str = None
    locale: str = None  # e.g. en-US
    user_models: List[str] = []
