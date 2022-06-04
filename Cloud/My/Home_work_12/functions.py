import json


def return_dictionary():
    """Возвращает список словарей с данными"""
    with open('posts.json', encoding='utf-8') as f:
        dictionary = json.load(f)
        return dictionary


def get_json_search(arg):
    """Вернёт словарь подходящий результатам поиска"""
    new_list = []
    for i in return_dictionary():
        if arg.lower() in i['content'].lower():
            new_list.append(i)
    return new_list


def update_dictionary(dict_):
    """Запишет словарь с новыми данными в список словарей"""
    with open('posts.json', 'r', encoding='utf-8') as f:
        dictionary = json.load(f)

    with open('posts.json', 'w', encoding='utf-8') as f:
        dictionary.append(dict_)
        json.dump(dictionary, f, ensure_ascii=False)


def extens_correct(filename):
    """Определит расширение файла на соответствие требованиям"""
    all_extens = {'jpg', 'png', 'bmp'}
    extension = filename.split('.')[-1]
    if extension in all_extens:
        return True
    return False
