from fastapi import APIRouter, Depends, HTTPException
from . import services
from app.schemas.products import ProductCreate, Product, ProductUpdate
from db import get_db, engine
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=Product, status_code=201)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return await services.create_product(product, db)

@router.get("/{product_id}/", response_model=Product)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    return await services.get_product(product_id, db)

@router.get("/")
async def read_products(db: Session = Depends(get_db)):
    return await services.get_products(db)

@router.patch("/{product_id}")
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    return services.update_product(product_id, product, db)

@router.delete("/{product_id}/")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return services.delete_product(product_id, db)
