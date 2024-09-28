from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

# Middleware to redirect HTTP to HTTPS

app.add_middleware(HTTPSRedirectMiddleware)

@app.get("/")
async def main():
    return {"message" : "hello World"}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8000)