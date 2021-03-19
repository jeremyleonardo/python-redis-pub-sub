import time
import redis
from prettyconf import config


CHANNEL = config("CHANNEL", default="test")
REDIS_HOST = config("REDIS_HOST", default="redis")


def main():
    r = redis.Redis(host=REDIS_HOST, decode_responses=True)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe(CHANNEL)
    while True:
        try:
            message = p.get_message()
        except redis.ConnectionError:
            # Do reconnection attempts here such as sleeping and retrying
            time.sleep(3)
            p = r.pubsub()
            p.subscribe(CHANNEL)
        if message:
            print(message)
            print(message['data'])
            time.sleep(0.001)


if __name__ == "__main__":
    print("Start listening...")
    try:
        main()
    except KeyboardInterrupt:
        pass
