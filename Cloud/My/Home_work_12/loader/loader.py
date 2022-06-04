import logging
from flask import Blueprint, render_template, request
from functions import update_dictionary, extens_correct

logging.basicConfig(level=logging.INFO)
logger_never_extens = logging.getLogger('never_extens')  # логгер, сигнализирующий о неверном формате файла
logger_not_file = logging.getLogger('not_file')  # логгер, сигнализирующий, что файл не был загружен
console_handler = logging.StreamHandler()
logger_never_extens.addHandler(console_handler)
logger_not_file.addHandler(console_handler)

loader_blueprint = Blueprint('loader_blueprint', __name__)


# обработка и загрузка данных из формы
@loader_blueprint.route("/post_uploaded.html", methods=["POST"])
def post_page():
    file = request.files.get('file')
    if file:
        text = request.values.get('text')
        filename = file.filename
        if extens_correct(filename):
            path = f"./uploads/images/{filename}"
            file.save(path)
            new_dict = {'pic': path, 'content': text}
            update_dictionary(new_dict)
            return render_template('post_uploaded.html', text=text, filename=filename)
        else:
            logger_never_extens.info('Попытка загрузить нестандартный файл')
            return '<h2>Файл не является изображением</h2>'
    else:
        logger_not_file.info('Файл не загружен')
        return '<h2>Файл не был загружен</h2>'
