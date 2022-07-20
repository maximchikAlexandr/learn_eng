import math
import time

from flask import flash

from dct import db
from dct.models import (
Texts,
TextsEngWords,
Examples,
EngWords,
TrRusWords,
EngRusWords
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

    # @_wapper_error('Error of DB: text is not unique')
    def add_text(self, text):
        tm = math.floor(time.time())  # Save time
        text_model = Texts(text=text,
                    time=tm,
                    id_user=1) # replace!!!

        self.__db.session.add(text_model)
        self.__db.session.commit()
        return True

dictDB = DictDB(db)