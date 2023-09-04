# interns-db

This is a study case on how to approach the container creation and architecture for FastAPI webapp as a DevOps engineer using an nginx reverse proxy to the Python backend and a postgres DB for persisting data.

This app works in conjunction with repos

*interns-backend-api
*interns-webserver

1. Interns DB should get started first
2. Interns Backend API should get started second
3. Lastly, we start interns Webserver


### Step #1 to run Interns DB
1. First start minikube on your local by typing
```
minikube start
```

2. Then, run a minikube mount on the data directory from this same repo :
```
cd data
DIR=$(pwd)
minikube mount $DIR:$DIR
```
3. Deploy kubernetes deployment and services
```
kubectl apply -f .
```