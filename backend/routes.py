from flask import Blueprint, request, jsonify
from backend.database import db
from backend.models import Book

book_routes = Blueprint('books', __name__)

@book_routes.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{"id": b.id, "title": b.title, "author": b.author, "genre": b.genre} for b in books])

@book_routes.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], genre=data['genre'], description=data.get('description', ''))
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Kitap eklendi!"}), 201
