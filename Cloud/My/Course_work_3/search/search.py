from flask import Blueprint, render_template, request, jsonify
from Cloud.My.Course_work_3.classes.posts import ClassPosts
from Cloud.My.Course_work_3.logger import logger_api

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/search/')  # поиск постов по ключевому слову
def page_search():
    search = request.args.get('s')
    result_search = ClassPosts().search_for_posts(search)
    length_results = len(result_search)
    return render_template('search.html', result_search=result_search, length=length_results, s=search)


@search_blueprint.route('/users/<username>')  # посты выбранного пользователя
def page_user_posts(username):
    posts_user = ClassPosts().get_posts_by_user(username)
    return render_template('user-feed.html', posts_user=posts_user)


@search_blueprint.route('/tag/<tag_name>')  # посты по выбранному тегу
def page_tags(tag_name):
    data = ClassPosts().get_all_dictionary_tag(tag_name)
    return render_template('tag.html', data=data, tag=tag_name)


@search_blueprint.route('/api/posts/')  # api запрос ко всему списку словарей
def api_posts():
    logger_api.info('Запрос /api/posts')
    dictionary = ClassPosts().get_posts_all()
    return jsonify(dictionary)


@search_blueprint.route('/api/posts/<int:post_id>')  # api запрос к одному словарю
def api_post_id(post_id):
    logger_api.info(f'Запрос /api/posts/{post_id}')
    dictionary = ClassPosts().get_post_by_pk(post_id)
    return jsonify(dictionary)
