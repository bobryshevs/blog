from flask_pymongo import PyMongo
from application.data_models.user import User
from application.data_translators.user_translator import UserTranslator


class FMongoDb:
    def __init__(self, mongo_: PyMongo):
        self.__mongo = mongo_
        self.__db = mongo_.db
        self.__users_coll = mongo_.db['users']

    def add_user(self, user: dict) -> bool:
        self.__users_coll.insert_one(user)
        return True


if __name__ == '__main__':
    from application.app import mongo

    fdb = FMongoDb(mongo)
    ut = UserTranslator()
    usr = User(name='Guest')

    print(fdb.add_user(ut.to_mongo(usr)))
