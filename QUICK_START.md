![build-docker-image](https://github.com/AlphaWong/mini-api/workflows/build-docker-image/badge.svg)

# start
```console
pipenv install -r ./requirements.txt
pipenv run python ./src/app.py
```

# generate api key
```console
pwgen -sy 20 1
```

# build image in local
```console
docker build . -t mini-api:0.0.0
```

# run docker image in local
```console
# replace MY_KEY with your own key
docker run -e API_KEY="MY_KEY" -p 8080:5000 mini-api:0.0.0
```

# kustomize dry-run
```console
kubectl apply -k ./config --dry-run=client -o yaml
```

# replace key with envsubst
```console
MY_KEY=MY_KEY envsubst '${MY_KEY}' < ./dev-key.env
```

# Minikube issue
https://github.com/kubernetes/minikube/issues/7344
```console
minikube start --vm-driver=hyperkit
```

# expose LoadBalancer in minikube
```console
minikube service mini-api-service --url
```

# visit argocd without domain
```console
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

# password
```console
export PASSWORD=$(kubectl get pods -n argocd -l app.kubernetes.io/name=argocd-server -o name | cut -d'/' -f 2)
account: admin
password: $PASSWORD
```

# replace the `MY_KEY`
```yaml
# kustomization.yaml
secretGenerator:
  - name: dev.key
    literals:
      - API_KEY=MY_KEY
```

# expose the service at live with `port-forward`
As nginx-ingress controller and `LoadBalancer` cannot get any external ip.
```console
kk port-forward mini-api-service -p 8888:8080
```
## postman connection for testing
postman collection: https://www.getpostman.com/collections/b13f03bf0882d3f7397c

# screenshot
![preview](https://upload.cc/i1/2020/10/20/1K9FTv.png)

# docker tagging bash
1. https://github.com/marketplace/actions/docker-buildx
1. https://github.com/crazy-max/ghaction-docker-meta
1. https://github.com/docker/build-push-action/blob/b072fc7faeea2e4a6cae4636dadbd68b9deca04b/.github/workflows/example.yml

# github action multiline issue
1. https://github.com/actions/toolkit/issues/403#issuecomment-671076570

# reference
1. https://github.com/docker/login-action
1. https://github.com/marketplace/actions/build-and-push-docker-images
1. https://docs.github.com/en/free-pro-team@latest/packages/getting-started-with-github-container-registry/migrating-to-github-container-registry-for-docker-images#authenticating-with-the-container-registry
1. https://kubectl.docs.kubernetes.io/pages/app_management/secrets_and_configmaps.html
1. https://unix.stackexchange.com/a/294400
1. https://github.com/kubernetes-sigs/kustomize/issues/2704
1. https://github.com/kubernetes-sigs/kustomize/blob/master/examples/transformerconfigs/crd/README.md
1. https://github.com/kubernetes-sigs/kustomize/issues/1250#issuecomment-505455209
1. https://github.com/kubernetes/minikube/issues/7344#issuecomment-688179776

# question?
ping me via `wck.alpha@gmail.com`
