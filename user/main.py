from flask import render_template,Blueprint, abort, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from user.service import check_data_user
from user.repository import userDB


user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='static')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        check_dct = check_data_user(request)

        # if data in form is correct
        if check_dct['password_ok']:
            hash_psw = generate_password_hash(request.form['psw'])
            if userDB.add_new_user(username=request.form['name'],
                         email=request.form['email'],
                         hashpsw=hash_psw):
                flash(f'User «{request.form["name"]}» is registred in the site',
                      category='success')
                return render_template('login.html')

        # if data in form is not correct
        if check_dct['flashed_messages']:
            for msg in check_dct['flashed_messages']:
                flash(msg, category='danger')

    return render_template('register.html')
