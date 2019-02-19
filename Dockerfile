FROM    python:3.7-alpine3.8

COPY    atest /atest

WORKDIR /atest

RUN     pip install -r requirements.txt