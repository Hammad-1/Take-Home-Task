from pydantic import BaseModel
from typing import List

# Pydantic model for Product
class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: str = None
    description: str = None
    price: float = None
    category_id: int = None
    created_at: str = None
    updated_at: str = None

class Product(ProductBase):
    id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True