from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from data_models.user import User
from data_translators.user_translator import UserTranslator
from data_translators.post_tranlator import PostTranslator


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

    def get_post_by_id(self, post_id: str) -> dict:
        return self.__posts_coll.find_one({'_id': ObjectId(post_id)})


if __name__ == '__main__':
    from app import mongo

    fdb = FMongoDb(mongo)
    ut = UserTranslator()
    pt =PostTranslator()
    usr = User(name='Guest')

    post = fdb.get_post_by_id(post_id='6111371a6e34b54502afbf3d')

