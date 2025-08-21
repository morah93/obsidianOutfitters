
from fastapi import APIRouter

router = APIRouter()

@router.post("/create")
def create_checkout():
    return {"checkout": "success"}
