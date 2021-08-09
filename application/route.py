from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from application.data_models.post import Post
from application.data_models.user import User
from application.data_translators.user_translator import UserTranslator
from application.db_worker import FMongoDb
from pymongo import MongoClient
from application.app import app, ut, pt, fdb


@app.route('/create_user', methods=['PUT'])
def create_user():
    if request.method == 'PUT':
        req = request.json
        usr = ut.to_mongo(ut.from_dict(req))
        fdb.add_user(usr)
        return '', 201  # Created


@app.route('/publish_post', methods=['PUT'])
def publish_post():
    if request.method == 'PUT':
        req = request.json
        post = pt.to_mongo(pt.from_dict(req))
        fdb.insert_post(post)
        return '', 201


@app.route('/get_posts', methods=['GET'])
def get_posts():
    if request.method == 'GET':
        req = request.json
        posts = fdb.get_posts(page_number=req['page_number'], page_size=req['page_size'])
        return jsonify([pt.to_mongo(pt.from_mongo(post)) for post in posts]), 200



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
