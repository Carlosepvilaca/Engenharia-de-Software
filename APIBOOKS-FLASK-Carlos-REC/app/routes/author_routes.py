# app/routes/author_routes.py

from flask import Blueprint
from app.controllers import author_controller

author_bp = Blueprint("authors", __name__)

# Rota para CREATE
@author_bp.route("/authors", methods=["POST"])
def add_author():
    """
    Adiciona um novo autor
    ---
    tags: [Autores]
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [ "name" ]
          properties:
            name:
              type: string
              example: "J.R.R. Tolkien"
            bio:
              type: string
              example: "Autor de O Senhor dos Anéis."
    responses:
      201: {description: "Autor adicionado"}
      400: {description: "Dados inválidos"}
      409: {description: "Autor já existe"}
    """
    return author_controller.add_author()

# Rota para READ (todos)
@author_bp.route("/authors", methods=["GET"])
def get_authors():
    """
    Lista todos os autores
    ---
    tags: [Autores]
    responses:
      200: {description: "Lista de autores"}
    """
    return author_controller.get_authors()

# Rota para READ (um)
@author_bp.route("/authors/<int:author_id>", methods=["GET"])
def get_author(author_id):
    """
    Retorna um autor específico
    ---
    tags: [Autores]
    parameters:
      - name: author_id
        in: path
        type: integer
        required: true
    responses:
      200: {description: "Detalhes do autor"}
      404: {description: "Autor não encontrado"}
    """
    return author_controller.get_author(author_id)

# Rota para UPDATE
@author_bp.route("/authors/<int:author_id>", methods=["PUT"])
def update_author(author_id):
    """
    Atualiza um autor
    ---
    tags: [Autores]
    parameters:
      - name: author_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name: {type: string}
            bio: {type: string}
    responses:
      200: {description: "Autor atualizado"}
      404: {description: "Autor não encontrado"}
    """
    return author_controller.update_author(author_id)

# Rota para DELETE
@author_bp.route("/authors/<int:author_id>", methods=["DELETE"])
def delete_author(author_id):
    """
    Remove um autor
    ---
    tags: [Autores]
    parameters:
      - name: author_id
        in: path
        type: integer
        required: true
    responses:
      200: {description: "Autor removido"}
      400: {description: "Não é possível remover autor com livros"}
      404: {description: "Autor não encontrado"}
    """
    return author_controller.delete_author(author_id)