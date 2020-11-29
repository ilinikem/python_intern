"""
app tests example

"""

from fastapi.testclient import TestClient
from app import app, is_alive_host

client = TestClient(app)


def test_read_app():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Semrush!"}


def test_live():
    response = client.get("/healthz?hostname=semrush.com")
    response1 = client.get("/healthz?hostname=http://semrush.com")
    assert response.json() == {"status": "up"}
    assert response1.json() == {"status": "up"}


def test_down():
    response = client.get("/healthz?hostname=semrush.com/404")
    response1 = client.get("/healthz?hostname=http://semrush.com/404")
    assert response.json() == {"status": "down"}
    assert response1.json() == {"status": "down"}


