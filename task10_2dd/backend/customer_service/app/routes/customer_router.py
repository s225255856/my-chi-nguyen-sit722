from fastapi import APIRouter

customer_router = APIRouter()

@customer_router.get("/")
async def root():
    return {"message": "Welcome to the Customer Service!"}