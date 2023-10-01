from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.products import Products
from app.schemas.products import ProductCreate, ProductUpdate
from . repositories import ProductRepo
from db import get_db, engine
from typing import List,Optional
from fastapi.encoders import jsonable_encoder

async def create_product(product_request: ProductCreate, db):
    """
    Create Product and store it in the database
    """
    product = jsonable_encoder(await ProductRepo.create(db=db, product=product_request))
    return product
    
async def get_product(product_id: int, db):
    """
    Get the Product with the given ID provided by User stored in database
    """
    product = ProductRepo.fetch_by_id(db,product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found with the given ID")
    return jsonable_encoder(product)
    
async def get_products(db):
    """
    Get all the Products stored in database
    """
    products = ProductRepo.fetch_all(db)
    if len(products) == 0:
        raise HTTPException(status_code=404, detail="No Product Found")
    return products

def update_product(product_id: int, product_data: ProductUpdate, db):
    """
    Update Product stored in the database
    """
    product = ProductRepo.fetch_by_id(db, product_id)
    if product:
        return ProductRepo.update(db=db, product_data=product_data, product=product)
    else:
        raise HTTPException(status_code=400, detail="Item not found with the given ID")
    

def delete_product(product_id: int, db):
    product = ProductRepo.fetch_by_id(db,product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found with the given ID")
    ProductRepo.delete(db,product_id)
    return "Product deleted successfully!"
