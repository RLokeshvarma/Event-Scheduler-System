import pytest
from app import app as flask_app

@pytest.fixture
def client():
    return flask_app.test_client()

def test_create_event(client):
    response = client.post('/events', json={
        "title": "Meeting",
        "description": "Team sync",
        "start_time": "2025-07-01 10:00",
        "end_time": "2025-07-01 11:00"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == "Meeting"