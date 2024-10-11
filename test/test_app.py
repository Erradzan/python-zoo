import pytest
from app import app

@pytest.fixture
def client():
    # Fixture to set up the Flask test client.
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_front_page(client):
    # Test the front page.
    response = client.get('/')
    assert response.status_code == 200
    assert b"WELCOME TO KUNGFU PANDA ZOO. LOL" in response.data

def test_get_animals(client):
    # Test getting all animals.
    response = client.get('/animals')
    assert response.status_code == 200
    assert isinstance(response.json, dict)  # Adjusted to check for a dictionary
    assert len(response.json) > 0

def test_get_animal(client):
    # Test getting a specific animal.
    response = client.get('/animals/1')
    assert response.status_code == 200
    assert response.json['name'] == 'Po'

def test_get_nonexistent_animal(client):
    # Test getting a non-existent animal.
    response = client.get('/animals/999')
    assert response.status_code == 404
    assert response.json == {'error': 'Animal not found'}

def test_add_animal(client):
    # Test adding a new animal.
    new_animal = {
        "name": "Master Tigress",
        "age": "15 years",
        "species": "South China tiger",
        "enclosure": "Training Area",
        "feeding_schedule": "Daily",
        "diet": "Meat"
    }
    response = client.post('/animals', json=new_animal)
    assert response.status_code == 201
    assert response.json['message'] == 'Animal added successfully'

def test_update_animal(client):
    # Test updating an existing animal.
    update_data = {
        "name": "Updated Po",
        "age": "21 years",
        "species": "giant panda",
        "enclosure": "Bamboo Forest",
        "feeding_schedule": "Monday, Wednesday, Friday",
        "diet": "Bamboo, dumplings"
    }
    response = client.put('/animals/1', json=update_data)
    assert response.status_code == 200
    assert response.json['message'] == 'Animal updated successfully'

def test_delete_animal(client):
    # Test deleting an animal.
    response = client.delete('/animals/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Animal deleted successfully'

def test_get_employees(client):
    # Test getting all employees.
    response = client.get('/employees')
    assert response.status_code == 200
    assert isinstance(response.json, dict)  # Adjusted to check for a dictionary
    assert len(response.json) > 0

def test_get_employee(client):
    # Test getting a specific employee.
    response = client.get('/employees/1')
    assert response.status_code == 200
    assert response.json['name'] == 'Jack Black'

def test_get_nonexistent_employee(client):
    # Test getting a non-existent employee.
    response = client.get('/employees/999')
    assert response.status_code == 404
    assert response.json == {'error': 'Employee not found'}

def test_add_employee(client):
    # Test adding a new employee.
    new_employee = {
        "name": "New Employee",
        "email": "newemployee@notrealemail.com",
        "phone_number": "1-800-0000",
        "role": "Caretaker of New Animal",
        "responsibilities": "Caring for new animal",
        "schedule": "9 AM to 5 PM"
    }
    response = client.post('/employees', json=new_employee)
    assert response.status_code == 201
    assert response.json['message'] == 'Employee added successfully'

def test_update_employee(client):
    # Test updating an existing employee.
    update_data = {
        "name": "Updated Jack Black",
        "email": "updatedjackblack@notrealemail.com",
        "phone_number": "1-800-0001",
        "role": "Head Caretaker (promoted)",
        "responsibilities": "Overall animal care",
        "schedule": "9 AM to 5 PM"
    }
    response = client.put('/employees/1', json=update_data)
    assert response.status_code == 200
    assert response.json['message'] == 'Employee updated successfully'

def test_delete_employee(client):
    # Test deleting an employee.
    response = client.delete('/employees/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Employee deleted successfully'