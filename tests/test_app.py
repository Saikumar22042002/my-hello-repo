import pytest
from app import app

@pytest.fixture
def client():
    """Create and configure a new app instance for each test."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the main '/' endpoint for status code and message."""
    response = client.get('/')
    assert response.status_code == 200
    expected_message = "Hello World from repo 'my-hello-repo' on branch 'my-hello-branch'"
    assert response.json['message'] == expected_message

def test_health(client):
    """Test the '/health' endpoint for status code and content."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'
