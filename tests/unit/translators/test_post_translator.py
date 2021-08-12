import pytest
from pymongo import MongoClient
from bson import ObjectId
from translators import PostTranslator
from models import Post


@pytest.fixture(scope="function")
def post_translator():
    return PostTranslator()


@pytest.fixture(scope='module')
def posts_collection():
    MONGO_HOST = "localhost"
    MONGO_PORT = 27017
    mongo_client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
    yield mongo_client.blog_database.posts
    mongo_client.close()



@pytest.fixture(scope="function")
def dict_post_and_mongo_post(posts_collection):
    post = {
        "text":"Text for mongo_post_fixture",
        "author":"Sviatoslav Bobryshev",
        "date_of_creation":"2021-08-11T16:52:25.551959"
    }
    m_id = posts_collection.insert_one(post).inserted_id
    post['_id'] = str(m_id)
    m_post = posts_collection.find_one({"_id": ObjectId(m_id)})
    yield post, m_post
    posts_collection.delete_one({'_id': ObjectId(m_id)})
    
    


def test_to_mongo_valid(post_translator):
    post = Post(
        text="Text for post",
        author="Sviatoslav Bobryshev",
        date_of_creation="2021-08-11T16:52:25.551959"
    )

    expected = {
        "text": "Text for post",
        "author": "Sviatoslav Bobryshev",
        "date_of_creation": "2021-08-11T16:52:25.551959"
    }

    current = post_translator.to_mongo(post)

    assert expected == current, \
        "PostTranslator.to_mongo returns INVALID dict"



def test_from_mongo_valid(dict_post_and_mongo_post,
                          post_translator):
    dict_post, mongo_post = dict_post_and_mongo_post
    expected = Post(
        m_id=dict_post['_id'],
        text=dict_post['text'],
        author=dict_post['author'],
        date_of_creation=dict_post['date_of_creation']
    )
    print(type(expected.m_id))

    current = post_translator.from_mongo(mongo_post)

    assert expected.is_equal(current), \
        'PostTranslator.from_mongo returns INVALID Post object'

    
    
