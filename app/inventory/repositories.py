from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.inventory import Inventory
from app.models.inventory_logs import InventoryLogs
from datetime import datetime

class InventoryRepo:
    def update_inventory_by_product(db: Session, product_id, quantity):
        inventory =  db.query(Inventory).filter(Inventory.product_id == product_id).first()
        if not inventory:
            raise HTTPException(status_code=404, detail="Inventory not found for this product")
        inventory.quantity += quantity
        # Create an inventory log to track the change
        log_entry = InventoryLogs(
        product_id=product_id,
        update_quantity=quantity,
        updated_at=datetime.utcnow()
        )
        db.add(log_entry)
        db.commit()
        db.refresh(inventory)
        return {"msg": "Inventory Updated Successfully"}
        
    def get_inventory_logs_by_product_id(db: Session, product_id):
        inventory_logs =  db.query(InventoryLogs).filter(InventoryLogs.product_id == product_id).all()
        return inventory_logs


        
