from typing import List, Optional
from pydantic import BaseModel

# Schematy dla kategorii
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode: True

# Schematy dla książek
class BookBase(BaseModel):
    title: str

class BookCreate(BookBase):
    authors: List[str]
    epochs: List[str]
    genres: List[str]
    kinds: List[str]

class Book(BookBase):
    id: int
    authors: List[Category]
    epochs: List[Category]
    genres: List[Category]
    kinds: List[Category]

    class Config:
        orm_mode: True
