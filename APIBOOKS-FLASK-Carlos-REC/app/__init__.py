# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flasgger import Swagger

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    Swagger(app)
    with app.app_context():
        # A importação precisa estar aqui para o db.create_all() encontrá-los
        from .models import book_model, author_model
        db.create_all()

        from .routes.book_routes import book_bp
        app.register_blueprint(book_bp)

        # --- ADICIONE ESTA PARTE ---
        from .routes.author_routes import author_bp
        app.register_blueprint(author_bp)
        # --- FIM DA ADIÇÃO ---

    return app