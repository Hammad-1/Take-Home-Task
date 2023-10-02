from sqlalchemy.orm import Session

from app.models import products as models
from app.models.inventory import Inventory
from app.schemas import products as schemas

class ProductRepo:
    async def create(db: Session, product: schemas.ProductCreate):
        product = models.Products(name=product.name,price=product.price,description=product.description,category_id=product.category_id)
        db.add(product)
        db.commit()
        # Create an associated inventory record
        inventory = Inventory(quantity=1, product_id=product.id)
        db.add(inventory)
        db.commit()
        db.refresh(product)
        return product

    def fetch_by_id(db: Session, product_id):
        return db.query(models.Products).filter(models.Products.id == product_id).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Products).offset(skip).limit(limit).all()

    def fetch_products_by_catrgory(db: Session, category_id):
        return  db.query(models.Products).filter(models.Products.category_id == category_id).all()

    def delete(db: Session, product_id):
        db_product= db.query(models.Products).filter_by(id=product_id).first()
        db.delete(db_product)
        db.commit()
     
    def update(db: Session, product_data, product):
        for field, value in product_data.dict(exclude_unset=True).items():
            setattr(product, field, value)
        db.commit()
        db.refresh(product)
        return {"msg": "Product Updated Successfully"}