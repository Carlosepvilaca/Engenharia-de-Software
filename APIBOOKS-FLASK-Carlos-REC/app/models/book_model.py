# app/models/book_model.py

from app import db
from sqlalchemy.orm import Mapped, mapped_column
from .author_model import Author # Importe o modelo Author

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    year: Mapped[int]
    genre: Mapped[str]

    # --- INÍCIO DA MODIFICAÇÃO ---
    # Substituímos o campo de texto 'author' por uma chave estrangeira
    author_id: Mapped[int] = mapped_column(db.ForeignKey("author.id"))
    
    # Criamos a referência ao objeto Author
    author: Mapped["Author"] = db.relationship(back_populates="books")
    # --- FIM DA MODIFICAÇÃO ---


    def to_dict(self):
        """Retorna representação completa do livro."""
        return {
            "id": self.id,
            "title": self.title,
            # Agora 'author' é um objeto, então chamamos seu próprio to_dict
            "author": self.author.to_dict_simple() if self.author else None,
            "year": self.year,
            "genre": self.genre
        }

    def to_dict_simple(self):
        """Retorna representação simplificada do livro."""
        return {
            "id": self.id,
            "title": self.title
        }