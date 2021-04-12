#!/usr/bin/env bash

export HOME=$(pwd)

export PYTHONPATH=${HOME}

export GUNICORN_HOST="0.0.0.0"
export GUNICORN_PORT="5000"
export GUNICORN_APP_PATH="${PYTHONPATH}server"
export GUNICORN_APP_MODULE="server.run:server"
export GUNICORN_WORKERS_NUMBER="2"
export GUNICORN_TIMEOUT="60"
export GUNICORN_BIND="${GUNICORN_HOST}:${GUNICORN_PORT}"

gunicorn --reload --capture-output --bind ${GUNICORN_BIND} --workers ${GUNICORN_WORKERS_NUMBER} --timeout ${GUNICORN_TIMEOUT} ${GUNICORN_APP_MODULE}
