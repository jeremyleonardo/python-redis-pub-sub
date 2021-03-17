from typing import Optional
import redis
from prettyconf import config
from fastapi import FastAPI


DEBUG = config("DEBUG", cast=config.boolean, default=False)
CHANNEL = config("CHANNEL", default="test")
REDIS_HOST = config("REDIS_HOST", default="redis")


app = FastAPI()


def publish(message):
    r = redis.Redis(host=REDIS_HOST)
    r.publish(CHANNEL, message)


@app.get("/")
async def root(
    message: Optional[str]
    ):
    publish(message or "test message")
    return "OK"
