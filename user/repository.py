"""Realization of repository pattern"""

import math
import time

from user import db
from user.models import User


class Repository:
    def __init__(self, session_):
        self.__session = session_

    def add_new_user(self, username, email, hashpsw):
        tm = math.floor(time.time())  # Save time
        user = User(username=username, email=email, hash_psw=hashpsw, time=tm)

        self.__session.add(user)
        self.__session.commit()
        return True

    @staticmethod
    def get_user_by_mail(email):
        """
        Func return a object of class 'User'
        :param email: email of user in DB
        :return: object of class 'User'
        """
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_id(user_id):
        """
        Func return a object of class 'User'
        :param user_id: id of user in DB
        :return: object of class 'User'
        """
        return User.query.get(user_id)


repository = Repository(db.session)
