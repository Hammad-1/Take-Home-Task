from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from db import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    sale_date = Column(DateTime, default=datetime.utcnow)
    revenue = Column(Float)

    product = relationship("Products", back_populates="sales")