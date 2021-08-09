from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from application.data_models.post import Post
from application.data_models.user import User
from application.data_translators.user_translator import UserTranslator
from application.db_worker import FMongoDb
from pymongo import MongoClient
from application.app import app, ut, fdb


@app.route('/create_user', methods=['PUT'])
def create_user():
    if request.method == 'PUT':
        req = request.json
        usr = ut.to_mongo(ut.from_dict(req))
        fdb.add_user(usr)
        return '', 201  # Created


def publish_post():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
