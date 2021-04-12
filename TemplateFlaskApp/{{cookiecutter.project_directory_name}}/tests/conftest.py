import flask
import pytest

from server.factory import create_server

LOCAL_SERVER_NAME = '127.0.0.1:5000'


@pytest.fixture
def server():
    """Create and configure a new app instance for each test."""
    test_app = create_server()
    test_app.config["SERVER_NAME"] = LOCAL_SERVER_NAME
    with test_app.app_context():
        yield test_app


@pytest.fixture
def dummy_api(server):
    dummy_blueprint = flask.blueprints.Blueprint('dummy blueprint',
                                                 __name__,
                                                 url_prefix='/api/dummy')
    server.register_blueprint(dummy_blueprint)
    return dummy_blueprint


def register_app_endpoints(app):
    from server.api.blueprint import v1
    app.register_blueprint(v1)


@pytest.fixture
def client(server):
    """A test client for the app."""
    register_app_endpoints(server)
    return server.test_client()


def raise_exception(*args, **kwargs):
    raise Exception("Function that raises exception")
