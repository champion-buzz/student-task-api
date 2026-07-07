from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_health_route():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Study RAG notes", "course": "AI", "done": False},
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Study RAG notes"


def test_missing_task():
    response = client.get("/tasks/999")

    assert response.status_code == 404
