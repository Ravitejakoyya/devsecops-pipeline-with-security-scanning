import pytest
from app.main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_create_user(client):
    res = client.post('/user', json={'username': 'alice', 'email': 'alice@example.com'})
    assert res.status_code == 201

def test_get_user(client):
    client.post('/user', json={'username': 'bob', 'email': 'bob@example.com'})
    res = client.get('/user/bob')
    assert res.status_code == 200
    assert res.get_json()['email'] == 'bob@example.com'

def test_ping(client):
    res = client.get('/ping')
    assert res.status_code == 200
    assert res.get_json()['message'] == 'pong'
    