from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from user.service import check_data_user
from user.repository import userDB


user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='static')
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message = 'Please login to access this page'
login_manager.login_message_category = 'success'


@login_manager.user_loader
def load_user(user_id):
    return userDB.get_user_by_id(user_id)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']

        if email and password:
            user = userDB.get_user_by_mail(email=email)
            rm = True if request.form.get('remainme') else False
            if user and check_password_hash(user.hash_psw, password):
                login_user(user, remember=rm)
                return redirect(url_for('index'))
            flash('Password or email are not corect', category='danger')
    return render_template('user/login.html', title='Please login')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        check_dct = check_data_user(request)

        # if data in form is correct
        if check_dct['valid_data']:
            hash_psw = generate_password_hash(request.form['psw'])
            if userDB.add_new_user(username=request.form['name'],
                         email=request.form['email'],
                         hashpsw=hash_psw):
                flash(f'User «{request.form["name"]}» is registred in the site',
                      category='success')
                return render_template('user/login.html', title='Please login')

        # if data in form is not correct
        if check_dct['flashed_messages']:
            for msg in check_dct['flashed_messages']:
                flash(msg, category='danger')

    return render_template('user/register.html', title='Registration')

@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))
