from flask import Blueprint

dct_bp = Blueprint('dct', __name__, template_folder='templates', static_folder='static')

@dct_bp.route('/list', methods=['GET', 'POST'])
def list():
    return 'list'

@dct_bp.route('/add_text', methods=['GET', 'POST'])
def add_text():
    return 'Add text'
