
from fastapi import FastAPI
from app.api.routes import products, checkout, ai_routes

app = FastAPI(title="Clothing Brand API")

app.include_router(products.router, prefix="/api/products")
app.include_router(checkout.router, prefix="/api/checkout")
app.include_router(ai_routes.router, prefix="/api/ai")

@app.get("/health")
def health():
    return {"status": "ok"}
