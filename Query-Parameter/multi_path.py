from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id, "status": "available"}

    if q:
        item.update({"search_query": q})

    if not short:
        item.update({
            "description": "This item is highly rated and offers great value for money. It's one of the top-selling products!"
        })

    return item

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8080)
