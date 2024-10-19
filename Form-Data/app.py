from fastapi import FastAPI, Form
from typing import Annotated

app = FastAPI()

# Define a POST endpoint for the login route
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    # Return the username and password as a JSON response
    return {"username": username, "password": password}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)