from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.models.inventory import Inventory
from app.schemas.inventory import Inventory
from app.products.repositories import ProductRepo
from . repositories import InventoryRepo

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

async def update_inventory(product_id, quantity, db):
    return InventoryRepo.update_inventory_by_product(db, product_id, quantity)

async def get_inventory_logs_by_product_id(product_id, db):
    inventory_logs = InventoryRepo.get_inventory_logs_by_product_id(db, product_id)
    if len(inventory_logs) > 0:
        return inventory_logs
    else:
        raise HTTPException(status_code=404, detail="No logs found of inventory update for this product")
