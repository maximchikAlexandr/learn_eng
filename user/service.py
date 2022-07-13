def _is_valid_password(password: str) -> bool:
    """
    Проверяет пароль на валидность
    :param password: password of a user
    :return: return True if password is valid, False otherwise
    """
    num_list = [ch for ch in password if ch in '0123456789']
    check_list = (len(password) > 3,
                  len(num_list) > 3,
                  password != password.lower(),
                  password != password.upper(),
                  password.isascii())
    return all(check_list)


def is_valid_data_user(username: str, email: str, psw: str, psw2: str) -> bool:
    check_list = (len(username) > 3,
                  '@' in email,
                  psw == psw2,
                  _is_valid_password(psw))
    return all(check_list)