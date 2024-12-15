from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import json
import os

app = Flask(__name__)


def load_books():
    if not os.path.exists('data.json'):
        return []
    with open('data.json', 'r') as file:
        return json.load(file)

def save_books(books):
    with open('data.json', 'w') as file:
        json.dump(books, file, indent=4)

SWAGGER_URL = '/api-docs'
API_URL = '/static/swagger_file.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Library Management API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ["title", "author", "published_year", "isbn"]):
            return jsonify({"message": "Missing required fields"}), 400

        books = load_books()
        books.append(data)
        save_books(books)
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

# List all books
@app.route('/books', methods=['GET'])
def list_books():
    try:
        books = load_books()
        return jsonify(books), 200
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

# Search for books
@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.get_json()
    books = load_books()
    for book in books:
        if book['isbn'] == isbn:
            book.update(data)
            save_books(books)
            return jsonify(book), 200
    return jsonify({'message': 'Book not found'}), 404

# Update book details by ISBN
@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    try:
        data = request.get_json()
        books = load_books()
        for book in books:
            if book['isbn'] == isbn:
                book.update(data)
                save_books(books)
                return jsonify(book), 200
        return jsonify({'message': 'Book not found'}), 404
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

# Delete a book by ISBN
@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    try:
        books = load_books()
        books = [book for book in books if book['isbn'] != isbn]
        save_books(books)
        return jsonify({'message': 'Book deleted'}), 200
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=3000)
