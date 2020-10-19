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
kubectl apply -k . --dry-run=client -o yaml
```

# replace key from dev-key via 
```console
MY_KEY=MY_KEY envsubst '${MY_KEY}' < ./dev-key.env
```

# reference
1. https://github.com/docker/login-action
1. https://github.com/marketplace/actions/build-and-push-docker-images
1. https://docs.github.com/en/free-pro-team@latest/packages/getting-started-with-github-container-registry/migrating-to-github-container-registry-for-docker-images#authenticating-with-the-container-registry
1. https://kubectl.docs.kubernetes.io/pages/app_management/secrets_and_configmaps.html
1. https://unix.stackexchange.com/a/294400