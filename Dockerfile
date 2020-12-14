FROM python:3.9-slim

ENV WORKDIR=/app
WORKDIR $WORKDIR

# for httptools and uvloop
RUN apt-get update && apt-get install -y gcc make
RUN pip install pipenv

COPY Pipfile $WORKDIR/Pipfile
COPY Pipfile.lock $WORKDIR/Pipfile.lock
RUN pipenv sync

COPY app $WORKDIR/app
COPY config $WORKDIR/config
COPY database $WORKDIR/database
COPY dotenv $WORKDIR/dotenv
COPY scripts $WORKDIR/scripts
COPY employees.json $WORKDIR/employees.json

CMD pipenv run docker start
