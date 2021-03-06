import datetime
import logging
import uuid

from flask import Flask, g, request

from server.api import blueprint
from server.api.index import index
from server.api.swagger import swaggerui_blueprint

log = logging.getLogger(__name__)


def register_blueprint(flask_app, blueprints=()):
    for flask_blueprint in blueprints:
        flask_app.register_blueprint(flask_blueprint)


def register_request_callbacks(flask_app):
    def begin_request():
        g.start = datetime.datetime.now()
        g.x_request_id = request.headers.get('X-Request-ID', uuid.uuid4())
        flask_app.logger.info(
            "Received a new request x_request_id[%s] body[%s] method[%s] endpoint[%s]",
            g.x_request_id,
            request.json,
            request.method,
            request.path
        )

    def end_request(response):
        request.direct_passthrough = False
        duration = datetime.datetime.now() - g.start
        log.info(
            'PERF x_request_id[%s] time[%s] method[%s] endpoint[%s] status[%s]',
            g.x_request_id,
            duration,
            request.method,
            request.path,
            response.status
        )
        log.debug('RESPONSE x_request_id[%s]', g.x_request_id)
        response.headers['X-Request-ID'] = g.x_request_id
        response.headers['X-Time-Elapsed'] = duration
        return response

    flask_app.before_request(begin_request)
    flask_app.after_request(end_request)


def create_server():
    app = Flask("{{cookiecutter.project_title}}")
    register_request_callbacks(app)
    register_blueprint(app, blueprints=(index, swaggerui_blueprint, blueprint.v1,))
    app.url_map.strict_slashes = False
    return app


def run_server(server):
    try:
        log.debug("Starting the {{cookiecutter.project_title}} Server")
        server.run()
    except Exception as e:
        log.error("Error while running the application: %s", e)
        raise
