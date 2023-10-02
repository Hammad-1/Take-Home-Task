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
