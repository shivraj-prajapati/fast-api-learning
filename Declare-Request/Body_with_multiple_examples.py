from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

#Here we are declare multiple examples for inserting multiple data 
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Algo",
                    "description": "A nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
                {
                    "name": "Hit",
                    "price": "35.4",
                },
                {
                    "name": "Twit",
                    "price": "On two three",
                },
            ],
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results