from fastapi import FastAPI

app = FastAPI()

@app.get("/app")
def read_main():
    return {"message": "Hello World from main app 1"}

subapi = FastAPI()

# if you want to access this function so you need to request on this path (http://127.0.0.1:8000/subapi/sub)
@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API 2"}

app.mount("/subapi", subapi)

if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)