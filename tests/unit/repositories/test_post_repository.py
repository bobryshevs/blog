from pymongo import MongoClient
from repositories.posts_repository import PostRepository 


class Constants:
    MONGO_HOST = "localhost"
    MONGO_PORT = 27017
    mongo_client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
    


class TestPostRepository:
    '''
    Один и тот же метод может по-разному отработать
    в зависимости от входных данных...
    '''

    @classmethod
    def setup_class(self):
        self.post_repository = PostRepository(Constants.mongo_client)


    @classmethod
    def teardown_class(self):
        pass


    def test_get_post_pages(self):
        """
        Eсли в базе не
        """
        


