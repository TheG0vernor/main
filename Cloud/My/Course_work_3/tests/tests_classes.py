from Cloud.My.Course_work_3.classes.posts import ClassPosts
from Cloud.My.Course_work_3.classes.comments import ClassComments



class TestsClass:

    def testing_get_posts_all(self):
        """Метод должен возвращать весь список словарей"""
        return_posts = ClassPosts.get_posts_all(ClassPosts())
        assert type(return_posts) == list, 'Метод get_posts_all вернул не список словарей'

    def testing_get_posts_all_short_content(self):
        """Метод должен возвращать список словарей с укороченным текстом"""
        return_short_posts = ClassPosts.get_posts_all_short_content(ClassPosts())
        assert type(return_short_posts) == list, 'Метод get_posts_all_short_content вернул не список словарей'

    def testing_get_posts_by_user(self):
        """Метод должен возвращать список словарей одного пользователя"""
        return_posts_by_user = ClassPosts.get_posts_by_user
        assert type(return_posts_by_user(ClassPosts(), 'leo')) == list, 'Метод get_posts_by_user вернул не список'
        assert return_posts_by_user(ClassPosts(), 'ыпыпыапр') == ValueError, 'Такого пользователя нет'

    def testing_search_for_posts(self):
        """Метод должен возвращать весь список словарей с найденными по ключевому слову постами"""
        return_posts = ClassPosts.search_for_posts
        assert type(return_posts(ClassPosts(), 'закат')) == list, 'Метод search_for_posts вернул не список'
        assert type(return_posts(ClassPosts(), 6)) == list, 'Тип данных (число в текст) не конвертирован'

    def testing_get_post_by_pk(self):
        """Метод должен возвращать один словарь по его идентификатору"""
        return_post = ClassPosts.get_post_by_pk
        assert return_post(ClassPosts(), 'два') == ValueError, 'Недопустимый тип данных'
        assert type(return_post(ClassPosts(), 2)) == dict, 'Метод get_post_by_pk вернул не словарь'

    def testing_get_comments_all(self):
        """Метод должен возвращать весь список словарей с комментариями"""
        return_comments = ClassComments.get_comments_all(ClassComments())
        assert type(return_comments) == list, 'Метод get_comments_all вернул не список'

    def testing_get_comments_by_post_id(self):
        """Метод должен возвращать список словарей с комментариями к одному посту"""
        return_comments_to_post = ClassComments.get_comments_by_post_id
        assert type(return_comments_to_post(ClassComments(), 1)) == list, 'Метод get_comments_by_post_id вернул не список'
        assert return_comments_to_post(ClassComments(), 10) == ValueError, 'Такого поста нет'
        assert return_comments_to_post(ClassComments(), 8) == [], 'Комментариев нет, но список не пуст'
        assert return_comments_to_post(ClassComments(), 'десять') == ValueError, 'Передан другой тип данных'

    def testing_get_comment_ending(self):
        """Метод должен возвращать слово с правильным окончанием для количества комментариев"""
        return_comment_ending = ClassComments.get_comment_ending
        assert type(return_comment_ending(ClassComments(), 1)) == str, 'Метод get_comment_ending вернул не слово'
        assert return_comment_ending(ClassComments(), 1) == 'комментарий', 'ошибка окончания'
        assert return_comment_ending(ClassComments(), 10) == 'комментариев', 'ошибка окончания'
        assert return_comment_ending(ClassComments(), 4) == 'комментария', 'ошибка окончания'

    def testing_get_write_views_count(self):
        """Метод не вернёт ничего. Производит запись в файл обновлённое значение ключа"""
        assert ClassPosts.get_write_views_count(ClassPosts(), 10) is None, 'Метод не должен ничего возвращать'

    def testing_get_dictionary_tag(self):
        """Метод должен возвращать словарь"""
        assert type(ClassPosts().get_dictionary_tag(ClassPosts().get_post_by_pk(5))) == dict, 'Метод вернул не словарь'

    def testing_get_all_dictionary_tag(self):
        """Метод должен возвращать список словарей по тегу"""
        assert type(ClassPosts().get_all_dictionary_tag('инста')) == list, 'Метод вернул не список'
