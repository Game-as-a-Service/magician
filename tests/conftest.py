import pytest
from magician.app.flask_app import app as flask_app


@pytest.fixture
def app():
    return flask_app


@pytest.fixture
def client(app):
    return app.test_client()
