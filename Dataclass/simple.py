from dataclasses import dataclass
from typing import Union

from fastapi import FastAPI
"""
dataclass FastAPI me ek lightweight alternative hai
jab aapko sirf data structure define karna ho bina validation ke.
"""


@dataclass
class Item:
    name : str
    price : float
    description : Union[str, None] = None
    tax : Union[float, None] = None
    
app = FastAPI()

@app.post("/items")
async def create_item(item : Item):
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8000)        