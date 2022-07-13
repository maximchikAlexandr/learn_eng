from flask import render_template,Blueprint, abort, request, flash, current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from user.service import is_valid_data_user
# from user.repository import UserDB

user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='static')
# userDB = UserDB(db)



@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if is_valid_data_user(request.form['name'],
                           request.form['email'],
                           request.form['psw'],
                           request.form['psw2']):
            flash('Good job', category='success')
            hash_psw = generate_password_hash(request.form['psw'])
            # # userDB.add_new_user(request.form['name'],
            #                request.requestform['email'],
            #                     hash_psw)

            return render_template('login.html')
        flash('Bad job', category='danger')

    return render_template('register.html')

