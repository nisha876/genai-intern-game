import re

BANNED_WORDS = {"badword1", "badword2"}

def is_clean(guess: str) -> bool:
    guess_lower = guess.lower()
    return not any(bad in guess_lower for bad in BANNED_WORDS)
# backend/core/moderation.py

def moderate_guess(guess: str) -> bool:
    """
    A basic moderation function.
    For now, just blocks obviously bad words. In real-world use, integrate OpenAI moderation.
    """
    banned_words = {"badword", "nonsense", "💩"}  # Extend this list as needed
    return guess.lower() not in banned_words

