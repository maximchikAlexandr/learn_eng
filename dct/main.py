from flask import Blueprint, render_template
from flask_login import login_required


dct_bp = Blueprint('dct', __name__, template_folder='templates', static_folder='static')

@dct_bp.route('/main', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('dct/index.html')


@dct_bp.route('/list', methods=['GET', 'POST'])
@login_required
def list():
    return 'list'

@dct_bp.route('/add_text', methods=['GET', 'POST'])
@login_required
def add_text():
    return 'Add text'

@dct_bp.route('/show_text', methods=['GET', 'POST'])
@login_required
def show_text():
    return render_template('dct/show_text.html', words=words)
