from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
from models.post import Post
from translators.post_tranlator import PostTranslator
from db_worker import FMongoDb
from pymongo import MongoClient


# Constants
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DATABASE_NAME = "blog_database"

app = Flask(__name__)
app.config['MONGO_URI'] = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DATABASE_NAME}"
app.config['MONGO_DBNAME'] = "blog_database"
app.config['SECRET_KEY'] = "SECRET"


mongo = PyMongo(app)
fdb = FMongoDb(mongo)



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
    posts = fdb.get_posts(page_number=request.args.get('page_number', type=int),
                          page_size=request.args.get('page_size', type=int))
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

