# Python Redis Pub/Sub

This is a sample app for python Redis pub/sub with FastAPI as pub.

Something to reconsider before using redis pub/sub with multiple sub workers : 
- https://stackoverflow.com/questions/7196306/competing-consumer-on-redis-pub-sub-supported
- https://stackoverflow.com/questions/32037803/redis-pub-sub-ack-nack

You might need load balancer for multiple worker/instance of subscriber because multiple instance of the same subscriber will all consume the message.

## Run

Build and start the services:

```bash
docker-compose build
docker-compose up
```
