import logging
api_log = 'api.log'
logging.basicConfig(level=logging.INFO)
logger_api = logging.getLogger('Вызываемый')  # объявим логгер
FileHandler = logging.FileHandler(f'C:\Project_Python\Cloud\My\Course_work_3\logs\\api.log')  # объявим хэндлер
formatter_one = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')  # объявим форматирование
FileHandler.setFormatter(formatter_one)  # применим форматирование к хэндлеру
logger_api.addHandler(FileHandler)  # применим хэндлер к логгеру
