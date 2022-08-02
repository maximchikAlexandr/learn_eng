import math
import time
from collections import ChainMap

from flask import flash
from flask_login import current_user

from dct import db
from dct.service import getEngTranslate, get_unic_words
from dct.models import (
    Text,
    Example,
    EngWord,
    TrRusWord,
    PartOfSpeech
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
    def add_text(self, text, title):
        tm = math.floor(time.time())  # Save time
        text_model = Text(text=text,
                    title=title,
                    time=tm,
                    id_user=current_user.get_id())

        if not self.is_existing_text(text):
            for word in get_unic_words(text):

                if self.is_existing_word(word):
                    eng_word_model = EngWord.query.filter(EngWord.eng_word == word).first()
                else:
                    eng_word_dct = getEngTranslate(word)
                    if eng_word_dct['tr']:
                        eng_word_model = self.add_word(eng_word_dct)
                    else: continue
                text_model.words.append(eng_word_model)

            self.__db.session.add(text_model)
            self.__db.session.commit()
            return True

        return False

    def is_existing_text(self, text):
        return bool(Text.query.filter(Text.text == text).all())

    def get_text(self, id_text):
        return Text.query.filter(Text.id == id_text).one()

    def remove_text(self, id_text):
        text = self.get_text(id_text)
        self.__db.session.delete(text)
        self.__db.session.commit()

    def get_text_paginate(self, id_user, page, per_page):
        return Text.query.filter(Text.id_user == id_user).paginate(page=page,
                                                                   per_page=per_page)

    def get_list_of_words(self, id_text):
        return Text.query.filter(Text.id == id_text).first().words

    def add_word(self, eng_word_dct):
        eng_word_model = EngWord(eng_word=eng_word_dct['text'],
                                ts=eng_word_dct['ts'])

        self._add_all_pos(eng_word_dct)
        self._add_all_rus_words(eng_word_dct, eng_word_model)
        self._add_all_examples(eng_word_dct, eng_word_model)

        self.__db.session.add(eng_word_model)
        self.__db.session.commit()

        return eng_word_model

    def is_existing_word(self, eng_word):
        return bool(EngWord.query.filter(EngWord.eng_word == eng_word).all())

    def get_word(self, id_word):
        return EngWord.query.filter(EngWord.id == id_word).one()

    def get_word_paginate(self, id_word, page, per_page):
        return EngWord.query.filter(EngWord.id == id_word).paginate(page=page,
                                                                   per_page=per_page)

    def _add_all_pos(self, eng_word_dct):
        pos_lst = []
        for pos in ChainMap(eng_word_dct['tr'], eng_word_dct['ex']):
            if not PartOfSpeech.query.filter(PartOfSpeech.pos == pos).all():
                pos_model = PartOfSpeech(pos=pos)
                pos_lst.append(pos_model)

        self.__db.session.add_all(pos_lst)
        self.__db.session.commit()

    def _add_all_examples(self, eng_word_dct, eng_word_model):
        examples_lst = []
        for pos, examples in eng_word_dct['ex'].items():
            for ex in examples:
                example_model = Example(
                    example=ex,
                    id_pos=PartOfSpeech.query.filter(PartOfSpeech.pos == pos).first().id,
                    id_eng_word=eng_word_model.id
                )
                examples_lst.append(example_model)

        self.__db.session.add_all(examples_lst)
        self.__db.session.commit()

    def _add_all_rus_words(self, eng_word_dct, eng_word_model):
        rus_words_lst = []
        for pos, tr_lst in eng_word_dct['tr'].items():
            for tr in tr_lst:
                if not TrRusWord.query.filter(TrRusWord.rus_word == tr).all():
                    tr_rus_word = TrRusWord(
                        rus_word = tr,
                        id_pos=PartOfSpeech.query.filter(PartOfSpeech.pos == pos).first().id
                    )
                    rus_words_lst.append(tr_rus_word)
                else:
                    tr_rus_word = TrRusWord.query.filter(TrRusWord.rus_word == tr).first()

                eng_word_model.translated_words.append(tr_rus_word)

        self.__db.session.add_all(rus_words_lst)
        self.__db.session.commit()

    def get_dct_words(self, id_text):
        words = self.get_text(id_text=id_text).words
        res = [
            { 'id' : wrd.id,
             'text' : wrd.eng_word,
             'ts' : wrd.ts,
             'tr' : [{pos.pos : [tr.rus_word for tr in wrd.translated_words if pos == tr.pos]} for pos in set(tr.pos for tr in wrd.translated_words)],
             'ex' : [{pos.pos : [ex.example for ex in wrd.examples if pos == ex.pos] } for pos in set(ex.pos for ex in wrd.examples)]}
            for wrd in words]
        return res

dictDB = DictDB(db)
