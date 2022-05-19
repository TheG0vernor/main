def main():
    import utils
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def page_index():
        return f'<pre>{utils.data_string()}</pre>'

    @app.route('/candidates/<int:x>')
    def page_candidates(x):
        if type(utils.return_dict(x)) != dict:
            return 'Нет такого кандидата в базе'
        url = utils.return_dict(x)['picture']
        return f"<img src='{url}'>\n\n" \
               f"<pre>Имя кандидата - {utils.return_dict(x)['name']}\n" \
               f"Позиция кандидата - {utils.return_dict(x)['position']}\n" \
               f"Навыки - {utils.return_dict(x)['skills']}</pre>"

    @app.route('/skills/<x>')
    def page_skills(x):
        return f'<pre>{utils.search_skills(x)}</pre>'

    app.run(host='127.0.0.6', port=80)


main()
