import json

from bson.objectid import ObjectId
from models import Post
from .translator import Translator


class PostTranslator(Translator):

    # === Mongo === #
    def to_document(self, post: Post) -> dict:
        return {
            "title": post.title,
            "content": post.content,
            "author_id": post.author_id
        }

    def from_document(self, mongo_post: dict) -> Post:
        post = Post()
        post.id = mongo_post.get("_id")
        post.title = mongo_post.get("title")
        post.content = mongo_post.get("content")
        post.author_id = mongo_post.get("author_id")
        post.comment_ids = mongo_post.get("comment_ids")
        return post
    # =============== #

    # === REDIS && RMQ === #
    def to_json_str(self, post: Post) -> str:
        return json.dumps(
            {
                "_id": str(post.id),
                "title": post.title,
                "content": post.content,
                "author_id": str(post.author_id),
                "comment_ids": [str(com_id) for com_id in post.comment_ids]
            }
        )

    def from_json_str(self, value: str) -> Post:
        post = self.from_document(json.loads(value))
        post.id = ObjectId(post.id)
        post.author_id = ObjectId(post.author_id)
        post.comment_ids = [ObjectId(com_id) for com_id in post.comment_ids]
        return post
    # =============== #
