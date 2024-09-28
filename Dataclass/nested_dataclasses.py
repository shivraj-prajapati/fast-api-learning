from dataclasses import field
from typing import List, Union

from fastapi import FastAPI
from pydantic.dataclasses import dataclass

@dataclass
class Item:
    name : str
    description : Union[str, None] = None
    
@dataclass
class Author:
    name : str
    items : List[Item] = field(default_factory=list)
    
app = FastAPI()

@app.post("/authors/{author_id}/items/", response_model=Author)
async def create_author_items(author_id : str, items : List[Item]):
    return {"name" : author_id, "items" : items}

@app.get("/authors/", response_model=List[Author])
def get_authors():
    return [  # 
        {
            "name": "Tony Stark",
            "items": [
                {
                    "name": "I am iron man",
                    "description": "Stark Industries",
                },
                {"name": "Pepper"},
            ],
        },
        {
            "name": "Thor",
            "items": [
                {
                    "name": "Thor ordinson",
                    "description": "The god of thunder",
                },
                {"name": "Loki"},
                {
                    "name": "Banner",
                    "description": "I am not Banner i am Hulk",
                },
            ],
        },
    ]
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8000)            