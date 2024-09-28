from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    client_port = request.client.port
    method = request.method
    headers = request.headers
    url = request.url
    query_params = request.query_params
    cookies = request.cookies
    http_version = request.scope["http_version"]
    
    data =  {
        "client_host": client_host,
        "client_port": client_port,
        "method": method,
        "headers": dict(headers),
        "url": str(url),
        "query_params": dict(query_params),
        "cookies": cookies,
        "http_version": http_version,
        "item_id": item_id
    }

    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
