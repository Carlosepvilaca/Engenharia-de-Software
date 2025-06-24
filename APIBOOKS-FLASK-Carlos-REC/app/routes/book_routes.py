# app/routes/book_routes.py

from flask import Blueprint
from app.controllers import book_controller

book_bp = Blueprint("books", __name__)

@book_bp.route("/books", methods=["POST"])
def add_book():
    """
    Adiciona um novo livro
    ---
    tags:
      - Livros
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - title
            - year
            - genre
            - author_id
          properties:
            title:
              type: string
              example: "1984"
            year:
              type: integer
              example: 1949
            genre:
              type: string
              example: "Ficção"
            author_id:
              type: integer
              description: ID do autor existente.
              example: 1
    responses:
      201:
        description: Livro adicionado com sucesso
      400:
        description: Erro de validação ou ID do autor faltando
      404:
        description: Autor não encontrado
    """
    return book_controller.add_book()

# As rotas GET, DELETE e a principal de PUT não precisam de mudança na documentação.
# Apenas a lógica interna delas foi alterada no controller.
@book_bp.route("/books", methods=["GET"])
def get_books():
    """
    Lista todos os livros
    ---
    tags:
      - Livros
    responses:
      200:
        description: Lista de livros
    """
    return book_controller.get_books()

@book_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    """
    Retorna um livro específico pelo ID
    ---
    tags:
      - Livros
    parameters:
      - in: path
        name: book_id
        type: integer
        required: true
        description: ID do livro a ser consultado
    responses:
      200:
        description: Livro encontrado com sucesso
      404:
        description: Livro não encontrado
    """
    return book_controller.get_book(book_id)

@book_bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    """
    Atualiza os dados de um livro
    ---
    tags:
      - Livros
    parameters:
      - in: path
        name: book_id
        type: integer
        required: true
        description: ID do livro a ser atualizado
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: "Novo título"
            year:
              type: integer
              example: 2024
            genre:
              type: string
              example: "Novo gênero"
            author_id:
              type: integer
              description: ID do novo autor.
              example: 2
    responses:
      200:
        description: Livro atualizado com sucesso
      404:
        description: Livro ou Autor não encontrado
    """
    return book_controller.update_book(book_id)

@book_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    """
    Remove um livro pelo ID
    ---
    tags:
      - Livros
    parameters:
      - in: path
        name: book_id
        type: integer
        required: true
        description: ID do livro a ser removido
    responses:
      200:
        description: Livro removido com sucesso
      404:
        description: Livro não encontrado
    """
    return book_controller.delete_book(book_id)