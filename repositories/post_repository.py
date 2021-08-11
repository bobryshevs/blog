from typing import Any
from pymongo import MongoClient
from bson import ObjectId
from repositories.repository import Repository
from structure import post_translator
from models.post import Post


class PostRepository(Repository):
    def __init__(self, client: MongoClient):
        self.client = client
        self.db = client.blog_database
        self.collection = client.blog_database.posts


    def get_pages(self, 
                  page_number: int, 
                  page_size: int
                  ) -> list[Post]:
    
        posts = list(self.collection.find().sort('_id', -1) \
                .skip(page_number*page_size - page_size)\
                .limit(page_size))
        posts = [
            post_translator.from_mongo(post)
            for post in posts
            if post is not None
        ]
        return posts

    def get_by_id(self, post_id: str) -> Any:
        if not self.is_valid_obj_id(post_id):
            return None
        obj_post_id = ObjectId(post_id)
        post = self.collection.find_one({"_id": obj_post_id})
        return post_translator.from_mongo(post)

    def delete_by_id(self, post_id: str) -> bool:
        deleted = True
        
        if not self.is_valid_obj_id(post_id) \
            or self.get_by_id(post_id) is None:
            return not deleted

        self.collection.delete_one({'_id': ObjectId(post_id)})
        return deleted 


    def create(self, text: str, author: str) -> str:
        post = Post(text=text, author=author)
        created_id = self.collection.insert_one(post.to_json()).inserted_id
        return str(created_id)

    def update(self, post_id: str, text: str, author: str):
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

    post_repo.create(text='Alliluya', author="sviat")
