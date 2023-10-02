from fastapi import APIRouter, Depends, HTTPException, Query
from . import services
from app.schemas.sales import Sale, Revenue
from db import get_db, engine
from sqlalchemy.orm import Session
from datetime import datetime
from datetime import date

router = APIRouter()

@router.get("/")
async def get_sales(db: Session = Depends(get_db)):
    '''
    Endpoint To Get all Sales
    '''
    return await services.get_sales(db)

@router.get("/filter_sales")
async def filter_sales(
    sale_id: int =  Query(None, description="Filter sales by sales id"),
    product_id: int = Query(None, description="Filter sales by product id"),
    category_id: int = Query(None, description="Filter sales by category id"),
    target_date: date = Query(None, description="Filter salesTarget date"), 
    start_date: date = Query(None, description="Start date to Filter sales"),
    end_date: date = Query(None, description="End date to Filter sales"),
    db: Session = Depends(get_db)
):
    '''
    Endpoint to Filter Sales by sales_id or product_id or category_id or date or date_range
    '''
    if sale_id:
        return await services.get_sale_by_id(sale_id, db)
    elif product_id:
        return await services.get_sales_by_product(product_id, db)
    elif category_id:
        return await services.get_sales_by_category(category_id, db)
    elif target_date:
        return await services.get_sales_by_date(target_date, db)
    elif start_date and end_date:
        return await services.get_sales_by_date_range(start_date, end_date, db)
    else:
        raise HTTPException(status_code=404, detail="please provide valid params") 

@router.get("/revenue")
async def get_revenue(
    period: str = Query(None, description="Time period for revenue please provide value in (daily, weekly, monthly, annual)"),
    date: date = Query(None, description="Enter Date for Daily or Weekly revenue"),
    year: int = Query(0, description="Year for monthly or annual revenue"),
    month: int = Query(0, description="Month for monthly revenue"),
    db: Session = Depends(get_db)
):
    '''
    Endpoint To Get Revenue based on the selected time period
    '''
    # if date is None:
    #     raise HTTPException(status_code=400, detail="Please provide date")

    if period == "daily":
        if date:
            return await services.get_daily_revenue(date, db)
        else:
            raise HTTPException(status_code=400, detail="Please provide date")
    elif period == "weekly":
        if date:
            return await services.get_weekly_revenue(date, db)
        else:
            raise HTTPException(status_code=400, detail="Please provide date")
    elif period == "monthly":
        if (year and month != 0) and month <= 12 :
            return await services.get_monthly_revenue(year, month, db)
        else:
            raise HTTPException(status_code=404, detail="please provide valid value of month and year")  
    elif period == "annual":
        # You can parse the selected date to extract the year
        if year != 0:
            return await services.get_annual_revenue(year, db)
        else:
            raise HTTPException(status_code=404, detail="please provide value of year")
    else:
        raise HTTPException(status_code=400, detail="Invalid time period")