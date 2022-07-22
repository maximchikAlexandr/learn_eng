from dct import db


class Texts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.Text(), nullable=False, unique=True)
    time = db.Column(db.Integer(), nullable=False)
    id_user = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'<id {self.id}, text: {self.text[:10]} >'

class EngWords(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    eng_word = db.Column(db.String(40), nullable=False, unique=True)
    ts = db.Column(db.String(40))

    def __repr__(self):
        return f'<id {self.id}, word: {self.eng_word} >'

class Examples(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    example = db.Column(db.String(40), nullable=False)
    pos = db.Column(db.String(20), nullable=False)
    id_eng_word = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<id {self.id}, ex: {self.example} >'

class TrRusWords(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    rus_word = db.Column(db.String(40), nullable=False, unique=True)
    pos = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<id {self.id}, rus word: {self.rus_word} >'
