from user import db


class Texts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.Text(), nullable=False, unique=True)
    time = db.Column(db.Integer(), nullable=False)
    id_user = db.Column(db.Integer(), nullable=False)

class TextsEngWords(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_text = db.Column(db.Integer(), nullable=False)
    id_eng_word = db.Column(db.Integer(), nullable=False)

class EngWords(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    eng_word = db.Column(db.String(40), nullable=False, unique=True)
    ts = db.Column(db.String(40))

class Examples(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    example = db.Column(db.String(40), nullable=False)
    pos = db.Column(db.String(20), nullable=False)
    id_eng_word = db.Column(db.Integer, nullable=False)

class TrRusWords(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    rus_word = db.Column(db.String(40), nullable=False, unique=True)
    pos = db.Column(db.String(20), nullable=False)

class EngRusWords(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_eng_word = db.Column(db.Integer(), nullable=False)
    id_rus_word = db.Column(db.Integer(), nullable=False)
