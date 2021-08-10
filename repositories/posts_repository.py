from os import O_NDELAY
import bson
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId

from models.post import Post


class PostRepository:
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = client.blog_database
        self.collection = client.blog_database.posts

    def get_post_by_id(self, post_id: str) -> dict:
        try:
            post_id = ObjectId(post_id)
        except InvalidId as err:
            return f'400 {err}', 400

        post = self.collection.find_one({"_id": ObjectId(post_id)})
        if post is None:
            return '404 Post not found', 404

        post['_id'] = post_id
        return post, 200

    def delete_post_by_id(self, post_id: str):
        result = self.collection.delete_one({'_id': ObjectId(post_id)})
        return '', 204


    def create_new_post(self, text: str, author: str) -> str:
        post = Post(text=text, author=author)
        created_id = self.collection.insert_one(post.to_json()).inserted_id
        return str(created_id)

    def update_post_by_id(self, post_id: str, text: str, author: str):
        self.collection.update_one({'_id': ObjectId(post_id)},
                                   {"$set":{"text": text, "author": author}})
        return 

    

    def print_about(self) -> None:
        print(f'{self.client=}\n'
              f'{self.db=}\n'
              f'{self.collection = }')


if __name__ == "__main__":
    MONGO_HOST = "localhost"
    MONGO_PORT = 27017
    mongo_client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")

    post_repo = PostRepository(mongo_client)

    post_repo.create_new_post(text='Alliluya', author="sviat")
