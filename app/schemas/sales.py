from pydantic import BaseModel
from typing import List

# Pydantic model for Sale
class SaleBase(BaseModel):
    quantity: int
    revenue: float

class SaleCreate(SaleBase):
    pass

class Revenue():
    date: str
    revenue: float

class Sale(SaleBase):
    id: int
    sale_date: str

    class Config:
        orm_mode = True