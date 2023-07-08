from fastapi.testclient import TestClient

from autograder.main import app

client = TestClient(app)
