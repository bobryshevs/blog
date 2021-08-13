from datetime import datetime
from translators.post_tranlator import PostTranslator
from pymongo import MongoClient
from bson import ObjectId
from repositories.repository import Repository
from models import Post


class PostRepository(Repository):
    def __init__(self, client: MongoClient, translator: PostTranslator):
        super().__init__(translator)
        self.client = client
        self.collection = client.blog_database.posts

    def get_pages(self,
                  page_number: int,
                  page_size: int
                  ) -> list[Post]:

        posts = list(self.collection.find().sort('_id', -1)
                     .skip(page_number*page_size - page_size)
                     .limit(page_size))
        posts = [
            self.translator.from_document(post)
            for post in posts
            if post is not None
        ]
        return posts

    def get_by_id(self, post_id: ObjectId) -> Post:
        post = self.collection.find_one({"_id": post_id})
        if post is not None:
            return self.translator.from_document(post)
        return None

    def delete_by_id(self, post_id: ObjectId) -> bool:
        if self.exists(post_id):
            self.collection.delete_one({'_id': post_id})
            return True
        return False

    def create(self, text: str, author: str) -> ObjectId:
        post = Post(text, author, datetime.now())
        created_id = self.collection.insert_one(
            self.translator.to_document(post)).inserted_id
        return created_id

    def update(self, post: Post) -> Post:
        if not self.exists(post.id):
            return None
        self.collection.update_one(
            {'_id': post.id},
            {"$set": {self.translator.to_document(post)}})
        return self.get_by_id(post.id)

    def exists(self, post_id: ObjectId) -> bool:
        return self.get_by_id(post_id) is not None
