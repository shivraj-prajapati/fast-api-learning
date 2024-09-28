from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

#This middleware is allowed only 2 urls which are given below
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["w3schools.com", "127.0.0.1"]
)

@app.get("/")
async def main():
    return {"message" : "Hello Word"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)