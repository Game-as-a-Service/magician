import pytest

from app import app
from app.config import TestingConfig


@pytest.fixture(scope="session")
def client():
    app.config.from_object(TestingConfig)

    with app.test_client() as client:
        yield client
