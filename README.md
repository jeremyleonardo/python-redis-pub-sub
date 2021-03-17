# Python Redis Pub/Sub

This is a sample app for python Redis pub/sub with FastAPI as pub.

Something to reconsider before using redis pub/sub with multiple sub workers : https://stackoverflow.com/questions/32037803/redis-pub-sub-ack-nack

## Run

Build and start the services:

```bash
docker-compose build
docker-compose up
```