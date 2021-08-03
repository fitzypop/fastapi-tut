"""Main FastAPI File."""

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from fastapi import FastAPI

# from pydantic import BaseModel


# Enum example
class ModelName(str, Enum):
    """Names of Models."""

    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"


@dataclass
class Item:
    """Sample of a Request Model."""

    name: str
    price: float
    is_offer: Optional[bool] = None


app = FastAPI()


@app.get("/")
async def read_root():
    """Read from api root."""
    return {"Hello": "World"}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """Get a Deep Learning Model."""
    if model_name == ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# Example of a Path Type String in a Path Parameter
# This is a Starlette feature
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """Read a file from the given path."""
    return {"file_path": file_path}


# Order Matters when it comes to Paths


@app.get("/item/{item_id}")
async def read_item(item_id: str):
    """Read Item from Path Parameter."""
    return {"item_id", item_id}


@app.get("/items/{item_id}")
async def read_items_with_options(item_id: int, q: str = None):
    """Read Item from query string."""
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """Update Item from query string."""
    return {"item_name": item.name, "item_id": item_id}


# Query Paramters Examples

# Anything that is not defined in the path, but has a default value is a query paramter with FastAPI

fake_things_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Query Paramters will be any key-value pair after a '?' in the URL, and separated by '&'


@app.get("/things")
async def get_thing(skip: int = 0, limit: int = 10):
    """Get things, skippable."""
    return fake_things_db[skip : skip + limit]
