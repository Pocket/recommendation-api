from app.main import app
from fastapi.testclient import TestClient

test_client = TestClient(app)


def test_main_root():
    response = test_client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_main_feed_success():
    response = test_client.get('/feed/4255')
    assert response.status_code == 200
    assert response.json() == {'id': 4255, 'title': "Essential Reads"}


def test_main_feed_fail():
    # send a string instead of int as the item id 
    response = test_client.get('/feed/hello')
    assert response.status_code == 422
