from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
"""
Update an item with the given item_id, optional query parameter, and optional item data.
Args:
    item_id (int): The ID of the item to update.
    q (str, optional): An optional query parameter.
    item (Item, optional): An optional item data to update.
Returns:
    dict: A dictionary containing the item_id, and optionally the query parameter and item data.
"""
@app.put("/items/{item_id}")
async def update_item(
    # Annotated is used to provide additional metadata for the parameters, such as validation rules or descriptions.
    
    item_id : Annotated[int, Path(title="The ID of the item to get")],    
    q : str | None = None,
    item : Item | None = None,
):
    results = {"item_id" : item_id}
    if q:
        results.update({"q" : q})
    if item:
        results.update({"item" : item})
    return results
    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)