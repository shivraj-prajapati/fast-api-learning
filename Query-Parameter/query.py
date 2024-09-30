from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Laptop"},
    {"item_name": "Smartphone"},
    {"item_name": "Headphones"},
    {"item_name": "Tablet"},
    {"item_name": "Smartwatch"},
    {"item_name": "Keyboard"},
    {"item_name": "Mouse"},
    {"item_name": "Monitor"},
    {"item_name": "Printer"},
    {"item_name": "Camera"}
]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8080)
