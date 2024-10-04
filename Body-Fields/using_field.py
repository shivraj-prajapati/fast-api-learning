from typing import Annotated
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., description="The name of the item")
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = Field(default=None, description="The tax of the item")
    sku: str = Field(
        ..., min_length=8, max_length=12, description="Stock Keeping Unit, must be between 8 and 12 characters"
    )
    quantity: int = Field(
        ..., ge=1, description="Quantity must be an integer greater than or equal to 1"
    )
    is_available: bool = Field(
        default=True, description="Availability of the item"
    )

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)