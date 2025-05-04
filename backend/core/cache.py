import aioredis
import os
import json

redis = aioredis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"), decode_responses=True)

async def check_cache(seed, guess):
    key = f"verdict:{seed}:{guess}"
    return await redis.get(key)

async def store_cache(seed, guess, verdict):
    key = f"verdict:{seed}:{guess}"
    await redis.set(key, verdict, ex=3600)


