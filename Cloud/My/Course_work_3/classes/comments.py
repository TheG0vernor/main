import json
from Cloud.My.Course_work_3.classes.posts import ClassPosts


class ClassComments:  # класс с методами, относящимися к комментариям
    def __init__(self, path='C:\Project_Python\Cloud\My\Course_work_3\data\comments.json', post_id=None, len_comments=0):
        self.len_comments = len_comments
        self.post_id = post_id
        self.path = path

    def get_comments_all(self):
        """Возвращает список словарей с комментариями"""
        with open(self.path, encoding='utf-8') as f:  # открыть файл с данными
            dictionary = json.load(f)
        return dictionary

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии к определённому посту"""
        self.post_id = post_id
        count = 0  # переменная-счётчик будет выше нуля, если пост присутствует
        for i in ClassPosts.get_posts_all(ClassPosts()):  # проверка наличия поста
            if post_id == i['pk']:
                count += 1
        if count == 0:
            return ValueError  # если такого поста нет, вернуть ошибку
        list_posts_id_comments = []
        dictionary = ClassComments.get_comments_all(ClassComments())
        for i in dictionary:  # найти комментарии к посту и добавить в список
            if post_id == i['post_id']:
                list_posts_id_comments.append(i)
        list_not_comments = []
        for i in list_posts_id_comments:  # если у поста нет комментариев, вернуть пустой список
            if i['comment'] == '':
                list_not_comments.append(i)
        if len(list_posts_id_comments) == len(list_not_comments):
            return []
        return list_posts_id_comments

    def get_comment_ending(self, len_comments):
        """Возвращает слово с правильным окончанием для количества комментариев"""
        self.len_comments = len_comments
        if len_comments == 1:
            return 'комментарий'
        elif 1 < len_comments < 5:
            return 'комментария'
        return 'комментариев'
