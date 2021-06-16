## Docker Build, Push and Deploy on K8s
s2i build . seldonio/seldon-core-s2i-python3:1.6.0 nishkarshraj/lakshika --environment-file=.s2i/environment
docker push nishkarshraj/lakshika
kubectl apply -f deployment.yaml -n jio
kubectl apply -f service.yaml -n jio
kubectl apply -f istio-service.yaml -n jio

## Test Docker container with Curl locally
docker run --rm --name [] -p 9000:9000 -p 5000:5000 -p 6000:6000 []
curl -X POST -H 'Content-Type: application/json' -d '{"data": {"ndarray": ["Hello world this is a test"]}}' http://localhost:9000/api/v1.0/predictions

## Get External IP of service where Istio Ingress is
kubectl get svc -n istio-system

## Test Docker container 
kubectl exec news-5668957fd5-k7knz -n jio -- wget --header='Content-Type:application/json' --post-data='{"data": {"ndarray": ["Hello world this is a test"]}}' -q -O - http://localhost:9000/api/v1.0/predictions

## Test Istio Sidecar proxy of Docker Container
kubectl exec news-5668957fd5-ww22d -c istio-proxy -- curl -X POST -H 'Content-Type: application/json' -d '{"data": {"ndarray": ["Hello world this is a test"]}}' http://news:9000/api/v1.0/predictions

## Hit the virtual Service on External IP endpoint
curl -X POST -H 'Content-Type: application/json' -d '{"data": {"ndarray": ["Hello world this is a test"]}}' http://<External IP>/api/v1.0/predictions
