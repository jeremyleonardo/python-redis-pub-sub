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
async def root():
    return "OK"


@app.post("/messaging/send")
async def send_message(
    message: Optional[str] = ''
    ):
    if message != '':
        publish(message)
    else:
        publish("test message")
    return {"status": "succes"}
