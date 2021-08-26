from translators.post_tranlator import PostTranslator
from pymongo import MongoClient
from bson import ObjectId
from repositories.mongo_repository import MongoRepository
from models import Post


class PostRepository(MongoRepository):
    def __init__(self, translator, collection):
        super().__init__(translator, collection)

    def get_page(self, page: int, page_size: int) -> list[Post]:
        posts = self.collection.find().sort('_id', -1) \
            .skip(page * page_size - page_size) \
            .limit(page_size)
        posts = [
            self.translator.from_document(post)
            for post in posts
            if post is not None
        ]
        return posts
