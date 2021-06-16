## Docker Build

```
s2i build . seldonio/seldon-core-s2i-python3:1.6.0 [image name] --environment-file=.s2i/environment
docker push nishkarshraj/lakshika
```

## Test Docker container with Curl locally

```
docker run --rm --name [container name] -p 9000:9000 -p 5000:5000 -p 6000:6000 [image name]
curl -X POST -H 'Content-Type: application/json' -d '{"data": {"ndarray": ["Hello world this is a test"]}}' http://localhost:9000/api/v1.0/predictions
```