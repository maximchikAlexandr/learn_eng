from flask_login import UserMixin

from user import db


class User(db.Model, UserMixin):
    __bind_key__ = 'user_bp'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    hash_psw = db.Column(db.String(255), nullable=False)
    time = db.Column(db.Integer(), nullable=False)
