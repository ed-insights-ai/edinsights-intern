"""
Flask API Server
-------------
Create a simple Flask API server according to the specified requirements.
This exercise focuses on building RESTful APIs with Flask.
"""

from flask import Flask, request, jsonify, abort, make_response
import json
import os
import uuid
from datetime import datetime
from functools import wraps
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Sample data (in a real app, this would come from a database)
BOOKS_FILE = 'books.json'

def load_books():
    """Load books from JSON file or create empty list if file doesn't exist."""
    try:
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, 'r') as f:
                return json.load(f)
        else:
            return []
    except Exception as e:
        logger.error(f"Error loading books: {e}")
        return []

def save_books(books):
    """Save books to JSON file."""
    try:
        with open(BOOKS_FILE, 'w') as f:
            json.dump(books, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error saving books: {e}")
        return False

# Sample books data for initial setup
SAMPLE_BOOKS = [
    {
        "id": "1",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
        "genre": "Fiction"
    },
    {
        "id": "2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_year": 1960,
        "genre": "Fiction"
    },
    {
        "id": "3",
        "title": "1984",
        "author": "George Orwell",
        "published_year": 1949,
        "genre": "Dystopian"
    }
]

# Create sample data file if it doesn't exist
if not os.path.exists(BOOKS_FILE):
    save_books(SAMPLE_BOOKS)

# Auth functions (to be implemented)
def require_api_key(f):
    """Decorator for requiring API key."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        # TODO: Implement your API key validation logic
        # YOUR CODE HERE
        return f(*args, **kwargs)
    return decorated_function


@app.route('/api/v1/books', methods=['GET'])
def get_books():
    """
    Get all books or filter by query parameters.
    
    Returns:
        json: A list of books
    """
    # YOUR CODE HERE
    pass

@app.route('/api/v1/books/<book_id>', methods=['GET'])
def get_book(book_id):
    """
    Get a specific book by ID.
    
    Args:
        book_id (str): The ID of the book to retrieve
        
    Returns:
        json: The book data
        
    Raises:
        404: If the book is not found
    """
    # YOUR CODE HERE
    pass

@app.route('/api/v1/books', methods=['POST'])
@require_api_key
def create_book():
    """
    Create a new book.
    
    Returns:
        json: The created book data
        
    Raises:
        400: If the request data is invalid
    """
    # YOUR CODE HERE
    pass

@app.route('/api/v1/books/<book_id>', methods=['PUT'])
@require_api_key
def update_book(book_id):
    """
    Update a specific book by ID.
    
    Args:
        book_id (str): The ID of the book to update
        
    Returns:
        json: The updated book data
        
    Raises:
        404: If the book is not found
        400: If the request data is invalid
    """
    # YOUR CODE HERE
    pass

@app.route('/api/v1/books/<book_id>', methods=['DELETE'])
@require_api_key
def delete_book(book_id):
    """
    Delete a specific book by ID.
    
    Args:
        book_id (str): The ID of the book to delete
        
    Returns:
        json: Success message
        
    Raises:
        404: If the book is not found
    """
    # YOUR CODE HERE
    pass

@app.route('/api/v1/books/search', methods=['GET'])
def search_books():
    """
    Search for books by title, author, or genre.
    
    Returns:
        json: A list of matching books
    """
    # YOUR CODE HERE
    pass

@app.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """
    Get statistics about the books collection.
    
    Returns:
        json: Statistics like total books, books per genre, etc.
    """
    # YOUR CODE HERE
    pass

@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors."""
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

# Custom middleware to log requests
@app.before_request
def log_request_info():
    """Log request information."""
    logger.info(f"Request: {request.method} {request.path} {request.remote_addr}")

@app.after_request
def add_header(response):
    """Add common headers to response."""
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization,X-API-Key'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response

if __name__ == '__main__':
    # Ensure books.json exists with sample data
    if not os.path.exists(BOOKS_FILE):
        save_books(SAMPLE_BOOKS)
    
    print("Flask API Server")
    print("Available endpoints:")
    print("  GET    /api/v1/books           - Get all books")
    print("  GET    /api/v1/books/<id>      - Get book by ID")
    print("  POST   /api/v1/books           - Create a new book (requires API key)")
    print("  PUT    /api/v1/books/<id>      - Update a book (requires API key)")
    print("  DELETE /api/v1/books/<id>      - Delete a book (requires API key)")
    print("  GET    /api/v1/books/search    - Search books")
    print("  GET    /api/v1/stats           - Get collection statistics")
    print("\nRunning on http://127.0.0.1:5000/")
    
    app.run(debug=True)