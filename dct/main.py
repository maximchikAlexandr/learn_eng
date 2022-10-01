"""
Create Blueprint 'dct'. This BP solves the following tasks:
- add new text from user form
- find all unique words in a new text
- get translate to russian from english
- saving all data in \data\dct_eng.db
"""


from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from dct import db
from dct.repository import TextRepository, Pagination
from dct.service import sec_to_datetime, get_words_from_pagination

dct_bp = Blueprint('dct', __name__, template_folder='templates', static_folder='static')
PER_PAGE_TEXTS = 6
PER_PAGE_WORDS = 15

@dct_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    page = request.args.get('page')
    page = int(page) if page and page.isdigit() else 1
    pages = Pagination.pagination_for_texts(id_user=current_user.get_id(),
                                page=page,
                                per_page=PER_PAGE_TEXTS)

    dates = {txt.id : sec_to_datetime(txt.time) for txt in pages.items}
    
    return render_template('dct/index.html',
                           title='Texts',
                           pages=pages,
                           dates=dates)


@dct_bp.route('/add_text', methods=['GET', 'POST'])
@login_required
def add_text():
    if request.method == 'POST':
        if request.form['text'] and request.form['title']:
            text = TextRepository(db.session,
                                    text=request.form['text'],
                                    title=request.form['title'])
            text.save()
            flash('Text added successfully', category='success')
        else:
            flash('Please fill all fields', category='danger')

    return render_template('dct/add_text.html', title='Adding a new text')


@dct_bp.route('/remove_text-<int:id_text>', methods=['GET', 'POST'])
@login_required
def remove_text(id_text):
    TextRepository.remove_text(db.session, id_text=id_text)
    return redirect(url_for('.index'))

@dct_bp.route('/show_text-<int:id_text>', methods=['GET', 'POST'])
@login_required
def show_text(id_text):
    page = request.args.get('page')
    page = int(page) if page and page.isdigit() else 1
    pages = Pagination.pagination_for_words(id_text=id_text,
                                page=page,
                                per_page=PER_PAGE_WORDS)

    words = get_words_from_pagination(pagination=pages)
    current_text = TextRepository.get_text(id_text=id_text)
    return render_template('dct/show_text.html',
                           words=words,
                           text=current_text,
                           pages=pages,
                           title='Text')
