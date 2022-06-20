from Cloud.My.Course_work_3.classes.basic import Basic


class ClassComments(Basic):  # класс с методами, относящимися к комментариям

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии к определённому посту"""
        count = 0  # переменная-счётчик будет выше нуля, если пост присутствует
        for i in ClassComments().get_posts_all():  # проверка наличия поста
            if post_id == i['pk']:
                count += 1
        if count == 0:
            return ValueError  # если такого поста нет, вернуть ошибку
        list_posts_id_comments = []
        dictionary = ClassComments().get_comments_all()
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
        if len_comments == 1:
            return 'комментарий'
        elif 1 < len_comments < 5:
            return 'комментария'
        return 'комментариев'
