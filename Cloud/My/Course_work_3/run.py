from flask import Flask, render_template, request, jsonify
from Cloud.My.Course_work_3.classes.posts import ClassPosts
from Cloud.My.Course_work_3.classes.comments import ClassComments
from Cloud.My.Course_work_3.logger import logger_api


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/')  # главная страница
def page_index():
    dictionary = ClassPosts().get_posts_all_short_content()  # список словарей с данными
    return render_template('index.html', dictionary=dictionary)


@app.route('/posts/<int:post_id>')  # отображение подробной информации о посте
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


@app.route('/search/')  # поиск постов по ключевому слову
def page_search():
    search = request.args.get('s')
    result_search = ClassPosts().search_for_posts(search)
    length_results = len(result_search)
    return render_template('search.html', result_search=result_search, length=length_results, s=search)


@app.route('/users/<username>')  # посты выбранного пользователя
def page_user_posts(username):
    posts_user = ClassPosts().get_posts_by_user(username)
    return render_template('user-feed.html', posts_user=posts_user)


@app.route('/tag/<tag_name>')  # посты по выбранному тегу
def page_tags(tag_name):
    data = ClassPosts().get_all_dictionary_tag(tag_name)
    return render_template('tag.html', data=data, tag=tag_name)


@app.route('/api/posts/')  # api запрос ко всему списку словарей
def api_posts():
    logger_api.info('Запрос /api/posts')
    dictionary = ClassPosts().get_posts_all()
    return jsonify(dictionary)


@app.route('/api/posts/<int:post_id>')  # api запрос к одному словарю
def api_post_id(post_id):
    logger_api.info(f'Запрос /api/posts/{post_id}')
    dictionary = ClassPosts().get_post_by_pk(post_id)
    return jsonify(dictionary)


@app.errorhandler(404)  # обработка ошибки несуществующей страницы
def crash_404(c):
    return f'<h2>статус-код 404</h2>'


@app.errorhandler(500)  # обработка ошибки сервера
def crash_500(c):
    return f'<h2>статус-код 500</h2>'


if __name__ == '__main__':
    app.run()
