"""Request Body section of FastAPI Tutorial."""

from typing import Any, Optional
from fastapi import FastAPI, Path, Query
from fastapi.param_functions import Body
from pydantic import BaseModel

# from dataclasses import dataclass
# @dataclass
# class Item:
#     """Example of Request Body Object."""

#     name: str
#     price: float
#     description: Optional[str] = None
#     tax: Optional[float] = None


class Item(BaseModel):
    """Example of Request Body Object."""

    name: str
    price: float
    description: Optional[str] = None
    tax: Optional[float] = None


class User(BaseModel):
    """Example of User Body Objects."""

    username: str
    full_name: Optional[str] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    """Create an example of an endpoint with a Request body."""
    return item


@app.put("/items/{item_id}")
async def put_item(item_id: int, item: Item, q: Optional[str] = None):
    """Create an example of a request with path, body, and query Parameters.

    Anything defined in the path string is a path parameter.
    Any "complex" type (i.e. not primitive) is a body parameter.
    Any "singular type" (i.e. primitives, incl. str) is a query paramter.
    """
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, max_length=50)):
#     """Example of string length validation with Query type."""
#     results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    """Advanced use cases of Query type."""
    results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(
#         ...,
#         title="The ID of the item to get",
#         ge=0,
#         le=1000,  # Required Path param, '...' makes it required
#     ),  # Path var
#     q: Optional[str] = None,  # Optional Query Param
#     item: Optional[Item] = None  # Optional Body param
# ):
#     """Demonstrate Path type and numeric data."""
#     results: dict[str, Any] = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: int = Body(...)
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results
