import math
import time

from flask import flash

from dct import db
from dct.models import (
    Text,
    Example,
    EngWord,
    TrRusWord
    )

def _wapper_error(flashed_message):
    def wapper_error(func):
        def wapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except:
                flash(flashed_message, category='danger')
            return False
        return wapper
    return wapper_error



class DictDB:
    def __init__(self, db):
        self.__db = db

    @_wapper_error('Error of DB: text is not unique')
    def add_text(self, text):
        tm = math.floor(time.time())  # Save time
        text_model = Text(text=text,
                    time=tm,
                    id_user=1) # replace!!!

        self.__db.session.add(text_model)
        self.__db.session.commit()
        return True

    def is_existing_text(self, text):
        return bool(Text.query.filter(Text.text == text).all())

    def get_text(self, id_text):
        return Text.query.filter(Text.id == id_text).one()

    def get_list_of_texts(self, id_user):
        return Text.query.filter(Text.id_user == id_user).all()

    def get_list_of_words(self, id_text):
        return Text.query.filter(Text.id == id_text).first().words

    def is_existing_word(self, eng_word):
        return bool(EngWord.query.filter(EngWord.eng_word == eng_word).all())

    def get_word(self, id_word):
        return EngWord.query.filter(EngWord.id == id_word).one()

# {'text': 'fill', 'ts': 'fɪl', 'tr': {'глагол': ['заполнять', 'заполнить'], 'существительное': ['заполнение', 'наполнение', 'заливка']}, 'ex': {'глагол': ['fill the space – заполнять пространство', 'fill the vacancy – заполнить вакансию', 'fill the earth – наполнять землю', 'filled polymer – наполненный полимер', 'fill with water – заливать водой', 'fill the tank – заправить бак', 'fill the gap – восполнить пробел', 'fill a pipe – набивать трубку'], 'существительное': ['fill factor – коэффициент заполнения', 'degree of filling – степень наполнения', 'background fill – заливка фона']}}
# dictDB.add_word(getEngTranslate('hand'))
    def add_word(self, eng_word_dct):
        eng_word_model = EngWord(eng_word=eng_word_dct['text'],
                    ts=eng_word_dct['ts'])

        self.__db.session.add(eng_word_model)
        self.__db.session.commit()

        return True


dictDB = DictDB(db)
