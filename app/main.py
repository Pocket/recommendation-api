import os

import uvicorn
from fastapi import FastAPI

from app.models.feed_item import FeedItem

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "Hello": "World",
    }


@app.get("/feed/{item_id}", response_model=FeedItem)
def read_item(item_id: int):
    return FeedItem(id=item_id, title="Essential Reads")


if __name__ == "__main__":
    # This runs uvicorn in a local development environment.
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
