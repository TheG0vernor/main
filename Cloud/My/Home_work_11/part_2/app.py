import utils
from flask import Flask, render_template

# Объявим Flask

app = Flask(__name__)


@app.route('/')  # обозначим главную страницу со ссылками на кандидатов
def page_index():
    dictionary = utils.dictionary
    return render_template("list.html", dictionary=dictionary)


@app.route('/candidate/<int:x>')  # сами странички кандидатов
def candidate(x):
    if type(utils.return_dict(x)) != dict:  # если функция вернёт не словарь, значит такого кандидата нет
        return '<h3>Нет такого кандидата в базе</h3>'
    name_ = utils.return_dict(x)['name']  # имя кандидата
    position = utils.return_dict(x)['position']  # позиция кандидата
    url = utils.return_dict(x)['picture']  # картинка в переменной
    skills = utils.return_dict(x)['skills']  # навыки кандидата
    return render_template('card.html', name=name_, position=position, url=url, skills=skills)


@app.route('/search/<candidate_name>')  # поиск по именам кандидатов
def name_cand(candidate_name):
    if type(utils.search_name(candidate_name)) != list:  # если функция вернёт не список, значит такого кандидата нет
        return '<h1>Найдено кандидатов: 0</h1>'
    len_results = len(utils.search_name(candidate_name))  # количество найденных кандидатов
    results_dict = utils.search_name(candidate_name)  # список словарей с найденными кандидатами
    return render_template('search.html', results_dict=results_dict, len_results=len_results)


@app.route('/skill/<skill_name>')  # поиск по навыкам кандидатов
def skill_cand(skill_name):
    if type(utils.search_skills(skill_name)) != list:  # если функция вернёт не список, значит такого кандидата нет
        return '<h1>Найдено кандидатов: 0</h1>'
    len_results = len(utils.search_skills(skill_name))  # количество найденных кандидатов
    results_dict = utils.search_skills(skill_name)  # список словарей с найденными кандидатами
    return render_template('skill.html', results_dict=results_dict, len_results=len_results)


app.run(host='127.0.0.6', port=80)
