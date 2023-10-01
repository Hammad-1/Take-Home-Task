from fastapi import HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from typing import List,Optional
from sqlalchemy.orm import Session
from datetime import datetime, timedelta


from app.models.sales import Sale
from app.schemas.sales import Sale
from . repositories import SalesRepo
from app.products.repositories import ProductRepo

from db import get_db, engine

async def get_sales(db):
    """
    Get all the Sales stored in database
    """
    sales = SalesRepo.fetch_all(db)
    if len(sales) == 0:
        raise HTTPException(status_code=404, detail="No Sale Found")
    return sales

async def get_sale_by_id(sale_id, db):
    """
    Get the Sale with the given ID provided by User stored in database
    """
    sale = SalesRepo.fetch_by_id(db, sale_id)
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found with the given ID")
    return jsonable_encoder(sale)

async def get_sales_by_product(product_id, db):
    """
    Filter Sales with the given product ID provided by User stored in database
    """
    sales = SalesRepo.fetch_by_product_id(db, product_id)
    if len(sales) == 0:
        raise HTTPException(status_code=404, detail="No Sale Found with this product_id")
    return sales

async def get_sales_by_date(target_date: datetime, db):
    """
    Filter Sales with given date provided by User stored in database
    """
    sales = SalesRepo.filter_sales_by_date(db, target_date)
    if len(sales) == 0:
        raise HTTPException(status_code=404, detail="No Sale Found on this date")
    return sales

async def get_sales_by_date_range(start_date, end_date, db):
    """
    Filter Sales with given date range provided by User 
    """
    sales = SalesRepo.filter_sales_by_date_range(db, start_date, end_date)
    if len(sales) == 0:
        raise HTTPException(status_code=404, detail="No Sale Found within date range")
    return sales

async def get_sales_by_category(category, db):
    """
    Filter Sales with the given Category provided by User stored in database
    """
    total_sales = []
    products = ProductRepo.fetch_products_by_catrgory(db, category)
    if len(products) == 0:
        raise HTTPException(status_code=404, detail="No Product Found with this category_id")
    for product in products:
        product_sales = SalesRepo.fetch_by_product_id(db, product.id)
        if len(product_sales) == 0:
            pass
        total_sales.append(product_sales)

    if len(total_sales) == 0:
        raise HTTPException(status_code=404, detail="No Sale Found with this category")
    return total_sales

async def get_daily_revenue(start_date, db):
    '''
    Calculate sum of daily revenue of given date
    '''
    end_date = start_date + timedelta(days=1)
    daily_revenue_sales =  SalesRepo.filter_sales_by_date_range(db, start_date, end_date)
    daily_revenue = sum(sale.revenue for sale in daily_revenue_sales)
    return {"date": start_date, "revenue": daily_revenue}

async def get_weekly_revenue(start_date, db):
    '''
    Calculate sum of daily revenue of given date
    '''
    end_date = start_date + timedelta(days=7)
    weekly_revenue_sales =  SalesRepo.filter_sales_by_date_range(db, start_date, end_date)
    weekly_revenue = sum(sale.revenue for sale in weekly_revenue_sales)
    return {"date": start_date, "revenue": weekly_revenue}

async def get_monthly_revenue(year, month, db):
    '''
    Calculate sum of monthly revenue 
    '''
    next_month = month + 1 if month < 12 else 1
    next_year = year + 1 if month == 12 else year
    start_date = datetime(year, month, 1)
    end_date = datetime(next_year, next_month, 1)
    monthly_revenue_sales =  SalesRepo.filter_sales_by_date_range(db, start_date, end_date)
    monthly_revenue = sum(sale.revenue for sale in monthly_revenue_sales)
    return {"date": start_date, "revenue": monthly_revenue}

async def get_annual_revenue(year, db):
    '''
    Calculate sum of annual revenue 
    '''
    next_year = year + 1
    start_date = datetime(year, 1, 1)
    end_date = datetime(next_year, 1, 1)
    annual_revenue_sales =  SalesRepo.filter_sales_by_date_range(db, start_date, end_date)
    annual_revenue = sum(sale.revenue for sale in annual_revenue_sales)
    return {"date": start_date, "revenue": annual_revenue}