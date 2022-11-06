from sqlalchemy.sql import func
from src.routes.routes import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname


def new_user(id, name, surname):
    user = User(id, name, surname)
    db.session.add(user)
    db.session.commit()
