import json

from bson.objectid import ObjectId
from models import Post
from json_serializers import JsonSerializer


class JsonPostSerializer(JsonSerializer):

    def present(self, post: Post) -> str:
        return json.dumps(
            {
                "_id": str(post.id),
                "title": post.title,
                "content": post.content,
                "author_id": str(post.author_id),
                "comment_ids": [str(com_id) for com_id in post.comment_ids]
            }
        )

    def from_json(self, value: dict) -> Post:
        post = Post()
        post.id = ObjectId(value.get("_id"))
        post.title = value.get("title")
        post.content = value.get("content")
        post.author_id = ObjectId(value.get("author_id"))
        post.comment_ids = [ObjectId(cid) for cid in value.get("comment_ids")]
        return post
