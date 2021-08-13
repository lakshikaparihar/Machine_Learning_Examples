# End-to-End Workflow (ModelDB x MLFlow)

## Start ModelDB Server

```
docker-compose up
```

## Create Model

```
python3 create_model.py
```

## Upload Model in ModelDB Store

```
python3 upload-artifact.py
```

## Fetch Model from ModelDB, Log into Mlflow and Move into Production

```
python3 final-log.py
```

## Dockerization

```
mkdir model_dir/

mv mlruns/0/<run id>/artifacts/<model name>/* model_dir/

docker build -t nish .

docker run --rm -it -p 5000:8080 nish
curl http://127.0.0.1:5000/invocations -H 'Content-Type: application/json' -d '{ 
    "columns": ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age"], 
    "data": [[10, 101, 76, 48, 180, 32.9, 0.171, 63], [0, 137, 40, 35, 168, 43.1, 2.288, 33]]
}'
```
