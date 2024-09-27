from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

# app = FastAPI(default_response_class=ORJSONResponse)
app = FastAPI()

@app.get("/")
async def get_message():
    return [{"message" : "Hello rocky.!"},{"message" : "How are You"}]

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8080)
