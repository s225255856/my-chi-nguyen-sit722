from fastapi import APIRouter

order_router = APIRouter()

@order_router.get("/")
async def root():
    return {"message": "Welcome to the Order Service!"}