from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from db import Base

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    last_updated = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", back_populates="inventory")