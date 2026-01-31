from fastapi import FastAPI
from controllers.deportes_controller import router as deportes_router

app = FastAPI(
    title="API Deportiva",
    description="Consumo de API deportiva externa",
    version="1.0.0"
)

app.include_router(deportes_router, prefix="/api/deportes")
