FROM python:alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY src /app/src
CMD [ "python3", "src/app.py" ]