from extensions import db
from user.models import User

class UserDB:

    def __init__(self, db):
        self.__db = db

    def add_new_user(self, username, email, hashpsw):
        user = User(username=username,
                    email=email,
                    hash_psw=hashpsw)

        self.__db.session.add(user)
        self.__db.session.commit()


userDB = UserDB(db)
