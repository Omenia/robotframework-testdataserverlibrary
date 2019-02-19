FROM    python:3.7.2-stretch

COPY    . /

WORKDIR /

RUN     pip3 install -r requirements.txt

WORKDIR /atest

CMD     python3 -m robot -P . -d output -v tds_host:$TDS_HOST -v tds_port:$TDS_PORT $ROBOT_OPTIONS .
