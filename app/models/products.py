from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from . categories import Categories

from db import Base

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(250))
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category = relationship("Categories", back_populates="products")
    sales = relationship("Sale", back_populates="product")  # Define the relationship with Sale model

