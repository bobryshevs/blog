from pymongo import MongoClient
from datetime import datetime
MONGO_HOST = "localhost"
MONGO_PORT = 27017

mongo_client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")

col = mongo_client.blog_database.posts

print(col.insert_one({"date": datetime.now()}))

