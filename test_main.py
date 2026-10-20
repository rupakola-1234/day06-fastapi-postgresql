
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Learn FastAPI"}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Learn FastAPI"


def test_get_missing_task():
    response = client.get("/tasks/999999")
    assert response.status_code == 404
