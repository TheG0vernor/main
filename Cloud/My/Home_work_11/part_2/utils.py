import json


def return_dict(id_):
    """Получение словаря кандидата по id"""
    for i in dictionary:
        if i['id'] == id_:
            return i


def search_skills(skill):
    """Получение списка словарей кандидатов с подходящим скиллом"""
    cand_list_dict = []
    for i in dictionary:
        if skill.lower() in i['skills'].lower():
            cand_list_dict.append(i)
    return cand_list_dict


def search_name(name):
    """Получение списка словарей кандидатов с подходящим именем"""
    cand_list_dict = []
    for i in dictionary:
        if name.lower() in i['name'].lower():
            cand_list_dict.append(i)
    return cand_list_dict


#  загрузим словарь с данными
file = open('candidates.json')
dictionary = json.loads(file.read())
file.close()
