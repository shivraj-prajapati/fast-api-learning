""""
We use BaseModel for data validation, readability, and automatic documentation.
It also simplifies type safety and data serialization, making API development easier.
"""

from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str


@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data


if __name__ == "__main__":
    import uvicorn
uvicorn.run(app, host="127.0.0.1", port=8000)





