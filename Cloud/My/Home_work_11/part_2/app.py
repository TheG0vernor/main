import utils
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def page_index():
    dictionary = utils.dictionary
    return render_template("list.html", dictionary=dictionary)


@app.route('/candidates/<int:x>')
def candidate(x):
    # if type(utils.return_dict(x)) != dict:  # если функция вернёт не словарь, значит такого кандидата нет
    #     return 'Нет такого кандидата в базе'
    name = utils.return_dict(x)['name']  # имя кандидата
    position = utils.return_dict(x)['position']  # позиция кандидата
    url = utils.return_dict(x)['picture']  # картинка в переменной
    skills = utils.return_dict(x)['skills']  # навыки кандидата
    return render_template('card.html', name=name, position=position, url=url, skills=skills)


app.run(host='127.0.0.6', port=80)
