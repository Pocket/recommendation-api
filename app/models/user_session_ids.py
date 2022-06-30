from pydantic import BaseModel


class UserSessionIds(BaseModel):
    """
    Represents user and session identifiers in internal and encoded representation:
    - user_id:
    - hashed_user_id: hashed (encoded) user_id.
    - guid: integer identifier that is consistent across sessions.
    - hashed_user_id: hashed (encoded) guid.
    """

    user_id: int = None
    hashed_user_id: str = None
    guid: int = None
    hashed_guid: str = None
