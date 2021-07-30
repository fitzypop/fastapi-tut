"""FastAPI Tutorial - Declare Request Example Data."""

from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


# class Item(BaseModel):
#     """Example of Item object."""

#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

#     class Config:
#         """Example of Pydantic Schema Customization Example."""

#         schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2,
#             }
#         }


# class Item(BaseModel):
#     """Example of Item object, and Field example arguments."""

#     name: str = Field(..., example="Foo")
#     description: Optional[str] = Field(None, example="A very nice item")
#     price: float = Field(..., example=35.4)
#     tax: Optional[float] = Field(None, example=3.2)


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     """Update Item Endpoint."""
#     results = {"item_id": item_id, "item": item}
#     return results


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item = Body(
        ...,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
