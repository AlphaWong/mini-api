from flask import Flask
from os import environ
from time import sleep

app = Flask(__name__)
port = environ.get('FLASK_PORT', 5000)


@app.route('/')
def hello_world():
    sleep(2)
    return 'Hello, World!'


@app.route("/health")
def health_check():
    return "", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)