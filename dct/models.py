from dct import db

texts_eng_words = db.Table('texts_eng_words',
                           db.Column('id', db.Integer(), primary_key=True),
                           db.Column('id_text', db.Integer(), db.ForeignKey('texts.id')),
                           db.Column('id_eng_word', db.Integer(), db.ForeignKey('eng_words.id'))
                           )

eng_rus_words = db.Table('eng_rus_words',
                         db.Column('id', db.Integer(), primary_key=True),
                         db.Column('id_rus_word', db.Integer(), db.ForeignKey('tr_rus_word.id')),
                         db.Column('id_eng_word', db.Integer(), db.ForeignKey('eng_words.id'))
                         )

class Text(db.Model):
    __tablename__ = 'texts'
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.Text(), nullable=False, unique=True)
    time = db.Column(db.Integer(), nullable=False)
    id_user = db.Column(db.Integer(), nullable=False)

    words = db.relationship('EngWord', secondary=texts_eng_words, backref=db.backref('texts', lazy='dynamic'))

    def __repr__(self):
        return f'<id {self.id}, text: {self.text} >'



class EngWord(db.Model):
    __tablename__ = 'eng_words'
    id = db.Column(db.Integer(), primary_key=True)
    eng_word = db.Column(db.String(40), nullable=False, unique=True)
    ts = db.Column(db.String(40))
    examples = db.relationship('Example', backref='eng_word', lazy=True)

    translated_words = db.relationship('TrRusWord', secondary=eng_rus_words, backref=db.backref('eng_words', lazy='dynamic'))

    def __repr__(self):
        return f'<id {self.id}, word: {self.eng_word}, [{self.ts}] >'

class Example(db.Model):
    __tablename__ = 'examples'
    id = db.Column(db.Integer(), primary_key=True)
    example = db.Column(db.String(40), nullable=False)
    id_pos = db.Column(db.Integer, db.ForeignKey('parts_of_speech.id'), nullable=False)
    id_eng_word = db.Column(db.Integer, db.ForeignKey('eng_words.id'),nullable=False)

    def __repr__(self):
        return f'<id {self.id}, ex: {self.example} >'

class TrRusWord(db.Model):
    __tablename__ = 'tr_rus_word'
    id = db.Column(db.Integer(), primary_key=True)
    rus_word = db.Column(db.String(40), nullable=False, unique=True)
    id_pos = db.Column(db.Integer, db.ForeignKey('parts_of_speech.id'), nullable=False)

    def __repr__(self):
        return f'<id {self.id}, rus word: {self.rus_word} >'

class PartOfSpeech(db.Model):
    __tablename__ = 'parts_of_speech'
    id = db.Column(db.Integer(), primary_key=True)
    pos = db.Column(db.String(20), nullable=False, unique=True)
    ex = db.relationship('Example', backref='pos', lazy=True)
    tr_rus_words = db.relationship('TrRusWord', backref='pos', lazy=True)

    def __repr__(self):
        return f'<id {self.id}, part of speech: {self.pos} >'
