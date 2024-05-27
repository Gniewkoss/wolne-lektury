from fastapi import FastAPI
from app.database import engine, Base
from app.endpoints import books, categories

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books.router)
app.include_router(categories.router)
