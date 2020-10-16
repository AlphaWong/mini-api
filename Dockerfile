FROM python:alpine
WORKDIR /app
ARG PORT=5000

COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY src /app/src

ENV FLASK_PORT=${PORT}
EXPOSE ${FLASK_PORT}
CMD [ "python3", "src/app.py" ]