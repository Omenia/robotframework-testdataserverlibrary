FROM    python:3.7-alpine3.8

COPY atest atest/
COPY requirements.txt /

RUN     pip install -r requirements.txt