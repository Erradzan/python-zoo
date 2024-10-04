from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

database = {
    "animals": {
        1: {
            "name": "Po",
            "age": "20 years",
            "species": "giant panda",
            "enclosure": "Bamboo Forest",
            "feeding_schedule": "Monday, Wednesday, Friday",
            "diet": "Bamboo, dumplings"
        },
        2: {
            "name": "Master Shifu",
            "age": "60 years",
            "species": "red panda",
            "enclosure": "Mountain Sanctuary",
            "feeding_schedule": "Tuesday, Thursday, Saturday",
            "diet": "Berries, bamboo shoots, rice"
        },
        3: {
            "name": "Tigress",
            "age": "22 years",
            "species": "South China tiger",
            "enclosure": "Jungle Arena",
            "feeding_schedule": "Monday, Thursday, Sunday",
            "diet": "Meat"
        },
        4: {
            "name": "Crane",
            "age": "18 years",
            "species": "Black-necked crane",
            "enclosure": "Wetlands",
            "feeding_schedule": "Daily",
            "diet": "Fish, small insects"
        },
        5: {
            "name": "Master Oogway",
            "age": "1000+ years",
            "species": "Galápagos tortoise",
            "enclosure": "Sacred Peach Tree Island",
            "feeding_schedule": "Monday, Wednesday, Saturday",
            "diet": "Leaves, fruit"
        }
    },
    "employees": {
        1: {
            "name": "Jack Black",
            "email": "JackBlack@notrealemail.com",
            "phone_number": "1-800-5454",
            "role": "Caretaker of Po",
            "responsibilities": "Feeding Po, keeping Bamboo Forest clean, organizing kung fu events",
            "schedule": "Live at the zoo"
        },
        2: {
            "name": "Dustin Hoffman",
            "email": "DustinHoffman@notrealemail.com",
            "phone_number": "1-800-8724",
            "role": "Caretaker of Master Shifu",
            "responsibilities": "Feeding Shifu, ensuring peace in Mountain Sanctuary, overseeing training areas",
            "schedule": "Live at the zoo"
        },
        3: {
            "name": "Angelina Jolie",
            "email": "AngelinaJolie@notrealemail.com",
            "phone_number": "1-800-you-wish",
            "role": "Caretaker of Tigress",
            "responsibilities": "Feeding Tigress, organizing Jungle Arena activities, ensuring Tigress's health and fitness",
            "schedule": "not live at the zoo so 9 AM to 5 PM Monday to Saturday"
        },
        4: {
            "name": "David Cross",
            "email": "DavidCross@notrealemail.com",
            "phone_number": "1-800-2121",
            "role": "Caretaker of Crane",
            "responsibilities": "Feeding Crane, maintaining Wetlands, ensuring flying practice and health checks",
            "schedule": "Live at the zoo"
        },
        5: {
            "name": "Randall Duk Kim",
            "email": "RandallDK@notrealemail.com",
            "phone_number": "1-800-wise-man",
            "role": "Caretaker of Master Oogway",
            "responsibilities": "Maintaining Sacred Peach Tree Island, feeding Oogway, organizing philosophical discussions",
            "schedule": "Live at the zoo, sometimes"
        }
    }
}

@app.route("/", methods=["GET"])
def front_page():
    return "<p> WELCOME TO KUNGFU PANDA ZOO. LOL </p>"

@app.route('/animals', methods=['GET'])
def get_animals():
    """Get all animals
    ---
    responses:
      200:
        description: A list of animals
    """
    return jsonify(database["animals"])

@app.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    """Get a specific animal
    ---
    parameters:
      - name: id
        type: integer
        required: true
        description: The ID of the animal
    responses:
      200:
        description: An animal
      404:
        description: Animal not found
    """
    animal = database["animals"].get(id)
    if animal:
        return jsonify(animal)
    return jsonify({'error': 'Animal not found'}), 404

@app.route('/animals', methods=['POST'])
def add_animal():
    """Add a new animal
    ---
    parameters:
      - name: animal
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            age:
              type: string
            species:
              type: string
            enclosure:
              type: string
            feeding_schedule:
              type: string
            diet:
              type: string
    responses:
      201:
        description: Animal added successfully
    """
    data = request.json
    new_id = max(database["animals"].keys()) + 1
    database["animals"][new_id] = data
    return jsonify({'message': 'Animal added successfully', 'id': new_id}), 201

@app.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    """Update an existing animal
    ---
    parameters:
      - name: id
        type: integer
        required: true
      - name: animal
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            age:
              type: string
            species:
              type: string
            enclosure:
              type: string
            feeding_schedule:
              type: string
            diet:
              type: string
    responses:
      200:
        description: Animal updated successfully
      404:
        description: Animal not found
    """
    animal = database["animals"].get(id)
    if animal:
        data = request.json
        database["animals"][id] = data
        return jsonify({'message': 'Animal updated successfully'})
    return jsonify({'error': 'Animal not found'}), 404

@app.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    """Delete an animal
    ---
    parameters:
      - name: id
        type: integer
        required: true
    responses:
      200:
        description: Animal deleted successfully
      404:
        description: Animal not found
    """
    if id in database["animals"]:
        del database["animals"][id]
        return jsonify({'message': 'Animal deleted successfully'})
    return jsonify({'error': 'Animal not found'}), 404

@app.route('/employees', methods=['GET'])
def get_employees():
    """Get all employees
    ---
    responses:
      200:
        description: A list of employees
    """
    return jsonify(database["employees"])

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    """Get a specific employee
    ---
    parameters:
      - name: id
        type: integer
        required: true
        description: The ID of the employee
    responses:
      200:
        description: An employee
      404:
        description: Employee not found
    """
    employee = database["employees"].get(id)
    if employee:
        return jsonify(employee)
    return jsonify({'error': 'Employee not found'}), 404

@app.route('/employees', methods=['POST'])
def add_employee():
    """Add a new employee
    ---
    parameters:
      - name: employee
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
            phone_number:
              type: string
            role:
              type: string
            responsibilities:
              type: string
            schedule:
              type: string
    responses:
      201:
        description: Employee added successfully
    """
    data = request.json
    new_id = max(database["employees"].keys()) + 1
    database["employees"][new_id] = data
    return jsonify({'message': 'Employee added successfully', 'id': new_id}), 201

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    """Update an existing employee
    ---
    parameters:
      - name: id
        type: integer
        required: true
      - name: employee
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
            phone_number:
              type: string
            role:
              type: string
            responsibilities:
              type: string
            schedule:
              type: string
    responses:
      200:
        description: Employee updated successfully
      404:
        description: Employee not found
    """
    employee = database["employees"].get(id)
    if employee:
        data = request.json
        database["employees"][id] = data
        return jsonify({'message': 'Employee updated successfully'})
    return jsonify({'error': 'Employee not found'}), 404

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    """Delete an employee
    ---
    parameters:
      - name: id
        type: integer
        required: true
    responses:
      200:
        description: Employee deleted successfully
      404:
        description: Employee not found
    """
    if id in database["employees"]:
        del database["employees"][id]
        return jsonify({'message': 'Employee deleted successfully'})
    return jsonify({'error': 'Employee not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)