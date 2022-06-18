from Cloud.My.Course_work_3.run import app
from Cloud.My.Course_work_3.classes.posts import ClassPosts


class TestApi:

    def testing_api_posts(self):
        data = ClassPosts().get_posts_all()
        assert type(app.test_client().get('/api/posts', follow_redirects=True).json) == list, 'Возвращён не list'
        assert app.test_client().get('/api/posts', follow_redirects=True).json[3].keys() == data[7].keys(), 'Ключи в словарях отличаются'

    def testing_api_post_id(self):
        post_id = 2
        data = ClassPosts().get_post_by_pk(post_id)
        assert type(app.test_client().get(f'/api/posts/{post_id}', follow_redirects=True).json) == dict, 'Возвращён не dict'
        assert app.test_client().get(f'/api/posts/{post_id}', follow_redirects=True).json.keys() == data.keys(), 'Ключи в словаре отличаются'
