# Mini API

## Scenario
We want to build a simple API interface prototype

## Necessary Environment Variables
- `API_KEY`: The API key is hardcoded at the moment, you can generate your own API key. The product API shall parse this key upon request from the header `X-API-KEY` and reject the rest without the header
- `FLASK_PORT`: Default 5000, this is the port which the flask application will be bound to

## Steps
1. Fork this repository
2. Create branch from a previous commit id of master: `git checkout -b dev 9a09dc2f77e2551bb764c86f9269543442007606`
3. Add the following piece of code on dev and merge the branch to main via pull request, for the sake of health-checking:
```python
@app.route("/health")
def health_check():
    return "", 200
```
4. Breifly read through the source code and build the docker image. Push this to your docker repository. If you may, please leave us a simple script in `hack/` for testing the docker image locally
5. Gain acces to the Kubernetes cluster. Deploy your images from docker repository. (_Please leave your deployment files in `config/`_)
6. After ensuring the functionality of your application on Kubernetes, please add the healthcheck functionallity using the `/health` endpoint you have added, to ensure the application is alive
7. To increase scalability of the application, please avoid hard-coding your `API_KEY` and `FLASK_PORT`. Store these into **secrets** and **configmaps** respectively
8. Deploy gitops tools, e.g., `fluxcd` or `argocd` to the cluster, so that whenever you have pushed a new image to docker repository, the latest version of image will be deployed automatically
9. build a docker CI pipeline to build and upload the docker image when there is a git push or merge. You can use any service as you like

## Outcome:
In your submission we would like to have your repository structurized like this:

```
.
|
| --- src/
| --- config/
| --- hack/
| --- Dockerfile
| --- requirements.txt
| --- README.md
```

`src/`: Containing scripts

`config/`: The configuration files, possibly including your Dockerfile, kubernetes, CI/CD configuration files

`hack/`: (optional) some random quick-hack one-liners you find useful and convenient to use