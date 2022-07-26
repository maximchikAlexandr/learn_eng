from flask import Blueprint, render_template, request, flash
from flask_login import login_required

from dct.repository import dictDB

dct_bp = Blueprint('dct', __name__, template_folder='templates', static_folder='static')

@dct_bp.route('/main', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('dct/index.html')


@dct_bp.route('/add_text', methods=['GET', 'POST'])
@login_required
def add_text():
    if request.method == 'POST':
        if request.form['text'] and request.form['title']:
            dictDB.add_text(text = request.form['text'],
                            title = request.form['title'])
            flash('Text added successfully', category='success')
        else:
            flash('Please fill all fields', category='danger')

    return render_template('dct/add_text.html', title='Adding a new text')

@dct_bp.route('/show_text', methods=['GET', 'POST'])
@login_required
def show_text():
    return render_template('dct/show_text.html')
