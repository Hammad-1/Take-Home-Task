from fastapi import FastAPI
from app.products.controllers import router as product_router
from app.sales.controllers import router as sales_router
from app.inventory.controllers import router as inventory_router
from db import Base, engine

app = FastAPI(title="Take Home Task")

Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(sales_router, prefix="/sales", tags=["Sales"])
app.include_router(inventory_router, prefix="/inventory", tags=["Inventory"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
