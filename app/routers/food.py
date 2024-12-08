from fastapi import APIRouter, HTTPException
from app.data import menu

router = APIRouter()

# Endpoint para obtener todas las categorías de comida
@router.get("/")
def get_all_food():
    return menu

# Endpoint para obtener comida por categoría
@router.get("/{category}")
def get_food_by_category(category: str):
    if category not in menu:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return menu[category]
