from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
from application.data_models.post import Post
from application.data_models.user import User
from application.data_translators.user_translator import UserTranslator
from application.db_worker import FMongoDb
from pymongo import MongoClient
from application.app import app, ut, pt, fdb


@app.route('/create_user', methods=['POST'])
def create_user():
    req = request.json
    usr = ut.to_mongo(ut.from_dict(req))
    fdb.add_user(usr)
    return '', 201  # Created


@app.route('/publish_post', methods=['POST'])
def publish_post():
    req = request.json
    post = pt.to_mongo(pt.from_dict(req))
    fdb.insert_post(post)
    return '', 201


@app.route('/get_posts', methods=['GET'])
def get_posts():
    posts = fdb.get_posts(page_number=request.args.get('page_number'),
                          page_size=request.args.get('page_size'))
    return jsonify([pt.to_mongo(pt.from_mongo(post)) for post in posts]), 200


@app.route('/get_post_by_id', methods=['GET'])
def get_post_by_id():
    post_id = request.args.get('post_id')
    return jsonify(pt.to_mongo(
        pt.from_mongo(fdb.get_post_by_id(post_id=post_id)))), 200


@app.route('/')
def index():
    return render_template('base.html', title='Custom Title', menu=['Posts'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)
