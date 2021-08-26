import json

from bson.objectid import ObjectId
from models import Post
from .translator import Translator


class PostTranslator(Translator):

    def to_document(self, post: Post) -> dict:
        return {
            "title": post.title,
            "content": post.content,
            "author_id": post.author_id,
            "comment_ids": post.comment_ids
        }

    def from_document(self, mongo_post: dict) -> Post:
        post = Post()
        post.id = mongo_post.get("_id")
        post.title = mongo_post.get("title")
        post.content = mongo_post.get("content")
        post.author_id = mongo_post.get("author_id")
        post.comment_ids = mongo_post.get("comment_ids")
        return post
