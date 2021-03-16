import redis
from flask import Flask
from flask import request
from prettyconf import config


DEBUG = config("DEBUG", cast=config.boolean, default=False)
CHANNEL = config("CHANNEL", default="test")
REDIS_HOST = config("REDIS_HOST", default="redis")


def publish(message):
    r = redis.Redis(host=REDIS_HOST)
    r.publish(CHANNEL, message)


app = Flask(__name__)


@app.route("/")
def notify():
    message = request.args.get("message", None)
    publish(message or "test message")
    return "OK"
