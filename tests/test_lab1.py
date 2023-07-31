from fastapi.testclient import TestClient
import pytest

from autograder.main import app

client = TestClient(app)


test_packages = [("uvicorn", "fastapi"), ("httpx", "pytest", "isort", "black")]


@pytest.mark.parametrize("packages", test_packages, ids=["main", "dev"])
def test_lab1_packagecheck(packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            assert False
    assert True


def test_lab1_root():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


@pytest.mark.parametrize(
    "query_parameter, value",
    [("bob", "name"), ("nam", "name")],
)
def test_lab1_hello_endpoint_bad_parameter(query_parameter, value):
    response = client.get(f"/hello?{query_parameter}={value}")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "input": None,
                "loc": ["query", "name"],
                "msg": "Field required",
                "type": "missing",
                "url": "https://errors.pydantic.dev/2.1/v/missing",
            }
        ]
    }


@pytest.mark.parametrize(
    "test_input, expected",
    [("james", "james"), ("bOB", "bOB"), ("BoB", "BoB"), (100, 100)],
)
def test_lab1_hello_endpoint(test_input, expected):
    response = client.get(f"/hello?name={test_input}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {expected}"}


def test_lab1_docs_endpoint():
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_lab1_openapi_version_correct():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json()["openapi"][0:2] == "3."
    assert response.headers["content-type"] == "application/json"


def test_lab1_hello_multiple_parameter_with_good_and_bad():
    response = client.get("/hello?name=james&bob=name")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello james"}
