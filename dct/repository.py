"""Realization of repository pattern"""

import math
import time
from collections import ChainMap

from flask import flash
from flask_login import current_user


from dct.service import Traslation, get_unic_words
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


class WordRepository:

    def __init__(self, session_, eng_word_dct):
        self.__session = session_
        self.__eng_word_dct = eng_word_dct
        self.__eng_word_model = EngWord(eng_word=eng_word_dct['text'],
                                 ts=eng_word_dct['ts'])

    def get_model(self):
        return self.__eng_word_model

    def save(self):
        self._save_all_pos()
        self._save_all_rus_words()
        self._save_all_examples()

        self.__session.add(self.__eng_word_model)
        self.__session.commit()

    def _save_all_pos(self):
        pos_lst = []
        for pos in ChainMap(self.__eng_word_dct['tr'], self.__eng_word_dct['ex']):
            if not PartOfSpeech.query.filter(PartOfSpeech.pos == pos).all():
                pos_model = PartOfSpeech(pos=pos)
                pos_lst.append(pos_model)

        self.__session.add_all(pos_lst)
        self.__session.commit()

    def _save_all_examples(self):
        examples_lst = []
        for pos, examples in self.__eng_word_dct['ex'].items():
            for ex in examples:
                example_model = Example(
                    example=ex,
                    id_pos=PartOfSpeech.query.filter(PartOfSpeech.pos == pos).first().id,
                    id_eng_word=self.__eng_word_model.id
                )
                examples_lst.append(example_model)

        self.__session.add_all(examples_lst)
        self.__session.commit()

    def _save_all_rus_words(self):
        rus_words_lst = []
        for pos, tr_lst in self.__eng_word_dct['tr'].items():
            for tr in tr_lst:
                if not TrRusWord.query.filter(TrRusWord.rus_word == tr).all():
                    tr_rus_word = TrRusWord(
                        rus_word=tr,
                        id_pos=PartOfSpeech.query.filter(PartOfSpeech.pos == pos).first().id
                    )
                    rus_words_lst.append(tr_rus_word)
                else:
                    tr_rus_word = TrRusWord.query.filter(TrRusWord.rus_word == tr).first()

                self.__eng_word_model.translated_words.append(tr_rus_word)

        self.__session.add_all(rus_words_lst)
        self.__session.commit()

    @staticmethod
    def is_existing_word(eng_word):
        return bool(EngWord.query.filter(EngWord.eng_word == eng_word).all())


class TextRepository:

    def __init__(self, session_, text, title):
        self.__session = session_
        self.__text = text
        self.__title = title
        self.__text_model = Text(text=text,
                          title=title,
                          time=math.floor(time.time()),
                          id_user=current_user.get_id())

    def save(self):

        if not self._is_existing_text():
            for word in get_unic_words(self.__text):

                if WordRepository.is_existing_word(word):
                    eng_word_model = EngWord.query.filter(EngWord.eng_word == word).first()
                else:
                    eng_word_dct = Traslation(word).parsing_response()
                    if eng_word_dct['tr']:
                        word = WordRepository(self.__session, eng_word_dct)
                        word.save()
                        eng_word_model = word.get_model()
                    else:
                        continue
                self.__text_model.words.append(eng_word_model)

            self.__session.add(self.__text_model)
            self.__session.commit()
            return True

        return False

    def _is_existing_text(self):
        return bool(Text.query.filter(Text.text == self.__text).all())

    @classmethod
    def remove_text(cls, session, id_text):
        text = cls.get_text(id_text)
        session.delete(text)
        session.commit()

    @staticmethod
    def get_text(id_text):
        return Text.query.filter(Text.id == id_text).one()


class Pagination:

    @staticmethod
    def pagination_for_texts(id_user, page, per_page):
        print('text', Text.query.filter(Text.id_user == id_user).paginate(page=page,
                                                                   per_page=per_page))
        return Text.query.filter(Text.id_user == id_user).paginate(page=page,
                                                                   per_page=per_page)

    @staticmethod
    def pagination_for_words(id_text, page, per_page):
        print('word', Text.query.filter(Text.id == id_text).one().words.paginate(page=page, per_page=per_page))
        return Text.query.filter(Text.id == id_text).one().words.paginate(page=page, per_page=per_page)

    @staticmethod
    def get_words_from_pagination(pagination):
        words = pagination.items
        res = [
            {'id': wrd.id,
             'text': wrd.eng_word,
             'ts': wrd.ts,
             'tr': [{pos.pos: [tr.rus_word for tr in wrd.translated_words if pos == tr.pos]} for pos in
                    set(tr.pos for tr in wrd.translated_words)],
             'ex': [{pos.pos: [ex.example for ex in wrd.examples if pos == ex.pos]} for pos in
                    set(ex.pos for ex in wrd.examples)]}
            for wrd in words]
        return res
