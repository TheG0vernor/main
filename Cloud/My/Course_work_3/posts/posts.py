from flask import Blueprint, render_template
from Cloud.My.Course_work_3.classes.posts import ClassPosts
from Cloud.My.Course_work_3.classes.comments import ClassComments

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')


@posts_blueprint.route('/')  # главная страница
def page_index():
    dictionary = ClassPosts().get_posts_all_short_content()  # список словарей с данными
    return render_template('index.html', dictionary=dictionary)


@posts_blueprint.route('/posts/<int:post_id>')  # отображение подробной информации о посте
def page_posts(post_id):
    comments = ClassComments().get_comments_by_post_id(post_id)  # список словарей с комментариями
    dictionary = ClassPosts().get_post_by_pk(post_id)  # словарь с подробной информацией о посте
    dictionary = ClassPosts().get_dictionary_tag(dictionary)  # словарь с исправленными тегами (если они есть)
    len_comments = len(ClassComments().get_comments_by_post_id(post_id))  # количество комментариев
    comment_ending = ClassComments().get_comment_ending(len_comments)
    ClassPosts().get_write_views_count(post_id)  # обновит количество просмотров
    if len_comments == 0:
        len_comments = 'Нет'
    return render_template('post.html', comments=comments, dictionary=dictionary, len_comments=len_comments,
                           comment_ending=comment_ending)
