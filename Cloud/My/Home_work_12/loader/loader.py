from flask import Blueprint, render_template, request, send_from_directory
from functions import update_dictionary, extens_correct
from logger import logger_not_file

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


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
            logger_not_file.info('Попытка загрузить нестандартный файл')
            return '<h2>Файл не является изображением</h2>'
    else:
        logger_not_file.info('Файл не загружен')
        return '<h2>Файл не был загружен</h2>'


@loader_blueprint.route("/uploads/<path:path>")  # делает загруженные файлы доступными
def static_dir(path):
    return send_from_directory("uploads", path)
