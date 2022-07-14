from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __bind_key__ = 'user_bp'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    hash_psw = db.Column(db.String(255), nullable=False)

class UserDB:

    def __init__(self, db):
        self.__db = db

    def add_new_user(self, username, email, hashpsw):
        user = User(username=username,
                    email=email,
                    hash_psw=hashpsw)

        self.__db.session.add(user)
        self.__db.session.commit()
