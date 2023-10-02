from sqlalchemy.orm import Session

from app.models.sales import Sale
from app.schemas import sales as schemas
from datetime import timedelta

class SalesRepo:

    def fetch_by_id(db: Session, sales_id):
        return db.query(Sale).filter(Sale.id == sales_id).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Sale).offset(skip).limit(limit).all()

    def fetch_by_product_id(db: Session, product_id):
        return db.query(Sale).filter(Sale.product_id == product_id).all()

    def filter_sales_by_date_range(db: Session, start_date, end_date):
        sales = db.query(Sale).filter(Sale.sale_date >= start_date, Sale.sale_date <= end_date).all()
        return sales
    
    def filter_sales_by_date(db: Session, target_date):
        sales = db.query(Sale).filter(Sale.sale_date >= target_date, Sale.sale_date < target_date + timedelta(days=1)).all()
        return sales