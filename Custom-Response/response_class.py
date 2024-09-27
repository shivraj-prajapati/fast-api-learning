from typing import Any
import orjson
from fastapi import FastAPI, Response

app = FastAPI()

class CustomORJSONResponse(Response):
    media_type = "application/type"
    
    def render(self, content : Any) -> bytes:
        assert orjson is not None, "orjson must be installed"  
        return orjson.dumps(content, option=orjson.OPT_INDENT_2)
    
@app.get("/", response_class=CustomORJSONResponse)
async def main():
    return {"message": "Hello World"}    

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8080)
    