from flask import Flask, request
from os import environ
from time import sleep
from sys import exit

app = Flask(__name__)
port = environ.get('FLASK_PORT', 5000)
api_key = environ.get('API_KEY')


@app.route('/', methods=['GET'])
def hello_world():
    sleep(5)
    if ('X-API-KEY' not in request.headers or request.headers['X-API-KEY'] != api_key ):
        return 'Unauthorized', 401
    else:
        return 'Hello, World!', 200


@app.route("/health")
def health_check():
    return "", 200


if __name__ == '__main__':
    if (api_key is None):
        print('Please set the environment variable $API_KEY !')
        exit(1)
    else:
        app.run(host='0.0.0.0', port=port)