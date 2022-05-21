import json


def data_string():
    """Вернёт данные по кандидатам в строке"""
    dict_string = ''
    for i in dictionary:
        dict_string += f"Имя кандидата - {i['name']}\n" \
                       f"Позиция кандидата - {i['position']}\n" \
                       f"Навыки - {i['skills']}\n\n"
    return dict_string[:-2]


def return_dict(id_):
    """Получение словаря из списка словарей по id"""
    for i in dictionary:
        if i['id'] == id_:
            return i


def search_skills(skill):
    """Получение кандидатов с навыком"""
    cand_skill = ''
    for i in dictionary:
        if skill.lower() in i['skills'].lower():
            cand_skill += f"Имя кандидата - {i['name']}\n" \
                          f"Позиция кандидата - {i['position']}\n" \
                          f"Навыки - {i['skills']}\n\n"
            return cand_skill[:-2]
    else:
        return 'Нет кандидата с таким навыком'
#     для точного поиска по навыку с 26 строки:
#             for j in i['skills'].lower().split(', '):
#                 if j == skill.lower():
#                     cand_skill += f"Имя кандидата - {i['name']}\n" \
#                                   f"Позиция кандидата - {i['position']}\n" \
#                                   f"Навыки - {i['skills']}\n\n"
#     if cand_skill != '':
#         return cand_skill[:-2]
#     else:
#         return 'Нет кандидата с таким навыком'


#  загрузим словарь с данными
file = open('candidates.json')
dictionary = json.loads(file.read())
file.close()
