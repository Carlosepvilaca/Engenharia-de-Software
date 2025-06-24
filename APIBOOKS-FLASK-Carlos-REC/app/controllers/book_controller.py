# app/controllers/book_controller.py

from flask import request, jsonify
from app.models.book_model import Book
from app.models.author_model import Author
from app import db

def add_book():
    data = request.get_json()
    # Agora esperamos um 'author_id' no JSON
    if 'author_id' not in data:
        return jsonify({"message": "O ID do autor é obrigatório"}), 400

    # Verifica se o autor existe
    author = Author.query.get(data['author_id'])
    if not author:
        return jsonify({"message": "Autor não encontrado"}), 404
        
    # Remove 'author_id' do dicionário para passar o resto para o construtor Book
    author_id = data.pop('author_id')
    new_book = Book(**data, author_id=author_id)
    
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Livro adicionado com sucesso!"}), 201

def get_books():
    books = Book.query.all()
    result = [book.to_dict() for book in books]
    return jsonify(result)

def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())

def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Livro removido com sucesso!"})

def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()

    book.title = data.get("title", book.title)
    book.year = data.get("year", book.year)
    book.genre = data.get("genre", book.genre)
    
    if 'author_id' in data:
        author = Author.query.get(data['author_id'])
        if not author:
            return jsonify({"message": "Autor não encontrado"}), 404
        book.author_id = data['author_id']

    db.session.commit()
    return jsonify({"message": "Livro atualizado com sucesso!"})