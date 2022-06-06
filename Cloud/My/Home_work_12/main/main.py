from flask import Blueprint, render_template, request
from functions import get_json_search

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/")  # главная страница, форма поиска
def page():
    return render_template('index.html')


@main_blueprint.route("/index.html")
def page_index():
    return render_template('index.html')


@main_blueprint.route("/post_form.html", methods=["GET", "POST"])  # форма для отправки данных
def page_post_form():
    text = request.values.get('text')
    file = request.files.get('file')
    return render_template('post_form.html', file=file, text=text)


@main_blueprint.route("/search")  # поиск данных
def main_page():
    s = request.args.get('s')
    content = get_json_search(s)
    return render_template('post_list.html', content=content, s=s)
