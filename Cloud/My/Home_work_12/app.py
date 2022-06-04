import logging
from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint

logging.basicConfig(level=logging.ERROR)
logger_not_dict = logging.getLogger('not_dict')  # логгер, сигнализирующий об отсутствии файла
console_handler = logging.StreamHandler()
logger_not_dict.addHandler(console_handler)


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/")
def page():
    return render_template('index.html')


@app.route("/index.html")
def page_index():
    return render_template('index.html')


@app.route("/")  # возвращает блюпринт поиска и отображения фото с сопровождающим текстом
def page_tag():
    return main_blueprint


@app.route("/post_form.html", methods=["GET", "POST"])  # форма для отправки данных
def page_post_form():
    text = request.values.get('text')
    file = request.files.get('file')
    return render_template('post_form.html', file=file, text=text)


@app.route("/")  # возвращает блюпринт загрузки файла и сопровождающего текста
def page_post_upload():
    return loader_blueprint


@app.route("/uploads/<path:path>")  # делает загруженные файлы доступными
def static_dir(path):
    return send_from_directory("uploads", path)


@app.errorhandler(500)  # обработка ошибки сервера
def crash_500(c):
    logger_not_dict.error('Обнаружено отсутствие файла')
    return f'<h2>Файл с данными не найден</h2>', 500


app.run()
