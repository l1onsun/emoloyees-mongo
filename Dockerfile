FROM python:3.8-slim

# ENV IN_DOCKER=True
ENV WORKDIR=/app

COPY app $WORKDIR/app
WORKDIR config $WORKDIR/config

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

CMD ["sh", "docker_cmd.sh"]
