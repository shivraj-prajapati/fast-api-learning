from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/items/decorator", status_code=201)
async def create_item_decorator(name: str):
    return {"name": name}

@app.post("/items/status_module", status_code=status.HTTP_201_CREATED)
async def create_item_status_module(name: str):
    return {"name": name}


@app.post("/items/json_response")
async def create_item_json_response(name: str):
    return JSONResponse(content={"name": name}, status_code=201)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)