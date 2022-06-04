from flask import Blueprint, render_template, request
from functions import get_json_search

main_blueprint = Blueprint('main_blueprint', __name__)


# поиск данных
@main_blueprint.route("/search")
def main_page():
    s = request.args.get('s')
    content = get_json_search(s)
    return render_template('post_list.html', content=content, s=s)
