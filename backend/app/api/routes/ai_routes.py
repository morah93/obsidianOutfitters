
from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
def chat_ai():
    return {"response": "Hello from AI chat!"}

@router.get("/recommendations")
def recommendations():
    return {"products": []}
