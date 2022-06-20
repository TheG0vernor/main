from flask import Flask
from Cloud.My.Course_work_3.posts.posts import posts_blueprint
from Cloud.My.Course_work_3.search.search import search_blueprint

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.register_blueprint(posts_blueprint)
app.register_blueprint(search_blueprint)


@app.errorhandler(404)  # обработка ошибки несуществующей страницы
def crash_404(c):
    return f'<h2>статус-код 404</h2>'


@app.errorhandler(500)  # обработка ошибки сервера
def crash_500(c):
    return f'<h2>статус-код 500</h2>'


if __name__ == '__main__':
    app.run()
