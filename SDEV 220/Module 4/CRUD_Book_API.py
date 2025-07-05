from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Database model definition
# It inherits from db.Model, which is the base class for all models in Flask-SQLAlchemy.
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author}"

# API Routes 
@app.route('/')
def index():
    return 'Welcome to the Book API!'

# GET all books
# This route will handle GET requests to '/books'.
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return jsonify({'books': output})

# GET a single book by ID
# This route will handle GET requests to '/books/<id>'
@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher})

# POST (Create) a new book
# This route will handle POST requests to '/books'.
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(book_name=data['book_name'], author=data['author'], publisher=data['publisher'])
    # Add the new book object to the database session.
    db.session.add(new_book)
    # Save the changes to the database.
    db.session.commit()
    # Return a JSON response with the ID of the newly created book.
    return jsonify({'id': new_book.id})

# PUT (Update) an existing book
# This route handles PUT requests to update a book's details.
@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()

    # Update the book's attributes with the new data.
    book.book_name = data['book_name']
    book.author = data['author']
    book.publisher = data['publisher']
    db.session.commit()
    return jsonify({'message': 'Book updated successfully.'})

# DELETE a book
# This route will handle DELETE requests to '/books/<id>'.
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "Book not found"}, 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully.'})

# This block ensures that the following code only runs when the script is executed directly
# (not when it's imported as a module).
if __name__ == '__main__':
    # This creates the database and the 'Book' table if they don't already exist.
    with app.app_context(): # RuntimeError: Working outside of application context.
        db.create_all()
    app.run(debug=True)
