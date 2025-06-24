# app/controllers/author_controller.py

from flask import request, jsonify
from app.models.author_model import Author
from app import db

# --- CREATE ---
def add_author():
    """Cria um novo autor no banco de dados."""
    data = request.get_json()
    if 'name' not in data or not data['name'].strip():
        return jsonify({"message": "O nome do autor é obrigatório"}), 400

    # Verifica se o autor já existe
    if Author.query.filter_by(name=data['name']).first():
         return jsonify({"message": "Autor com este nome já existe"}), 409

    new_author = Author(name=data['name'], bio=data.get('bio'))
    db.session.add(new_author)
    db.session.commit()
    return jsonify({"message": "Autor adicionado com sucesso!", "author": new_author.to_dict_simple()}), 201

# --- READ ---
def get_authors():
    """Lê e retorna todos os autores."""
    authors = Author.query.all()
    return jsonify([author.to_dict() for author in authors]), 200

def get_author(author_id):
    """Lê e retorna um autor específico pelo ID."""
    author = Author.query.get_or_404(author_id)
    return jsonify(author.to_dict()), 200

# --- UPDATE ---
def update_author(author_id):
    """Atualiza os dados de um autor existente."""
    author = Author.query.get_or_404(author_id)
    data = request.get_json()
    
    # Atualiza os campos se eles forem fornecidos no JSON
    author.name = data.get('name', author.name)
    author.bio = data.get('bio', author.bio)
    
    db.session.commit()
    return jsonify({"message": "Autor atualizado com sucesso!", "author": author.to_dict_simple()}), 200

# --- DELETE ---
def delete_author(author_id):
    """Deleta um autor do banco de dados."""
    author = Author.query.get_or_404(author_id)
    
    # Regra de negócio: não permitir deletar autor se ele tiver livros associados
    if author.books:
        return jsonify({"message": "Não é possível deletar autor com livros associados."}), 400

    db.session.delete(author)
    db.session.commit()
    return jsonify({"message": "Autor removido com sucesso!"}), 200