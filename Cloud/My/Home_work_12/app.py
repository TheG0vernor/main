from flask import Flask
from main.main import main_blueprint
from loader.loader import loader_blueprint
from logger import logger_not_file


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.errorhandler(500)  # обработка ошибки сервера
def crash_500(c):
    logger_not_file.error('Обнаружено отсутствие файла')
    return f'<h2>Файл с данными не найден</h2>'


app.run()
