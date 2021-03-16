
## Run

Build and start the services:

```bash
# Build the input and output images
docker-compose build

# Start all services
docker-compose up
```

Now you can send a request to the input service by querying port 5000 on the
host:

```bash
curl 'localhost:5000/?message=foobar'
```

You will see the message being printed in the Docker Compose logs.
