def _searching_error(username: str, email: str, psw: str, psw2: str) -> dict:

    # calculating the length
    min_len_name_error = len(username) < 4
    max_len_name_error = len(username) > 20
    min_len_psw_error = len(psw) < 6
    max_len_psw_error = len(psw) > 20

    equal_psw_error = psw != psw2 # check equal passwords
    digit_error = len([ch for ch in psw if str(ch) in '0123456789']) < 3 # searching for digits
    uppercase_error = psw == psw.lower() # searching for uppercase
    lowercase_error = psw == psw.upper() # searching for lowercase
    ascii_error = not psw.isascii()  #  searching for ascii
    unique_symbols_error = len(set(psw)) / len(psw) < 0.75 # check count of a unique symbols

    return  {
        'max_len_psw_error' : max_len_psw_error,
        'min_len_psw_error': min_len_psw_error,
        'max_len_name_error': max_len_name_error,
        'min_len_name_error': min_len_name_error,
        'digit_error' : digit_error,
        'equal_psw_error' : equal_psw_error,
        'uppercase_error' : uppercase_error,
        'lowercase_error' : lowercase_error,
        'ascii_error' : ascii_error,
        'unique_symbols_error' : unique_symbols_error
    }

def check_data_user(request)  -> dict:

    check_dct = _searching_error(request.form['name'],
                                request.form['email'],
                                request.form['psw'],
                                request.form['psw2'])

    flashed_messages = {
        'max_len_psw_error' : 'Max length of password is 20 symbols',
        'min_len_psw_error': 'Min length of password is 6 symbols',
        'max_len_name_error': 'Max length of username is 20 symbols',
        'min_len_name_error': 'Min length of username is 4 symbols',
        'digit_error' : 'Password must contain 3 or more digits',
        'equal_psw_error' : 'Passwords is not equal',
        'uppercase_error' : 'Password must contain 1 or more symbols in upercase',
        'lowercase_error' : 'Password must contain 1 or more symbols in lowercase',
        'ascii_error' : 'Password contain only from ascii symbols',
        'unique_symbols_error' : 'More 75% of symbols in password must be unique'
    }

    return {
        'valid_data' : not any(check_dct.values()),
        'flashed_messages' : [flashed_messages[key] for key, value in check_dct.items() if value]
    }
