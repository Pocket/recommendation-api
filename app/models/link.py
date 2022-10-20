from pydantic import BaseModel, Field


class LinkModel(BaseModel):
    url: str = Field(description='The URL to send the user to when clicking on the link.')
    text: str = Field(description='The link text displayed to the user.')


