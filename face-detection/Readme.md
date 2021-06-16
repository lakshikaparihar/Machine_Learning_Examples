```
docker run --rm --name test -p 9000:9000 -p 5000:5000 -p 6000:6000 face
```

```
curl -X POST -H 'Content-Type: application/json' -d '{"data": {"ndarray": ["https://avatars.githubusercontent.com/u/35298207?s=400&u=4f30ea1314276797d0150f338aa20ea64d607e49&v=4"]}}' http://localhost:9000/api/v1.0/predictions
```
