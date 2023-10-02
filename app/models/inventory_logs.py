from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from db import Base

class InventoryLogs(Base):
    __tablename__ = "inventory_logs"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    update_quantity = Column(Integer)
    updated_at = Column(DateTime, default=datetime.utcnow)
