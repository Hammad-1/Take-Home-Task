from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.models.inventory import Inventory
from app.schemas.inventory import Inventory
from app.products.repositories import ProductRepo

async def view_inventory_status(low_stock_threshold, db):
    '''
    This method extract inventory status for all products
    '''
    products =  ProductRepo.fetch_all(db)
    inventory_status = []
    if len(products) > 0:
        for product in products:
            quantity = 0
            for inventory in product.inventory:
                quantity += inventory.quantity
                item_status = {
                    "product_name": product.name,
                    "quantity": quantity,
                    "status": "Low Stock" if quantity < low_stock_threshold else "In Stock"
                }
            inventory_status.append(item_status)
    return inventory_status

    raise HTTPException(status_code=404, detail="No Product Found")




