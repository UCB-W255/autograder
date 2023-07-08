from fastapi.testclient import TestClient

from autograder.main import app

client = TestClient(app)


def test_good():
    assert 1==1