import random
import string
from bson import ObjectId

from models import Post
from structure import post_tranlator


class PostFactory:
    def get(self, title: str = None, content: str = None) -> Post:
        STR_LEN = 10
        post = Post()
        post.title = "title" if title is None else title
        post.content = "content" if content is None else content
        post.author_id = ObjectId()
        post.comment_ids = []
        return post

    def get_document(self, title: str) -> dict:
        return post_tranlator.to_document(self.get(title=title))

    def get_many_models(self, count: int) -> list[Post]:
        return [self.get(title=f"{i}-post") for i in range(count)]

    def get_many_documents(self, count: int) -> list[dict]:
        return [self.get_document(title=f"{i}-post") for i in range(count)]
