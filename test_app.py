from app import app

def test_create_event():
    client = app.test_client()
    response = client.post('/events', json={
        "title": "Test Event",
        "description": "This is a test",
        "start_time": "2025-06-30 10:00",
        "end_time": "2025-06-30 11:00"
    })
    assert response.status_code == 201
    assert 'id' in response.get_json()
