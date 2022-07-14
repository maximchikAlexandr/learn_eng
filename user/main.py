from flask import render_template,Blueprint, abort, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from user.service import is_valid_data_user
from user.repository import userDB


user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='static')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # later create func "register_new_user" in service.py
        if is_valid_data_user(request.form['name'],
                           request.form['email'],
                           request.form['psw'],
                           request.form['psw2']):
            flash('Good job', category='success')
            hash_psw = generate_password_hash(request.form['psw'])
            userDB.add_new_user(username=request.form['name'],
                         email=request.form['email'],
                         hashpsw=hash_psw)

            return render_template('login.html')
        flash('Bad job', category='danger')

    return render_template('register.html')
