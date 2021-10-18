import math

from repositories.mongo_repository import MongoRepository
from models import Post, Page


class PostRepository(MongoRepository):
    def __init__(self, translator, collection):
        super().__init__(translator, collection)

    def get_page(self, page: int, page_size: int) -> Page:
        posts = self.collection.find().sort('_id', -1) \
            .skip(page * page_size - page_size) \
            .limit(page_size)
        posts = [
            self.translator.from_document(post)
            for post in posts
            if post is not None
        ]
        doc_count: int = self.collection.count_documents({})
        page_obj = Page()
        page_obj.items = posts
        page_obj.page = page
        page_obj.page_size = page_size
        page_obj.page_count = self._calc_page_count(doc_count, page_size)

        return page_obj

    def _calc_page_count(self, doc_count: int, page_size: int) -> int:
        count = math.ceil(doc_count / page_size)
        return count if count != 0 else 1
