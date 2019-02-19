FROM    python:3.7.2-stretch

COPY    . /atest

WORKDIR /atest

CMD     python3 -m robot -P . -d output -v tds_host:$TDS_HOST -v tds_port:$TDS_PORT $ROBOT_OPTIONS .
