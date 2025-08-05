from fastapi import FastAPI,Request,Header,Response
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def read_root():
    return {"message":"Welcome to root page"}

@app.get('/headers')
def headers(request:Request):
    return {
        "headers" : dict(request.headers)
    }

class Item(BaseModel):
    name:str
    price:float

@app.post('/items')
def create_item(item:Item):
    return {
        "name" : item.name,
        "price": item.price,
        "status" : "Item recieved successfully"
    }