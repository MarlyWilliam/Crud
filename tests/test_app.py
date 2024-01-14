import json
import pytest
from app import app, items_data


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_create_item(client):
    # Test creating an item
    response = client.post('/items', json={'name': 'Test Item', 'description': 'Test Description', 'price': 10.99})
    assert response.status_code == 201


def test_read_all_items(client):
    # Test reading all items
    response = client.get('/items')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_read_item(client):
    # Test reading a specific item
    response = client.get('/items/1')
    assert response.status_code == 200
    assert 'Test Item' in response.json['name']


def test_update_item(client):
    # Test updating an item
    response = client.put('/items/1', json={'name': 'Updated Item', 'description': 'Updated Description', 'price': 19.99})
    assert response.status_code == 200


def test_item_not_found(client):
    # Test reading, updating, and deleting a non-existent item
    for endpoint in ['/items/999', '/items/999', '/items/999']:
        response = client.get(endpoint)
        assert response.status_code == 404


def test_invalid_input(client):
    # Test input validation error when creating an item
    response = client.post('/items', json={'name': 'Test Item', 'description': 123, 'price': 'invalid_price'})
    assert response.status_code == 400


def test_invalid_update_input(client):
    # Test input validation error when updating an item
    response = client.put('/items/1', json={'name': 'Updated Item', 'description': 123, 'price': 'invalid_price'})
    assert response.status_code == 400


def test_delete_item(client):
    # Test deleting an item
    response = client.delete('/items/1')
    assert response.status_code == 200


def test_update_nonexistent_item(client):
    # Test updating a non-existent item
    response = client.put('/items/999', json={'name': 'Updated Item', 'description': 'Updated Description', 'price': 19.99})
    assert response.status_code == 404


def test_delete_nonexistent_item(client):
    # Test deleting a non-existent item
    response = client.delete('/items/999')
    assert response.status_code == 404