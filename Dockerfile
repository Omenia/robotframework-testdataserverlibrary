FROM    python:3.7-alpine3.8

COPY atest atest/
COPY requirements.txt /

RUN     pip3 install -r requirements.txt