from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from starlette.requests import Request
import random
import os
from api.routes import router  # Make sure this exists and is correctly implemented

app = FastAPI()

# Set up templates directory
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))


# Static files (e.g. CSS, JS, images)
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Game logic
CHOICES = ["rock", "paper", "scissors"]

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("game.html", {"request": request, "result": None})


@app.post("/play/", response_class=HTMLResponse)
async def play(request: Request, user_choice: str = Form(...)):
    computer_choice = random.choice(CHOICES)
    result = determine_winner(user_choice, computer_choice)
    return templates.TemplateResponse("game.html", {
        "request": request,
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    })

# Include additional API routes
app.include_router(router)


