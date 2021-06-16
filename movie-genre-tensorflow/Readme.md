### Steps

```
docker build -t [docker image] .
s2i build . [docker image] [seldon image]
docker run --rm --name [docker container] -p 9000:9000 -p 5000:5000 -p 6000:6000 [seldon image]
curl \
  -F "userid=1" \
  -F "filecomment=This is an image file" \
  -F "image=@/nish.jpeg" \
  http://localhost:9000/api/v1.0/predictions
```
