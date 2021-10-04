import math

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
        doc_count: int = self.collection.count_documents({})
        page = {
            "items": posts,
            "page": page,
            "page_size": page_size,
            #  Zero division is not allowed by the validator
            "page_count": math.ceil(doc_count / page_size)
        }

        return page
