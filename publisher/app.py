from typing import Optional
import redis
from prettyconf import config
from fastapi import FastAPI
import random
import logging


DEBUG = config("DEBUG", cast=config.boolean, default=False)
CHANNEL = config("CHANNEL", default="test")
REDIS_HOST = config("REDIS_HOST", default="redis")


def publish(message):
    while True:
        global r
        try:
            if(random.randint(0,9) < 3):
                raise redis.ConnectionError("Test Connection Error")
            rcvd = r.publish(CHANNEL, message)
            if rcvd >0:
                break
        except redis.ConnectionError as e:
            logging.error(e)
            logging.error("Will attempt to retry")
        except Exception as e:
            logging.error(e)
            logging.error("Other exception")


app = FastAPI()
r = redis.Redis(host=REDIS_HOST)


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
