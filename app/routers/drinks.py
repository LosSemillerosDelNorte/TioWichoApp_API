from fastapi import APIRouter, HTTPException
from app.data import bebidas_menu

router = APIRouter()

# Endpoint para obtener todas las categorías de bebidas
@router.get("/")
def get_all_drinks():
    return bebidas_menu

# Endpoint para obtener bebidas por categoría
@router.get("/{category}")
def get_drinks_by_category(category: str):
    if category not in bebidas_menu:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return bebidas_menu[category]
