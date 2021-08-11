from flask import Flask, jsonify, request, render_template
from flask.helpers import url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from models.post import Post
from translators.post_tranlator import PostTranslator
from db_worker import FMongoDb
from blueprints.post import post
from blueprints.comment import comment



# Constants


app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET"

app.register_blueprint(post, url_prefix='/post')
app.register_blueprint(comment, url_prefix='/comment')




@app.route('/')
def index():
    return render_template('base.html', title='Custom Title', menu=['Posts'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9002)
