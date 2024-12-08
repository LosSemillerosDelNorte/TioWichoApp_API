# from fastapi import APIRouter, HTTPException
# from app.data import users

# router = APIRouter()

# @router.get("/")
# def get_users():
#     return users

# @router.get("/{user_id}")
# def get_user(user_id: int):
#     user = next((u for u in users if u["id"] == user_id), None)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# @router.post("/")
# def add_user(user: dict):
#     user["id"] = len(users) + 1
#     users.append(user)
#     return user
