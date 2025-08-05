from fastapi import FastAPI
from app.routes import items

app = FastAPI()

# Registering routes
app.include_router(items.router)