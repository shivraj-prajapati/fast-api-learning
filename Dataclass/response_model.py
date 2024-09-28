from dataclasses import dataclass, field
from typing import List, Union

from fastapi import FastAPI

@dataclass
class Item:
    name : str
    price : float
    tags : List[str] = field(default_factory=list)
    description : Union[str, None] = None
    tax : Union[float, None] = None
    
app = FastAPI()

@app.get("/items/next", response_model=Item)
async def read_next_item():
    return{
        "name": "Milkha Singh",
        "price": 56.1,
        "description": "A coder is rock in real life",
        "tags": ["MuskMelon"],
    }
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8000)        