import logging

logging.basicConfig(level=logging.INFO)
logger_not_file = logging.getLogger('not_file')
# логгер, сигнализирующий об ошибках при работе с файлом данных или загрузке файла изображения
