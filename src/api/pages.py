from flask import Blueprint, render_template, redirect


bp = Blueprint('site',__name__)



@bp.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/', methods=['GET'])
def back_to_main_page():
    return redirect('/index.html', code=301)