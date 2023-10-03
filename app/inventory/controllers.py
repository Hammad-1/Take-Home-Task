from fastapi import APIRouter, Depends, HTTPException
from . import services
from db import get_db, engine
from sqlalchemy.orm import Session

router = APIRouter()
@router.get("/inventory-status")
async def view_inventory_status(
    low_stock_threshold: int = 10,
    db: Session = Depends(get_db)
):
    '''
    Endpoint to view current inventory status for all products, including low stock alerts.
    '''
    return await services.view_inventory_status(low_stock_threshold, db)

@router.patch("/")
async def update_inventory(
    product_id : int = 0,
    quantity : int = 0,
    db: Session = Depends(get_db)
):
    '''
    Endpoint to Update Inventory of a product
    '''
    if product_id and quantity != 0:
        return await services.update_inventory(product_id, quantity, db)
    raise HTTPException(status_code=400, detail="Please provide product_id and quantity")

@router.get("/track-inventory-update")
async def get_inventory_logs(product_id : int = 0, db: Session = Depends(get_db)):
    '''
    Endpoint to track inventory logs
    '''
    if product_id != 0:
        return await services.get_inventory_logs_by_product_id(product_id, db)
    raise HTTPException(status_code=400, detail="Please provide product_id and quantity")