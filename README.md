#  ELK stack demo app for checking metrics and indices
This is a demo application with a static html form running in nginx that reverse proxies into a FastAPI backend with a Postgres database running in Kubernetes. 

The purpose of this app is to run experiments and learn ELK version 8+ running in kubernetes. [This repo|https://github.com/jcroyoaun/kodekloud-elk-k8s)] has the instructions for installing ELK with a simple strategy to ship all logs using filebeat into logstash for a single node kubernetes cluster. 


to install the demo app, simply do

```bash
helm upgrade --install elk-demo .
```
