from fastapi import APIRouter, HTTPException
from services.deportes_service import DeportesService

router = APIRouter()
service = DeportesService()

@router.get("/ligas")
def obtener_ligas():
    try:
        return service.obtener_ligas_futbol()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
