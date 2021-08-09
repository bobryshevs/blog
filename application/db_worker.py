from flask_pymongo import PyMongo
from application.data_models.user import User
from application.data_translators.user_translator import UserTranslator
from application.data_translators.post_tranlator import PostTranslator


class FMongoDb:
    def __init__(self, mongo_: PyMongo):
        self.__mongo = mongo_
        self.__db = mongo_.db
        self.__users_coll = mongo_.db['users']
        self.__posts_coll = mongo_.db['posts']

    def add_user(self, user: dict) -> bool:
        self.__users_coll.insert_one(user)
        return True

    def insert_post(self, post: dict) -> bool:
        self.__posts_coll.insert_one(post)
        return True

    def get_posts(self, page_number: int, page_size: int) -> list:
        posts = self.__posts_coll.find().sort('_id', -1).skip(page_number*page_size - page_size).limit(page_size)
        return list(posts)


if __name__ == '__main__':
    from application.app import mongo

    fdb = FMongoDb(mongo)
    ut = UserTranslator()
    pt =PostTranslator()
    usr = User(name='Guest')

    a = [pt.to_mongo(pt.from_mongo(i)) for i in list(fdb.get_posts(page_number=2, page_size=2))]
    print(a)
