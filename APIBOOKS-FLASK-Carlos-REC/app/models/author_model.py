# app/models/author_model.py

from app import db
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class Author(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    bio: Mapped[str] = mapped_column(nullable=True) 

    books: Mapped[List["Book"]] = db.relationship(back_populates="author")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "bio": self.bio,
            "books": [book.to_dict_simple() for book in self.books]
        }
    
    def to_dict_simple(self):
        return {
            "id": self.id,
            "name": self.name
        }