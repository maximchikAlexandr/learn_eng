from collections import namedtuple

from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from dct.repository import dictDB
from dct.service import sec_to_datetime

dct_bp = Blueprint('dct', __name__, template_folder='templates', static_folder='static')
txt_tpl = namedtuple('txt', ['title', 'datetime'])

@dct_bp.route('/main', methods=['GET', 'POST'])
@login_required
def index():
    texts = dictDB.get_list_of_texts(id_user=current_user.get_id())
    info_of_texts = [txt_tpl(title=txt.title, datetime=sec_to_datetime(txt.time)) for txt in texts]
    
    return render_template('dct/index.html',
                           title='Texts',
                           texts=info_of_texts)


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
