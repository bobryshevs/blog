from pymongo import MongoClient
from repositories.posts_repository import PostRepository

MONGO_HOST = "localhost"
MONGO_PORT = 27017

mongo_client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")

post_repository = PostRepository(client=mongo_client)
