# Mini API
Scenario: We want to build a simple API interface providing CRUD functions, where the API is actually linked to a MongoDB instance for data storage and query at the same time. Please follow the steps in the following:

## Steps
- Fork / Clone this repository
- Breifly read through the source code and build the docker image. Push this to your docker repository. If you may, please leave us a simple script in `hack/` for testing the docker image locally
- Gain acces to the Kubernetes cluster. Deploy your images from docker repository. (_Please leave your deployment files in `config/`_)
- After ensuring the functionality of your application on Kubernetes, please add the healthcheck functionallity to ensure the application is alive
- Deploy gitops tools, e.g., `fluxcd` or `argocd` to the cluster, so that whenever you have pushed a new image to docker repository, the latest version of image will be deployed automatically
- build a docker CI pipeline to build and upload the docker image when there is a git push or merge. You can use any service as you like

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