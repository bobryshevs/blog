from translators.post_tranlator import PostTranslator
from pymongo import MongoClient
from bson import ObjectId
from repositories.repository import Repository
from models import Post


class PostRepository(Repository):
    def __init__(self, client: MongoClient, translator: PostTranslator):
        super().__init__(translator)
        self.client = client
        self.coll = client.blog_database.posts

    def get_page(self, page: int, page_size: int) -> list[Post]:
        posts = list(self.coll.find().sort('_id', -1)
                     .skip(page * page_size - page_size)
                     .limit(page_size))
        posts = [
            self.translator.from_document(post)
            for post in posts
            if post is not None
        ]
        return posts

    def get_by_id(self, post_id: ObjectId) -> Post:
        post = self.coll.find_one({"_id": post_id})
        if not post:
            return None
        return self.translator.from_document(post)

    def delete(self, post_id: ObjectId) -> None:
        self.coll.delete_one({'_id': post_id})

    def create(self, post: Post) -> ObjectId:
        return self.coll.insert_one(self.translator.to_document(post)) \
            .inserted_id

    def update(self, post: Post) -> Post:
        if not self.exists(post.id):
            return None

        self.coll.update_one(
            {'_id': post.id},
            {"$set": {self.translator.to_document(post)}})
        return post

    def exists(self, post_id: ObjectId) -> bool:
        return self.get_by_id(post_id) is not None
