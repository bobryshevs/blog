from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from application.data_models.post import Post
from application.data_models.user import User
from application.data_translators.user_translator import UserTranslator
from application.db_worker import FMongoDb
from pymongo import MongoClient


# Constants
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DATABASE_NAME = "blog_database"

app = Flask(__name__)
app.config['MONGO_URI'] = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DATABASE_NAME}"
app.config['MONGO_DBNAME'] = "blog_database"
app.config['SECRET_KEY'] = "SECRET"

ut = UserTranslator()
mongo = PyMongo(app)
fdb = FMongoDb(mongo)








if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=9001)
