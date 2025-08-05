from fastapi import FastAPI
from app.models.item import Item

router = FastAPI()

@router.post('/items')
def create_item(item:Item):
    return {
        "item" : item,
        "status":"Item Added"
    }