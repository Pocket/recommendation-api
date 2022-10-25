from pydantic import BaseModel


class PocketClient(BaseModel):
    """
    Represents a Pocket Client a.k.a. "API User".
    """

    consumer_key: str = None
    api_id: str = None
    application_name: int = None
