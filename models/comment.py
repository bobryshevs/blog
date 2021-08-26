from bson.objectid import ObjectId
from .model import Model


class Comment(Model):
    def __init__(self):
        self.id: ObjectId = None
        self.author_id: ObjectId = None
        self.text: str = None

    @staticmethod
    def from_request(args: dict):
        comment = Comment()
        comment.author_id = args.get("author_id")
        comment.text = args.get("text")
        return comment
