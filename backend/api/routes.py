from fastapi import APIRouter, Request
from core.game_logic import GameManager
from fastapi import HTTPException
from pydantic import BaseModel


router = APIRouter()
game = GameManager()

# ✅ Define the request model
class GuessInput(BaseModel):
    guess: str
    seed: str = "Rock"  # optional, defaults to "Rock"

@router.post("/guess")
async def make_guess(request: Request):
    body = await request.json()
    return await game.handle_guess(body)




@router.get("/history")
def get_history():
    return game.get_history()

@router.get("/score")
def get_score():
    return game.get_score()

@router.post("/reset")
def reset_game():
    game.reset()
    return {"message": "Game reset"}