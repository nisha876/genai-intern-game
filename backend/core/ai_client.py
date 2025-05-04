import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_ai_verdict(seed, guess):
    prompt = f"Does '{guess}' beat '{seed}' in any game, metaphor, or real-world context? Answer only YES or NO."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.choices[0].message['content'].strip().upper()
    if "YES" in raw and "NO" not in raw:
        return "YES"
    else:
        return "NO"
