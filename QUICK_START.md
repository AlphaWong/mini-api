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