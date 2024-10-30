from fastapi import FastAPI, HTTPException
from .schemas import TextInput, SentimentOutput

from transformers import pipeline

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis
from functools import lru_cache
from contextlib import asynccontextmanager


@lru_cache(maxsize=1)
def get_sentiment_analyzer():
    """Initialize and cache the sentiment analysis pipeline"""
    return pipeline("sentiment-analysis")

@asynccontextmanager
async def startup(_: FastAPI):
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="sentiment-cache")
    yield

app = FastAPI(lifespan=startup)


@app.get("/")
async def root():
    return {"message": "This is an example API"}

@app.post("/predict-sentiment")
# @cache(expire=3600)
async def predict_sentiment(input: TextInput) -> SentimentOutput:
    try: 
        sentiment_analyzer = get_sentiment_analyzer()
        result = sentiment_analyzer(input.text)
        sentiment = result[0]
        return SentimentOutput(
            label=sentiment["label"],
            score=sentiment["score"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing request") from e
