from pydantic import BaseModel


class ApiClient(BaseModel):
    """
    Represents the client (a.k.a. "API User") making the request to this API.
    """

    consumer_key: str = None
    api_id: str
    application_name: str = None
    is_native: bool = None  # Indicates whether an app is a native Pocket app.
    is_trusted: bool = None  # Indicates the app is non-automated actions and represents real human usage
