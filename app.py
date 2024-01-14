from flask import Flask, request, jsonify, abort
from jsonschema import validate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["50 per hour", "5 per minute"])

items_data = []

item_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "price": {"type": "number"}
    },
    "required": ["name", "description", "price"]
}


class Item:
    def __init__(self, id, name, description, price):
        """Class to represent an Item."""
        self.id = id
        self.name = name
        self.description = description
        self.price = price


@app.route('/items', methods=['POST'])
@limiter.limit("5 per minute")
def create_item():
    """Endpoint to create a new item."""
    try:
        validate(request.json, item_schema)
    except Exception as e:
        abort(400, f"Input validation error: {str(e)}")

    items_data.append(Item(len(items_data) + 1, **request.json))
    return jsonify({'message': 'Item created successfully'}), 201


@app.route('/items', methods=['GET'])
@limiter.limit("10 per minute")
def read_all_items():
    """Endpoint to retrieve all items."""
    return jsonify([item.__dict__ for item in items_data])


@app.route('/items/<int:id>', methods=['GET'])
@limiter.limit("10 per minute")
def read_item(id):
    """Endpoint to retrieve a specific item by ID."""
    item = next((item for item in items_data if item.id == id), None)
    if item:
        return jsonify(item.__dict__)
    else:
        abort(404, 'Item not found')


@app.route('/items/<int:id>', methods=['PUT'])
@limiter.limit("5 per minute")
def update_item(id):
    """Endpoint to update a specific item by ID."""
    item = next((item for item in items_data if item.id == id), None)
    if item:
        try:
            validate(request.json, item_schema)
        except Exception as e:
            abort(400, f"Input validation error: {str(e)}")

        item.__dict__.update(request.json)
        return jsonify({'message': 'Item updated successfully'})
    else:
        abort(404, 'Item not found')


@app.route('/items/<int:id>', methods=['DELETE'])
@limiter.limit("5 per minute")
def delete_item(id):
    """Endpoint to delete a specific item by ID."""
    global items_data
    index_to_delete = next((i for i, item in enumerate(items_data) if item.id == id), None)
    if index_to_delete is None:
        abort(404, {'error': 'Item not found'})

    items_data.pop(index_to_delete)

    return jsonify({'message': 'Item deleted successfully'})


@app.errorhandler(400)
def bad_request_error(error):
    """Handler for 400 Bad Request errors."""
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400


@app.errorhandler(404)
def not_found_error(error):
    """Handler for 404 Not Found errors."""
    return jsonify({'error': 'Not Found', 'message': str(error)}), 404


if __name__ == '__main__':
    app.run(debug=True)
