from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
    #This Schema is help to show the example in the Swagger UI
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Rocky",
                    "description": "Enter Here Description",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }
    
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)