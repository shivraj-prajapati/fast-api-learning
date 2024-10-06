from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl, EmailStr

app = FastAPI()

# Define a model for Image with URL and name fields
class Image(BaseModel):
    url: HttpUrl
    name: str

# Define a model for Item with various fields including nested Image
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None
    stock: int
    seller_email: EmailStr

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):

    results = {"item_id": item_id, "item": item}
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)