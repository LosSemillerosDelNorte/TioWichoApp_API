from fastapi import FastAPI
from app.routers import drinks, food

app = FastAPI(title="TioWichoApp API", version="1.0")

# Registrar rutas
app.include_router(drinks.router, prefix="/drinks", tags=["Drinks"])
app.include_router(food.router, prefix="/food", tags=["Food"])

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API de TioWichoApp!"}
