import sys

sys.path.append('../')

import pytest

from src.app import app as api


@pytest.fixture
def app():
    yield api


@pytest.fixture
def test_cli(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app))
