# from fastapi import APIRouter, HTTPException
# from app.data import professionals

# router = APIRouter()

# @router.get("/")
# def get_professionals():
#     return professionals

# @router.get("/{professional_id}")
# def get_professional(professional_id: int):
#     professional = next((p for p in professionals if p["id"] == professional_id), None)
#     if not professional:
#         raise HTTPException(status_code=404, detail="Professional not found")
#     return professional

# @router.post("/")
# def add_professional(professional: dict):
#     professional["id"] = len(professionals) + 1
#     professionals.append(professional)
#     return professional
