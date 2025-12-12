from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

app = FastAPI()
items = {}

@app.get("/")
def root():
    return {"message": """Use /items{name} to see the item you added.
            Use /items to see the entire list of items you have added."""}

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def create_item(item: Item):
    items[item.name] = item
    return {"message": f"You added {item.name}"}


@app.get("/items/{name}")
def get_item(name: str):
    return items.get(name, {"error": "Item not found"})


