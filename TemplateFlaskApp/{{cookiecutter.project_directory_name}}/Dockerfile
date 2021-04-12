FROM python:3.8 as base
COPY requirements.txt /
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt
FROM python:3.8
COPY --from=base /wheels /wheels
COPY --from=base requirements.txt .

ENV PYTHONBUFFERED=1

RUN pip install --no-cache /wheels/*
WORKDIR /app

COPY ./server /app/server
COPY ./scripts/runserver.sh /app/scripts/runserver.sh

RUN useradd {{cookiecutter.docker_user}}
RUN chown -R {{cookiecutter.docker_user}}:{{cookiecutter.docker_user}} /app
RUN chmod +x /app/scripts/runserver.sh

USER {{cookiecutter.docker_user}}

CMD ["/app/scripts/runserver.sh"]
