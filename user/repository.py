import math
import time

from flask import flash

from user import db
from user.models import User


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


class UserDB:

    def __init__(self, db):
        self.__db = db

    @_wapper_error('Error of DB: username is not unique')
    def add_new_user(self, username, email, hashpsw):
        tm = math.floor(time.time())  # Save time
        user = User(username=username,
                    email=email,
                    hash_psw=hashpsw,
                    time=tm)

        self.__db.session.add(user)
        self.__db.session.commit()
        return True

userDB = UserDB(db)
