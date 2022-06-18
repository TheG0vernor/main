import json


class ClassPosts:  # класс с методами, относящимися к постам
    def __init__(self, path='C:\Project_Python\Cloud\My\Course_work_3\data\data.json', username=None, query=None, pk=None):
        self.pk = pk
        self.query = query
        self.username = username
        self.path = path

    def get_posts_all(self):
        """Возвращает список словарей с постами"""
        with open(self.path, encoding='utf-8') as f:  # открыть файл с данными
            dictionary = json.load(f)
        return dictionary

    def get_posts_all_short_content(self):
        """Возвращает список словарей с постами, в которых укорочен контент"""
        dict_short = []
        for i in ClassPosts.get_posts_all(ClassPosts()):
            i['content'] = i['content'][:50]+'...'
            dict_short.append(i)
        return dict_short

    def get_posts_by_user(self, user_name):
        """Возвращает посты определённого пользователя"""
        self.username = user_name
        list_user_posts = []
        dictionary = ClassPosts.get_posts_all(ClassPosts())
        for i in dictionary:  # найти посты пользователя и добавить в список
            if user_name in i['poster_name']:
                i['content'] = i['content'][:50]+'...'
                list_user_posts.append(i)
        list_not_posts = []
        for i in list_user_posts:  # если у пользователя нет постов, вернуть пустой список
            if i['content'] == '':
                list_not_posts.append(i)
        if len(list_user_posts) == len(list_not_posts) and len(list_user_posts) != 0:
            return []
        if len(list_user_posts) == 0:  # если пользователя нет, вернуть ошибку
            return ValueError
        return list_user_posts

    def search_for_posts(self, query):
        """Возвращает посты по ключевому слову"""
        self.query = query
        dictionary = ClassPosts.get_posts_all(ClassPosts())
        list_posts = []
        query = str(query)
        for i in dictionary:
            if query.lower() in i['content'].lower():
                i['content'] = i['content'][:50]+'...'
                list_posts.append(i)
        return list_posts[:10]

    def get_post_by_pk(self, pk):
        """Возвращает 1 пост по его идентификатору"""
        self.pk = pk
        dictionary = ClassPosts.get_posts_all(ClassPosts())
        for i in dictionary:
            if pk == i['pk']:
                return i
        return ValueError

    def get_write_views_count(self, pk):
        """Обновляет количество просмотров"""
        with open(self.path, encoding='utf-8') as f:  # открыть файл с данными
            dictionary = json.load(f)
            for i in dictionary:
                if pk == i['pk']:
                    i['views_count'] = i['views_count'] + 1

        with open(self.path, 'w', encoding='utf-8') as f:  # записать файл с данными
            json.dump(dictionary, f, ensure_ascii=False)

    def get_dictionary_tag(self, dictionary):
        """Принимает и возвращает словарь с исправленными тегами"""
        if '#' in dictionary['content']:
            data_new = []
            for i in dictionary['content'].split(' '):
                if '#' in i[0]:
                    i = f'<a href="/tag/{i[1:]}">{i}</a>'
                    data_new.append(i)
                else:
                    data_new.append(i)
            dictionary['content'] = (' '.join(data_new))
        return dictionary

    def get_all_dictionary_tag(self, tag):
        """Ищет и возвращает список словарей с тегом"""
        data = []
        for i in ClassPosts().get_posts_all():
            if f'#{tag}' in i['content']:
                i['content'] = i['content'][:50] + '...'
                data.append(i)
        return data
