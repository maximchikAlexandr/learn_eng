from flask import render_template,Blueprint, abort

user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='static')

@user_bp.route('/login')
def login():
    try:
        return render_template('login.html')
    except:
        abort(404)