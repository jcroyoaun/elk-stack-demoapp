#  ELK stack demo app for checking metrics and indices

to install it simply do

```bash
helm upgrade --install elk-demo .
```

If backend doesn't work

```
kubectl rollout restart deployment elk-demo-backend-api -n elk-demo
```
